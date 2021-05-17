from instUser import instUser


if __name__ == '__main__':

    user = instUser(USERNAME, PASSWORD)
    user.download_resources_from_main_page(TARGET)
    user.download_resources_from_stories(TARGET)


