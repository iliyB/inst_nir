import utils
from enum import Enum
import instagrapi
import os

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
        print("Login in is successful")



    def download_resources(self, resources, source: Source ,path: str):
        utils.create_folder(path + "/photo")
        utils.create_folder(path + "/feed")
        utils.create_folder(path + "/igtv")
        utils.create_folder(path + "/clips")
        utils.create_folder(path + "/album")

        for resource in resources:
            if resource.media_type == typeId.photo.value:
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

    def download_resources_from_main_page(self, username: str, path: str = os.getcwd()):

        user_id = self.client.user_id_from_username(username)
        medias = self.client.user_medias(user_id)

        utils.create_folder(path + "/" + username)
        utils.create_folder(path + "/" + username + "/resources_from_main_page")

        self.download_resources(medias, Source.media, path + "/" + username + "/resources_from_main_page")

    def download_resources_from_stories(self, username: str, path: str = os.getcwd()):

        user_id = self.client.user_id_from_username(username)
        stories = self.client.user_stories(user_id)

        utils.create_folder(path + "/" + username)
        utils.create_folder(path + "/" + username + "/resources_from_stories")

        self.download_resources(stories, Source.story, path + "/" + username + "/resources_from_stories")
