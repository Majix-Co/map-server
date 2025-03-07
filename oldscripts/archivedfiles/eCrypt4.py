import cryptography
from cryptography.fernet import Fernet
import os
import time
import shutil
source = os.getcwd()
version = "4.1"
print("[WARN] This script uses the OS module")
print("\nWill create new working directory to add files\n")
dest = "eCrypt-Working-Directory"
if "eCrypt-Working-Directory" in source:
        print("Directory is valid Okay to start script")
else:
    print("hi")
    os.mkdir("eCrypt-Working-Directory")
    shutil.move('eCrypt4.py',dest)


def ecryptstart():
    dest = os.getcwd()
    print("Welcome to eCrypt", version)
    print("© Caiden Pinter 2025 | Majix Co. 2025")
    i = input("What file do you want to use (Give full path) ex. /home/user/Downloads/example.txt")
    print("Copying file to current working directory")
    shutil.copy(i,dest)
    print("File was copyed")
    dir = os.listdir()
    print(dir)
    print("Does your file exist?")
    if i == "y":
        i = input("What is the name of the file as seen above?")
        encfile = i

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