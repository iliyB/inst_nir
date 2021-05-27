import xml.etree.ElementTree as xml
import os
import datetime

class DataXml:



    def __init__(self, filename: str, folder: str = os.getcwd()):
        self.tree = xml.parse(folder + "/" + filename)
        self.root = self.tree.getroot()
        self.current_user = None
        self.filename = filename
        self.folder = folder
        self.format_date = '%Y-%m-%d'

    def commit(self):
        self.tree.write(self.folder + "/" + self.filename)


    #Methods for work with user

    def get_users(self):
        return [child.attrib['username'] for child in self.tree.getroot()]

    def add_user(self, username: str):
        for user in self.tree.getroot().findall('user'):
            if user.attrib['username'] == username:
                raise Exception("User" + username + "exists")

        new_user = xml.Element('user', {'username': username, "activate": "true"})
        new_user.append(xml.Element("hashtags"))
        new_user.append(xml.Element("friends"))
        new_user.append(xml.Element("medias"))
        new_user.append(xml.Element("stories"))
        self.tree.getroot().append(new_user)



    def delete_user(self, username: str):
        for user in self.tree.getroot().findall('user'):
            if user.attrib['username'] == username:
                self.tree.getroot().remove(user)
                return True

        raise Exception("User" + username + "exists")

    def check_active_user(self, username: str):
        for user in self.tree.getroot().findall('user'):
            if user.attrib['username'] == username:
                return user.attrib['active'] == 'true'
        else:
            raise Exception("Username " + username + " isn't found")

    def activate_user(self, username: str):
        for user in self.tree.getroot().findall('user'):
            if user.attrib['username'] == username:
                user.set("active", "true")
                return True

        else:
            raise Exception("Username " + username + " isn't found")

    def deactivate_user(self, username: str):
        for user in self.tree.getroot().findall('user'):
            if user.attrib['username'] == username:
                user.set("active", "false")
                return True

        else:
            raise Exception("Username " + username + " isn't found")

    def select_user(self, username: str):
        for user in self.tree.getroot().findall('user'):
            if user.attrib['username'] == username:
                self.root = user
                self.current_user = username
                return True
        else:
            raise Exception("Username " + username + " isn't found")

    def get_current_user(self):
        return self.current_user

    def reset_user(self):
        self.root = self.tree.getroot()
        self.current_user = None

    #Methods for work with hashtags

    def add_hashtag(self, hashtag: str, date_str: str):
        new_hashtag = xml.Element("hashtag")
        name = xml.Element("name")
        name.text = hashtag
        date = xml.Element("date")
        date.text = date_str
        new_hashtag.append(name)
        new_hashtag.append(date)

        self.root.find('hashtags').append(new_hashtag)

    def get_user_hashtags(self):
        if not self.current_user:
            raise Exception("User isn't selected")

        hashtags = {}
        for hashtag in self.root.find('hashtags'):
            if hashtag[0].text in hashtags:
                hashtags[hashtag[0].text] += 1
            else:
                hashtags.update({hashtag[0].text: 1})

        return hashtags

    def get_user_hashtags_for_the_days(self, days: int):
        if not self.current_user:
            raise Exception("User isn't selected")

        hashtags = {}
        for hashtag in self.root.find('hashtags'):
            if (datetime.date.today() - datetime.datetime.strptime(
                        hashtag[1].text, self.format_date).date()
            ).days <= days:
                if hashtag[0].text in hashtags:
                    hashtags[hashtag[0].text] += 1
                else:
                    hashtags.update({hashtag[0].text: 1})

        return hashtags


    #Methods for work with friends

    def add_friend(self, friend: str, date_str: str):
        new_friend = xml.Element("friend")
        name = xml.Element("name")
        name.text = friend
        date = xml.Element("date")
        date.text = date_str
        new_friend.append(name)
        new_friend.append(date)

        self.root.find('friends').append(new_friend)

    def get_user_friends(self):
        if not self.current_user:
            raise Exception("User isn't selected")

        friends = {}
        for friend in self.root.find('friends'):
            if friend[0].text in friends:
                friends[friend[0].text] += 1
            else:
                friends.update({friend[0].text: 1})

        return friends

    def get_user_friends_for_the_days(self, days: int):
        if not self.current_user:
            raise Exception("User isn't selected")

        friends = {}
        for friend in self.root.find('friends'):
            if (datetime.date.today() - datetime.datetime.strptime(
                    friend[1].text, self.format_date).date()
            ).days <= days:
                if friend[0].text in friends:
                    friends[friend[0].text] += 1
                else:
                    friends.update({friend[0].text: 1})

        return friends

    #Methods for work with medias and stories

    def check_story(self, id_story: int):
        for story in self.root.find("stories"):
            if story.attrib['id'] == str(id_story):
                return True

        return False

    def add_story(self, id_story: int, date_str: str, type_str: str, objects_array: {}):
        new_story = xml.Element("story", {"id": str(id_story)})
        date = xml.Element("date")
        date.text = date_str
        type = xml.Element("type")
        type.text = type_str
        objects = xml.Element("objects")
        for key in objects_array.keys():
            object = xml.Element("object", {"name": key})
            count = xml.Element("count")
            count.text = str(objects_array[key])
            object.append(count)
            objects.append(object)

        new_story.append(date)
        new_story.append(type)
        new_story.append(objects)
        self.root.find("stories").append(new_story)

    def check_media(self, id_media: int):
        for media in self.root.find("medias"):
            if media.attrib['id'] == str(id_media):
                return True

        return False

    def add_media(self, id_media: int, date_str: str, type_str: str, objects_array: {}):
        new_media = xml.Element("media", {"id": str(id_media)})
        date = xml.Element("date")
        date.text = date_str
        type = xml.Element("type")
        type.text = type_str
        objects = xml.Element("objects")
        for key in objects_array.keys():
            object = xml.Element("object", {"name": key})
            count = xml.Element("count")
            count.text = str(objects_array[key])
            object.append(count)
            objects.append(object)

        new_media.append(date)
        new_media.append(type)
        new_media.append(objects)
        self.root.find("medias").append(new_media)

    def get_user_objects_with_resources(self):
        if not self.current_user:
            raise Exception("User isn't selected")

        objects = {}
        for media in self.root.find('medias'):
            for object in media.find('objects'):
                if object.attrib['name'] in objects:
                    objects[object.attrib['name']] += int(object[0].text)
                else:
                    objects.update({object.attrib['name']: int(object[0].text)})

        for story in self.root.find('stories'):
            for object in story.find('objects'):
                if object.attrib['name'] in objects:
                    objects[object.attrib['name']] += int(object[0].text)
                else:
                    objects.update({object.attrib['name']: int(object[0].text)})

        return objects

    def get_user_objects_with_resources_for_the_days(self, days: int):
        if not self.current_user:
            raise Exception("User isn't selected")

        objects = {}
        for media in self.root.find('medias'):
            if (datetime.date.today() - datetime.datetime.strptime(
                    media[0].text, self.format_date).date()
            ).days <= days:
                for object in media.find('objects'):
                    if object.attrib['name'] in objects:
                        objects[object.attrib['name']] += int(object[0].text)
                    else:
                        objects.update({object.attrib['name']: int(object[0].text)})

        for story in self.root.find('stories'):
            if (datetime.date.today() - datetime.datetime.strptime(
                    story[0].text, self.format_date).date()
            ).days <= days:
                for object in story.find('objects'):
                    if object.attrib['name'] in objects:
                        objects[object.attrib['name']] += int(object[0].text)
                    else:
                        objects.update({object.attrib['name']: int(object[0].text)})

        return objects



    def get_user_types_of_resources(self):
        if not self.current_user:
            raise Exception("User isn't selected")

        types = {}
        for media in self.root.find("medias"):
            if media[1].text in types:
                types[media[1].text] += 1
            else:
                types.update({media[1].text: 1})

        for story in self.root.find("stories"):
            if story[1].text in types:
                types[story[1].text] += 1
            else:
                types.update({story[1].text: 1})

        return types

    def get_user_types_of_resources_for_the_days(self, days: int):
        if not self.current_user:
            raise Exception("User isn't selected")

        types = {}
        for media in self.root.find("medias"):
            if (datetime.date.today() - datetime.datetime.strptime(
                    media[0].text, self.format_date).date()
            ).days <= days:
                if media[1].text in types:
                    types[media[1].text] += 1
                else:
                    types.update({media[1].text: 1})
        for story in self.root.find('stories'):
            if (datetime.date.today() - datetime.datetime.strptime(
                    story[0].text, self.format_date).date()
            ).days <= days:
                if story[1].text in types:
                    types[story[1].text] += 1
                else:
                    types.update({story[1].text: 1})

        return types






