import cryptography
from cryptography.fernet import Fernet
import os
import time
def decrypt():
    i = input("Are you sure you would like to decrypt (y/n) ")
    if i == "y":
        print("\n[FileCheck] Starting File check service\n")
        i = input("What is the name of the key (Make sure it is in the same directory as this script): ")
        filecheck = os.path.isfile(i) 
        if filecheck == True:
            print("\nThis will decrypt the file and delete the old key a new key will need to be genereated")
            with open('enckey.key', 'rb') as filekey:
                key = filekey.read()
                fernet = Fernet(key)
                with open(encfile, 'rb') as enc_file:
                    encrypted = enc_file.read()
                    decrypted = fernet.decrypt(encrypted)
                    with open(encfile, 'wb') as dec_file:
                        dec_file.write(decrypted)
                        print("\nMaking backup of old key")
                        f = open('enckey.key', 'r')
                        open('encbackup.key', 'x')
                        v = open('encbackup.key', 'w')
                        v.write(f.read())
                        time.sleep(3)
                        print("\nBackup created")
                        i = input("\nWould you like to keep the backup? [If you change the file the old key will be invalid] (y/n): ")
                        if i == "y":
                            os.remove('enckey.key')
                            print("Thank you for using eCrypt")
                            exit()
                        elif i == "n":
                            os.remove('enckey.key')
                            os.remove('encbackup.key')
                            print("Thank you for using eCrypt")
                            exit()
        elif filecheck == False:
            print("Sorry that path is not valid please try again")
def encrypt():    
    i = input("Are you sure you would like to encrypt? Once encrypted if you lose the key you CAN NOT access the data. See README for more info(y/n): ")
    if i == "y":
        i = input("What would you like to name your key? Only type the name NOT the file extension: ")
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
    elif i == "n":
        print("Okay, No changes were made. Quiting Program")
        exit()