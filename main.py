from instUser import instUser
from DataXml import DataXml
from utils import *
import login


def get_plots(usernames: [], xml: DataXml):
    for username in usernames:
        print()
        print(username)
        if not username in xml.get_users():
            print("Создание нового пользователя в БД")
            xml.add_user(username)
        xml.select_user(username)
        path = os.getcwd() + "/" + username + "/plots"
        create_folder(path)

        print("Hashtags")
        hashtags = sorted_dict(xml.get_user_hashtags())
        print(hashtags)
        save_plot(get_short_dict(hashtags, 15), path + "/" + get_filename(username, "hashtags"), 0.3)

        print("Friends")
        friends = sorted_dict(xml.get_user_friends())
        print(friends)
        save_plot(get_short_dict(friends, 15), path + "/" + get_filename(username, "friends"), 0.3)

        print("Types of resources")
        types = sorted_dict(xml.get_user_types_of_resources())
        print(types)
        save_plot(get_short_dict(types, 15), path + "/" + get_filename(username, "types"), 0.1)


        print("Objects with resources")
        objects = sorted_dict(xml.get_user_objects_with_resources())
        print(objects)
        save_plot(get_short_dict(objects, 15), path + "/" + get_filename(username, "objects"), 0.2)

def get_plots_for_the_days(usernames: [], xml: DataXml, days: int):
    for username in usernames:
        print()
        print(username)
        if not username in xml.get_users():
            print("Создание нового пользователя в БД")
            xml.add_user(username)
        xml.select_user(username)
        path = os.getcwd() + "/" + username + "/plots" + str(days)
        create_folder(path)

        print("Hashtags")
        hashtags = sorted_dict(xml.get_user_hashtags_for_the_days(days))
        print(hashtags)
        save_plot(get_short_dict(hashtags, 15), path + "/" + get_filename(username, "hashtags"), 0.3)

        print("Friends")
        friends = sorted_dict(xml.get_user_friends_for_the_days(days))
        print(friends)
        save_plot(get_short_dict(friends, 15), path + "/" + get_filename(username, "friends"), 0.3)

        print("Types of resources")
        types = sorted_dict(xml.get_user_types_of_resources_for_the_days(days))
        print(types)
        save_plot(get_short_dict(types, 15), path + "/" + get_filename(username, "types"), 0.1)


        print("Objects with resources")
        objects = sorted_dict(xml.get_user_objects_with_resources_for_the_days(days))
        print(objects)
        save_plot(get_short_dict(objects, 15), path + "/" + get_filename(username, "objects"), 0.2)

def get_data(user: instUser, usernames: [], xml: DataXml):
    for username in usernames:
        print()
        print(username)
        if not username in xml.get_users():
            print("Создание нового пользователя в БД")
            xml.add_user(username)
        print("*****************************************")
        print("Check story")
        user.check_resources_from_stories(username, xml)
        print("*****************************************")
        print("Check media")
        user.check_resources_from_main_page(username, xml)
        print("*****************************************")



if __name__ == '__main__':

    user = instUser(login.Login, login.Password)

    xml = DataXml("bd.xml")
    #print("Введите никнейм пользователя:")
    usernames = ['vira.dur', 'kat.lun', 'zoopsychology.ru']

    #get_plots(usernames, xml)
    get_plots_for_the_days(usernames, xml, 4)












