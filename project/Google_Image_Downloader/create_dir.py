"""
*Filename         :create_dir.py
*Description      :
*Time             :2023/08/28 18:58:37
*Author           :jacksonhack
*Version          :1.0

"""

import os
from os import chdir
from os import makedirs
from os import removedirs
from os import remove
from os import rename
from os import rmdir
from os.path import exists
from os.path import pardir  # * parent_directory
from os.path import curdir
from shutil import copytree
from shutil import move
from shutil import rmtree
import stat


# create a directory
def create_directory(name):
    if exists(pardir + "/" + name):
        print("Folder already exist...Cannot Overwhrite this")
    else:
        makedirs(pardir + "/" + name)


def touch(name):
    with open(name, "w"):
        pass


def delete_directory(path):
    os.chmod(path, stat.S_IWRITE)
    rmtree(path)


def backup_files(name_dir, folder):
    des_dir = name_dir + ":\\" + folder
    # print(des_dir)
    if exists(des_dir):
        delete_directory(des_dir)
    copytree(cwd, name_dir + ":\\" + folder)


def move_foders(filename, name_dir, folder):
    if not exists(name_dir + ":\\" + folder):
        makedirs(name_dir + ":\\" + folder)
    move(filename, name_dir + ":\\" + folder)


cwd = "../../"


def main():
    print()
    # create_directory(dir)
    # rename(pardir + '/' + dir, pardir + '/' + dir + 'hhh')
    # backup_files('B', 'back_proj')

    # delete_directory(pardir + "/" + dir)


if __name__ == "__main__":
    main()
