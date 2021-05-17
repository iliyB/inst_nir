import os


def create_folder(folder: str):
    if not os.path.isdir(folder):
        os.mkdir(folder)