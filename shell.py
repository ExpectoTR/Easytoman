#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import os
import sys
from encode import Encode

#--------------------- DEFINITIONS ---------------------

platform_list = []
crypt = Encode()

try:
	with open("hashes.txt", "r") as f:
	    read = f.readlines()
except FileNotFoundError:
	os.system("touch hashes.txt")
	with open("hashes.txt", "r") as f:
		    read = f.readlines()

read = "".join(read).split("$")
for platform in read[3::2]:
    platform_list.append(platform)

#--------------------- FUNCTIONS ---------------------

def lists():
    try:
        with open("hashes.txt", "r") as f:
            read = f.readlines()

        read = "".join(read).split("$")
        final_platform = platform_list[-1]
        if read[-2] != final_platform:
            #x= -2
            platform_list.append(read[-2])
            # If you're enter more than one argument, without command list, it gives only last one argument.
            # In the following rows, will update soon.
            """
            x = (read.index(read[-2]) - read.index(final_platform))*(-2)
            while read[x] != final_platform:
                x+=2
                platform_list.append(read[x])
            """

        print("All platforms in following line!\n")
        for i in platform_list:
            print(i.capitalize())
        if read[-2] != platform_list[-1]:
            print(read[-2].capitalize())
        print()
    except IndexError:
        print("There are no platforms here :) Please add new platform using \"new\" ")



def shell():
    while True:
        command = input("shell> ").lstrip(" ").rstrip(" ")
        if command == "help":
            print("""
    Following commands will be useful to you.

    clear - clear the screen
    list - list all saved platforms
    new - create new platform
    del - delete platform
    getpw - give password of platform
    restart - restart the program
    exit - exit the program
            """)

        elif command == "clear":
            os.system("clear")
            print("\t\tEasytoman Shell\t\t")

        elif command == "list":
            lists()

        elif command == "new":
            platform = input("Please enter the platform name (twitter,facebook etc.) >  ")
            platform = platform.lower()
            word = input("Word >  ")
            key = input("Key >  ")
            crypt.encode_save(word,key,platform)
            print("Successfully added new platform!")

        elif command == "getpw":
            platform_name = input("Please enter the platform name (twitter,facebook etc.) >  ").lower()
            word = input("Word (Sensitive) >  ")
            key = input("Key (Sensitive) >  ")
            if crypt.isplatform_hash(word, key, platform_name):
                print("\n\nYour " + str(platform_name).capitalize() + "'s password is " + "\"" + crypt.encode_algorithm_main(word,key) + "\" (without quotes)\n\n")
            else:
                print("Wrong word or key!")

        elif command == "restart":
            os.system("clear")
            os.system("exit")
            os.system("./easytoman.py")

        elif command == "del":
            lists()
            option = input("Please enter the platform name you want to delete\n")
            yesno = input("You're removing {} 's password.Are you sure ?  y/n  ".format(option))
            if yesno == "y":
                if option in platform_list:
                    line = platform_list.index(option) +1
                    with open("hashes.txt", "r") as f:
                        readfile = f.readlines()
                        readfile.remove(readfile[int(line)])
                    with open("hashes.txt","w") as file:
                        file.write("".join(readfile))
                    print("Successful.But, if you enter \"list\", maybe the platform still visible.Forget about it. :)")
            elif yesno == "n":
                pass
            else:
                print("Wrong value!")

        elif command == "exit":
            sys.exit()
        else:
            print("Command not found!")