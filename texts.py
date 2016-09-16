#!/usr/bin/env python3
#-*- coding:utf-8 -*-

from time import sleep

class Text:
    def animated_text(self,text):
        for i in text:
            print(i,end="",flush=True)
            sleep(0.050)
        print()

    def logintext(self):
        text = """

    Welcome to EasytoMan , abbr. of Easy to Manipulate, this tool helps in creating & hiding security(encrypted) passwords.


    Please choose what you want to do , and pass next step.

    1- Login as [S]uper[U]ser
    2- Help
    3- Exit

    If you want more description about EasytoMan , choose "help"

        """

        self.animated_text(text)

    def firsttext(self):
        text = """

    Welcome to EasytoMan , abbr. of Easy to Manipulate, this tool helps in creating & hiding security(encrypted) passwords.


    Apparently, the first time in this program.You must be change new password to Super User.

    If you want more description about EasytoMan , choose "help"

        """

        self.animated_text(text)

    def helptext(self):
        text = """
    EasytoMan , created in 2016, September by ExpectoTR.This tool's main mission is create more powerful and hacked to almost impossible passwords and safety hiding it.

    Briefly, this tool takes a word and a key from you to which platform(twitter, mega, reddit, wifi etc.) want you to do encryption.The word and key must be MEMORABLE.
    This tool encrypts according to a specific algorithm with key and word.Then save the encrypted cipher in "hashes.txt"

    |> What is [S]uper[U]ser ?
    SuperUser is most authorized user in tool, like root in Linux systems.
    If you choose SuperUser (can choose 1 instead "su"), it will ask you SuperUser password.When enter the correct password, you log in as root user.So, this tool not be asked you key and word.
    Just give platform name and it gives your platform password.Also, SuperUser can change the authority on the platform passwords.(access,change etc.)

    |> Why use Easytoman ?
    Normal passwords occurs just one text(including alphanumeric etc.).. For example = ExpectoTR2016
    When the malicious people are want your account, it will be easy to break your password.
    But if you encrypt with Easytoman, you will enter two values(word and key) and Easytoman encrypt this values with special encryption algorithm.
    So, break your password not although impossible,  more than enough difficult...



        """
        self.animated_text(text)

    def process(self):
        while True:
            text = """
            Choose what you want to do ?

            1- Get password of Platform
            2- Create new Platform

            """
            self.animated_text(text)
            option = input(self.animated_text("Choose one (1 or 2)  "))
            if option == "1":
                return 1
            elif option == "2":
                return 0
            else:
                print("Wrong Value! ")