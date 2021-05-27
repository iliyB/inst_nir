import utils
from enum import Enum
import instagrapi
import os
from DataXml import *
from detector import *

class typeId(Enum):
    photo = 1
    video = 2
    igtv  = 2
    reels = 2
    album = 8

class Source(Enum):
    media = 0
    story = 1

class instUser():

    def __init__(self, login: str, password: str):
        self.client = instagrapi.Client()
        self.client.login(login, password)
        self.detector_photo = detector_photo()
        print("Login in is successful")

    def check_resources(self, resources, source: Source, path_main: str, xml: DataXml):
        utils.create_folder(path_main + "/photo")
        utils.create_folder(path_main + "/feed")
        utils.create_folder(path_main + "/igtv")
        utils.create_folder(path_main + "/clips")
        utils.create_folder(path_main + "/album")

        for resource in resources:
            print()
            print()
            print("new resource")
            if source == Source.story and xml.check_story(resource.pk):
                print("Story is have")
                continue
            elif source == Source.media and xml.check_media(resource.pk):
                print("Media is have")
                continue

            date = resource.taken_at.date()
            if source == Source.story and resource.mentions:
                users = []
                for usertag in resource.mentions:
                    users.append((dict(dict(usertag).get('user'))['username']))
                for user in users:
                    xml.add_friend(user, str(date))
            elif source == Source.media:
                hashtags = self.get_hashtags_from_caption(resource.caption_text)
                if hashtags:
                    for hashtag in hashtags:
                        xml.add_hashtag(str(hashtag), str(date))

                if resource.usertags:
                    users = []
                    for usertag in resource.usertags:
                        users.append((dict(dict(usertag).get('user'))['username']))
                    for user in users:
                        xml.add_friend(user, str(date))

            print("Hashtags and friends")

            if source == Source.story:
                if resource.media_type == typeId.photo.value:
                    type = "photo"
                elif resource.media_type == typeId.album.value:
                    type = "album"
                else:
                    type = resource.product_type

                objects = {}
                if resource.media_type == typeId.photo.value:
                    file_name = "{username}_{story_pk}.jpg".format(
            username=xml.get_current_user(), story_pk=resource.pk)

                    if os.path.isfile(path_main + '/photo/' + file_name):
                        path = path_main + '/photo/' + file_name
                        print("file is have")
                    else:
                        path = self.client.photo_download_from_story(resource.pk, path_main + "/photo")
                        print("downloaded")
                    objects_ = self.detector_photo.detectorRetinaNet_from_photo(path)
                    print("send objects")
                    for k in objects_.keys():
                        if k in objects:
                            objects[k] += objects_[k]
                        else:
                            objects.update({k: objects_[k]})
                elif resource.media_type == typeId.video.value and resource.product_type == 'feed':
                    path = self.client.video_download_from_story(resource.pk, path_main + "/feed")
                elif resource.media_type == typeId.igtv.value and resource.product_type == 'igtv':
                    path = self.client.video_download_from_story(resource.pk, path_main + "/igtv")
                elif resource.media_type == typeId.reels.value and resource.product_type == 'clips':
                    path = self.client.video_download_from_story(resource.pk, path_main + "/clips")

                print(objects)
                xml.add_story(resource.pk, str(date), type, objects)

            elif source == Source.media:
                if resource.media_type == typeId.photo.value:
                    type = "photo"
                elif resource.media_type == typeId.album.value:
                    type = "album"
                else:
                    type = resource.product_type

                objects = {}
                if resource.media_type == typeId.photo.value:
                    file_name = "{username}_{story_pk}.jpg".format(
                        username=xml.get_current_user(), story_pk=resource.pk)

                    if os.path.isfile(path_main + '/photo/' + file_name):
                        path = path_main + '/photo/' + file_name
                        print("file is have")
                    else:
                        path = self.client.photo_download(resource.pk, path_main + "/photo")
                        print("downloaded")
                    objects_ = self.detector_photo.detectorRetinaNet_from_photo(path)
                    print("send objects")
                    for k in objects_.keys():
                        if k in objects:
                            objects[k] += objects_[k]
                        else:
                            objects.update({k: objects_[k]})
                elif resource.media_type == typeId.video.value and resource.product_type == 'feed':
                    path = self.client.video_download(resource.pk, path_main + "/feed")
                elif resource.media_type == typeId.igtv.value and resource.product_type == 'igtv':
                    path = self.client.video_download(resource.pk, path_main + "/igtv")
                elif resource.media_type == typeId.reels.value and resource.product_type == 'clips':
                    path = self.client.video_download(resource.pk, path_main + "/clips")
                elif resource.media_type == typeId.album.value:
                    file_name = "{username}_{story_pk}.jpg".format(
                        username=xml.get_current_user(), story_pk=resource.resources[0].pk)
                    if os.path.isfile(path_main + '/album/' + file_name):
                        paths = []
                        for r in resource.resources:
                            paths.append(path_main + '/album/' + "{username}_{story_pk}.jpg".format(
                        username=xml.get_current_user(), story_pk=r.pk))
                        print("album is have")
                    else:
                        paths = self.client.album_download(resource.pk, path_main + "/album")
                        print("album downloaded")
                    for path in paths:
                        objects_ = self.detector_photo.detectorRetinaNet_from_photo(path)
                        print("send objects")
                        for k in objects_.keys():
                            if k in objects:
                                objects[k] += objects_[k]
                            else:
                                objects.update({k: objects_[k]})

                print(objects)
                xml.add_media(resource.pk, str(date), type, objects)

        xml.commit()




    def download_resources(self, resources, source: Source, path: str):
        utils.create_folder(path + "/photo")
        utils.create_folder(path + "/feed")
        utils.create_folder(path + "/igtv")
        utils.create_folder(path + "/clips")
        utils.create_folder(path + "/album")

        for resource in resources:

            if resource.media_type == typeId.photo.value:
                if source.value:
                    self.client.photo_download_from_story(resource.pk, path + "/photo")
                else:
                    self.client.photo_download(resource.pk, path + "/photo")
            elif resource.media_type == typeId.video.value and resource.product_type == 'feed':
                if source.value:
                    self.client.video_download_from_story(resource.pk, path + "/feed")
                else:
                    self.client.video_download(resource.pk, path + "/feed")
            elif resource.media_type == typeId.igtv.value and resource.product_type == 'igtv':
                if source.value:
                    self.client.video_download_from_story(resource.pk, path + "/igtv")
                else:
                    self.client.video_download(resource.pk, path + "/igtv")
            elif resource.media_type == typeId.reels.value and resource.product_type == 'clips':
                if source.value:
                    self.client.video_download_from_story(resource.pk, path + "/clips")
                else:
                    self.client.video_download(resource.pk, path + "/clips")
            elif resource.media_type == typeId.album.value:
                self.client.album_download(resource.pk, path + "/album")

    def check_resources_from_main_page(self, username: str, xml: DataXml, path: str = os.getcwd()):

        xml.select_user(username)
        user_id = self.client.user_id_from_username(username)
        medias = self.client.user_medias(user_id)

        utils.create_folder(path + "/" + username)
        utils.create_folder(path + "/" + username+ "/resources_from_main_page")
        self.check_resources(medias, Source.media, path + "/" + username + "/resources_from_main_page", xml)

    def check_resources_from_stories(self, username: str, xml: DataXml, path: str = os.getcwd()):

        xml.select_user(username)
        user_id = self.client.user_id_from_username(username)
        stories = self.client.user_stories(user_id)

        utils.create_folder(path + "/" + username)
        utils.create_folder(path + "/" + username + "/resources_from_stories")
        self.check_resources(stories, Source.story, path + "/" + username + "/resources_from_stories", xml)


    def download_resources_from_main_page(self, username: str, path: str = os.getcwd()):

        user_id = self.client.user_id_from_username(username)
        medias = self.client.user_medias(user_id)

        utils.create_folder(path + "/" + username)
        utils.create_folder(path + "/" + username+ "/resources_from_main_page")

        self.download_resources(medias, Source.media, path + "/" + username + "/resources_from_main_page")

    def download_resources_from_stories(self, username: str, path: str = os.getcwd()):

        user_id = self.client.user_id_from_username(username)
        stories = self.client.user_stories(user_id)

        utils.create_folder(path + "/" + username)
        utils.create_folder(path + "/" + username + "/resources_from_stories")

        self.download_resources(stories, Source.story, path + "/" + username + "/resources_from_stories")

    def get_hashtags_from_caption(self, caption: str):
        try:
            hashtags = []
            while caption.find("#"):
                hashtag = ""
                i = caption.index("#")
                while len(caption) > (i + 1) and caption[i + 1] != " " and caption[i + 1] != "\n":
                    hashtag += caption[i + 1]
                    i += 1

                hashtags.append(hashtag)
                caption = caption.replace("#", "", 1)
        except Exception:
            pass

        return hashtags
