import cryptography
from cryptography.fernet import Fernet
import os
import time
def decrypt():
    i = input("Are you sure you would like to decrypt (y/n) ")
    if i == "y":
        print("\n[FileCheck] Starting File check service\n")
        i = input("What is the name of the key (Make sure it is in the same directory as this script)\n[Please include .key in the name]\n: ")
        keycurrent = i
        print("This is the key selceted: ", keycurrent)
        filecheck = os.path.isfile(i) 
        if filecheck == True:
            print("\nThis will decrypt the file and delete the old key a new key will need to be genereated")
            try:
                with open(keycurrent, 'rb') as filekey:
                    key = filekey.read()
                    fernet = Fernet(key)
                    with open(encfile, 'rb') as enc_file:
                        encrypted = enc_file.read()
                        decrypted = fernet.decrypt(encrypted)
                        with open(encfile, 'wb') as dec_file:
                            dec_file.write(decrypted)
                            print("\nMaking backup of old key")
                            f = open(keycurrent, 'r')
                            open('encbackup.key', 'x')
                            v = open('encbackup.key', 'w')
                            v.write(f.read())
                            time.sleep(3)
                            print("\nBackup created")
                            i = input("\nWould you like to keep the backup? [If you change the file the old key will be invalid] (y/n): ")
                            if i == "y":
                                os.remove(keycurrent)
                                print("Thank you for using eCrypt")
                                exit()
                            elif i == "n":
                                os.remove(keycurrent)
                                os.remove('encbackup.key')
                                print("Thank you for using eCrypt")
                                exit()
            except ValueError:
                print("\n[ERROR] Your key is not valid or is couropted make sure it is the .key format and is the original copy or correctly formated please try again\n")

        elif filecheck == False:
            print("Sorry that path is not valid please try again")
            exit()
def encrypt():    
    i = input("Are you sure you would like to encrypt? Once encrypted if you lose the key you CAN NOT access the data. See README for more info(y/n): ")
    if i == "y":
        i = input("What would you like to name your key? Only type the name NOT the file extension: ")
        filecheck = i + ".key"
        filecheckfin = os.path.isfile(filecheck)
        if filecheckfin == False:
            name = i
            # Generate a key and save it
            key = Fernet.generate_key()
            with open(name + '.key', 'wb') as filekey:
                filekey.write(key)
        # specify type and use that UNLESS you are using a varibal
            # Read the key from the file
            with open(name + '.key', 'rb') as filekey:
                key = filekey.read()

            # Read the file to be encrypted
            with open(encfile, 'rb') as file:
                original = file.read()

        # Create a Fernet cipher suite and encrypt the data
            cipher_suite = Fernet(key)
            encrypted = cipher_suite.encrypt(original)

            # Write the encrypted data back to the file
            with open(encfile, 'wb') as encrypted_file:
                encrypted_file.write(encrypted)
                print("Encrypted!")
        elif filecheckfin == True:
            print("\n[WARNING] The key name specified already exist using that name would overwrite the file please try another\n")
            encrypt()
    elif i == "n":
        print("Okay, No changes were made. Quiting Program")
        exit()
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
                os.path.isfile(i + '.key')
                os.path.isfile(encfile)
                decrypt()
            except FileNotFoundError as e:
                print("[ERROR]Failed file test please make sure your files are named corectly and are in this directory. See README for more info. You could also have a broken enc key see readme for more info")
                exit()
print("Welcome to eCrypt", version)
print("© Caiden Pinter 2025 | Majix Co. 2025")
i = input("What file do you want to use (Give full path) ex. /home/user/Downloads/example.txt: ")
print("Okay, This file will be prepared for encryption")
print("\nChecking if path is valid\n")
isexist = os.path.exists(i)
if isexist == True:
    print("Your path is valid calling encrypt function")
    print("Stating File structure")
    encfile = i
    print("\nThis file is selected: ", encfile)
    print("\nCalling check")
    enccheck()
elif isexist == False:
    print("That file path is invalid or does not exist please try again")