import cryptography
from cryptography.fernet import Fernet
import os
import time
import shutil
source = os.getcwd()
version = "4.1"
print("[WARN] This script uses the OS module")
#print("\nWill create new working directory to add files\n")
def enccheck():
        print("Function was sucsefully called!")
        print("Key will be made by user discression")
        i = input("Do you agree to allow this program to access the required files? (y[encrypt]/n/decrypt): ")
        if i == "y":
            try:
                os.path.isfile(encfile)
                encrypt()    
            except FileNotFoundError as e:
                print("An error has occurred. Please check if the main file is in this directory.")
                print("This error has occurred:", e)
        elif i.lower() == "n":
            print("This needs to be accepted. Killing program. No changes have been made")
            exit()
        else:
            try:
                os.path.isfile("enckey.key")
                os.path.isfile(encfile)
                decrypt()
            except FileNotFoundError as e:
                print("[ERROR]Failed file test please make sure your files are named corectly and are in this directory. See README for more info. You could also have a broken enc key see readme for more info")
                exit()
print("Welcome to eCrypt", version)
print("© Caiden Pinter 2025 | Majix Co. 2025")
i = input("What file do you want to use (Give full path) ex. /home/user/Downloads/example.txt")
print("Okay, This file will be prepared for encryption")
print("Checking if path is valid")
isexist = os.path.exists(i)
if isexist == True:
    print("Your path is valid calling encrypt function")
    print("Stating File structure")
    encfile = i
    print("Calling check")
    enccheck()
elif isexist == False:
    print("That file path is invalid or does not exist please try again")
        
        
