#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import getpass
import os
import sys
from time import sleep
import encode
from texts import Text
from shell import shell

enc = encode.Encode()
txt = Text()

os.system("clear")

try:
	with open("hashes.txt","r") as file:
	    value = file.readline().split("$")
except FileNotFoundError:
	os.system("touch hashes.txt")
	with open("hashes.txt","r") as file:
		    value = file.readline().split("$")
if "password" in value:
    txt.logintext()
    while True:
        option = input("Choose one (su, help or exit)  ")
        if option == "1" or option == "su":
            # Login as Super User
            pw = getpass.getpass("\nPlease enter the su password  ")
            if enc.su_pass_verify(pw):
                print("\nPassword Correct! You logged in successfully..Please wait...\n")
                sleep(2)
                os.system("clear")
                print("\t\tWelcome to Easytoman Shell\t\t")
                shell()
            else:
                print("Oh,no.Somethings wrong!\n")


        elif option == "2" or option == "help":
            txt.helptext()

        elif option == "3" or option == "exit":
            sys.exit()

        else:
            print("Input is invalid.")
else:
    txt.firsttext()
    pw = getpass.getpass("\nPlease enter the first su password  ")
    enc.su_pass(pw)
    print("Success...Please write \"./easytoman.py\" again.\n")
    sys.exit()


