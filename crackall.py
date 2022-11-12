import hashlib
import sys
import colorama
import os
import time

colorama.init(autoreset=True)

class Cracker():
    def __init__(self):
        logo = """#############################################
                                            #
One of the fastest hash crackers.           #
"CrackAll" by nonTrouble.                   #
                                            #
#############################################"""
        os.system("echo off")
        os.system("cls")
        print(colorama.Fore.YELLOW+logo)
        print("\n")
        

    def crackHash(self,hash,wordlist,hashtype="md5"):

        found = 0

        try:
            with open(wordlist,"r",encoding="utf-8") as file:
                data = file.read()
        except FileNotFoundError:
            print(colorama.Fore.RED+"File is not found.")
            return False
        
        data = str(data).split("\n")
        
        if hashtype=="md5":
            for password in data:
                sHash = hashlib.md5(password.encode())
                sHash = sHash.hexdigest()
                if sHash == hash:
                    print(colorama.Fore.WHITE+"Found : {}".format(colorama.Fore.BLUE+password))
                    print("\n")
                    found = 1
                    return True

        elif hashtype=="sha256":
            for password in data:
                sHash = hashlib.sha256(password.encode())
                sHash = sHash.hexdigest()
                if sHash == hash:
                    print(colorama.Fore.WHITE+"Found : {}".format(colorama.Fore.BLUE+password))
                    print("\n")
                    found = 1
                    return True

        elif hashtype=="sha512":
            for password in data:
                sHash = hashlib.sha512(password.encode())
                sHash = sHash.hexdigest()
                if sHash == hash:
                    print(colorama.Fore.WHITE+"Found : {}".format(colorama.Fore.BLUE+password))
                    print("\n")
                    found = 1
                    return True
        else:
            print("Available hashtypes : md5,sha256,sha512")
            return False

        if found == 0:
            print(colorama.Fore.RED+"The hash object you tried to crack is not crackable with this wordlist.Try another")
            print("\n")
            return False
  
  
#Sample Code
  
cracker = Cracker()
cracker.crackHash("a665a45920422f9d417e4867efdc4fb8a04a1f3fff1fa07e998e86f7f7a27ae3","wordlist/rockyou.txt","sha256")


"""#############################################
                                            #
One of the fastest hash crackers.           #
"CrackAll" by nonTrouble.                   #
                                            #
#############################################


Found : 123"""
            



    



    

    
