#!/usr/bin/env python3
#-*- coding:utf-8 -*-

import hashlib
import base64

class Encode:
    def __init__(self):
        self.org_pw = ""

    def encodewithMD5(self,value):
        return hashlib.md5(value.encode("utf-8")).hexdigest()

    def encodewithSHA512(self,value):
        return hashlib.sha512(value.encode("utf-8")).hexdigest()

    def encodewithB64(self,value):
        return base64.b64encode(bytes(value,"utf-8"))

    def encode_algorithm_main(self, word, key):
        word_md5 = self.encodewithMD5(word)
        key_md5 = self.encodewithMD5(key)
        total = str(word_md5) + str(key_md5)
        total_SHA512 = self.encodewithSHA512(total)
        total_SHA512_list = list(total_SHA512)
        org_pw_list = []
        pw_list = []
        i = 0
        sayac = 0
        for i in total_SHA512_list[0:127:3]:
            if total_SHA512_list.index(i) % 2 == 0:
                pw_list.append(i.swapcase())
            else:
                pw_list.append(i)
        while len(org_pw_list) < 18:
            org_pw_list.append(pw_list[sayac])
            sayac +=1

        return "".join(org_pw_list)

    def encode_algorithm_in_hashtext(self,word,key,platform_name):
        org_pw = self.encode_algorithm_main(word,key)
        org_pw_encoded = self.encodewithSHA512(str(self.encodewithMD5("expecto"))+str(self.encodewithMD5(org_pw)))
        org_pw_in_hashtext = str("$"+str(platform_name)+"$")+str(org_pw_encoded)+str(org_pw_encoded[::-7])+ str("\n")
        return org_pw_in_hashtext


    def encode_save(self,word,key,platform_name):
        with open("hashes.txt","a") as file:
            file.write(self.encode_algorithm_in_hashtext(word,key,platform_name))

    def su_pass(self,password):
        pw = self.encodewithMD5(self.encodewithSHA512(password))
        su_pw_in_hashtext = "$password$"+str(pw)
        with open("hashes.txt","w") as file:
            file.write(su_pw_in_hashtext+str("\n"))

    def su_pass_verify(self,password):
        pw = self.encodewithMD5(self.encodewithSHA512(password)) + str("\n")
        with open("hashes.txt","r") as file:
            passwd = file.readline().split("$")
        if pw == passwd[2]:
            return True
        else:
            return False

    def isplatform_hash(self,word,key,platform_name):
        hash = self.encode_algorithm_in_hashtext(word,key,platform_name).split("$")[2]
        with open("hashes.txt","r") as f:
            readlines = f.readlines()
            readlines = "".join(readlines).split("$")
            index = readlines.index(platform_name)+1
        if hash == readlines[index].split("\n")[0]+str("\n"):
            return True
        else:
            return False