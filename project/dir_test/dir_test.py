"""
*Filename         :dir_test.py
*Description      :Test  to see if the directory testdir exist
*Time             :2023/08/29 00:25:00
*Author           :jacksonhack
*Version          :1.0


"""

from __future__ import print_function

import os

try:
    input = raw_input()
except NameError:
    pass


def main():
    check_dir = input("Enter the name of directory to check : ")
    print()

    if os.path.exists(check_dir):
        print("The directory exist.")
        os.rmdir(check_dir)
    else:
        print("No directory found for " + check_dir)
        print()
        option = input("Would you like this directory create? y/n")
        if option == "n":
            print("GoodBy")
        elif option == "y":
            os.makedirs(check_dir)
            print("Directory created for " + check_dir)
        else:
            print("Not an option. Exiting")


if __name__ == "__main__":
    main()
