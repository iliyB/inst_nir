import os
import matplotlib.pyplot as plt
import operator

def create_folder(folder: str):
    if not os.path.isdir(folder):
        os.mkdir(folder)

def delete_file(file: str):
    if os.path.isfile(file):
        os.remove(file)

def sorted_dict(dict1: {}):
    sorted_turple = sorted(dict1.items(), key=operator.itemgetter(1))
    sorted_dict = {}

    for k, v in reversed(sorted_turple):
        sorted_dict.update({k: v})

    return sorted_dict

def get_short_dict(full_dict: {}, length: int):
    short_dict = {}
    i = 0
    for key in full_dict.keys():
        if i >= length:
            break
        else:
            i += 1
        short_dict.update({key : full_dict[key]})

    return short_dict

def save_plot(dict: {}, path: str, left: float):
    s = [dict[key] for key in dict.keys()]
    x = range(len(s))
    plt.close()
    ax = plt.gca()
    ax.barh(x, s, align='edge')  # align='edge' - выравнивание по границе, а не по центру
    plt.yticks(x, dict.keys())
    plt.subplots_adjust(left=left)
    plt.savefig(path)

def get_filename(username: str, type: str):
    return "{username}_{type}.jpg".format(
        username=username, type=type)