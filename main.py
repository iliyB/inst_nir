from instUser import instUser


if __name__ == '__main__':

    user = instUser("mih_raf", "IZImail117")
    user.download_resources_from_main_page("vira.dur")
    user.download_resources_from_stories("vira.dur")


