import os
import shutil
import time
import sys
import findtext
from cryptography.fernet import Fernet
print('Adding Pernament modifications to cleanup.py')
findtext.filereplace('cleanup.py',"os.remove('decrypt.py')", '#', '1/10')
findtext.filereplace('cleanup.py',"os.remove('eCryptcm.py')", '#', '2/10')
findtext.filereplace('cleanup.py',"os.remove('install.py')", '#', '3/10')
findtext.filereplace('cleanup.py',"os.remove('license.txt')", '#', '4/10')
findtext.filereplace('cleanup.py',"os.remove('passwordgencm.py')", '#', '5/10')
findtext.filereplace('cleanup.py',"os.remove('posfixinstall2.py')", '#', '6/10')
findtext.filereplace('cleanup.py',"os.remove('postfixinstall3.sh')", '#', '7/10')
findtext.filereplace('cleanup.py',"os.remove('cleanup.py')", '#', '8/10')
findtext.filereplace('cleanup.py',"os.remove('findtext.py')", '#', '9/10')
findtext.filereplace('cleanup.py',"os.remove('licensecompare.txt')", '#', '10/10')
findtext.filereplace('eCrypt4.4.py','updateskip = 0', 'updateskip = 1', 'Done')
findtext.filereplace('cleanup.py',"os.remove('eCrypt4.4.py')", '#', 'Done')
findtext.filereplace('install.py','offlinekiosk = 0', 'offlinekiosk = 1', 'Done')
os.remove('cleanup.sh')
open('cleanup.sh', 'x')
cleanupsh = open('cleanup.sh', 'w')
cleanupsh.writelines(
''''
#! /bin/bash
cd ..
# rm -f posfixinstall.sh
# rm -f findtext.py
# rm -f cleanup.sh
# rm -rf eCrypt-Installer
'''
)
cleanupsh.close()
def final():
    findtext.filereplace('majix.conf', 'Active12', 'Finished', 'Okay to use installer | Thank you for using majix!')
    #findtext.filereplace('install.py', 'offlinekiosk = 0', 'offlinekiosk = 1', 'Done')
    #os.system('sudo pkill python')
    #findtext.filereplace('install.py', '                            if 1 == 1:', '                            if 1 == 2:', 'Cancel second run')
    exit()
def encrypt2():    
    i = "y"
    if i == "y":
        # Generate a key and save it
        key = Fernet.generate_key()
        with open('ecryptinkey.key', 'wb') as filekey:
            filekey.write(key)
    # specify type and use that UNLESS you are using a varibal
        # Read the key from the file
        with open('ecryptinkey.key', 'rb') as filekey:
            key = filekey.read()

        # Read the file to be encrypted
        with open('eCrypt4.4.py', 'rb') as file:
            original = file.read()

    # Create a Fernet cipher suite and encrypt the data
        cipher_suite = Fernet(key)
        encrypted = cipher_suite.encrypt(original)

        # Write the encrypted data back to the file
        with open('eCrypt4.4.py', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            os.remove('eCryptcm.py')
            open('eCryptcm.py', 'x')
            passwordoutput = open('eCryptcm.py', 'w')
            with open('eCrypt4.4.py', 'r') as passinput:
                passwordoutput.write(passinput.read())
            passwordoutput.close()
            passinput.close()
            print("Encrypted!")
            final()
            exit()
    elif i == "n":
        print("Okay, No changes were made. Quiting Program")
        exit()
def encrypt():    
    i = "y"
    if i == "y":
        # Generate a key and save it
        key = Fernet.generate_key()
        with open('password3key.key', 'wb') as filekey:
            filekey.write(key)
    # specify type and use that UNLESS you are using a varibal
        # Read the key from the file
        with open('password3key.key', 'rb') as filekey:
            key = filekey.read()

        # Read the file to be encrypted
        with open('passwordgen3.py', 'rb') as file:
            original = file.read()

    # Create a Fernet cipher suite and encrypt the data
        cipher_suite = Fernet(key)
        encrypted = cipher_suite.encrypt(original)

        # Write the encrypted data back to the file
        with open('passwordgen3.py', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            print("Encrypted!")
            os.remove('passwordgencm.py')
            open('passwordgencm.py', 'x')
            passwordoutput = open('passwordgencm.py', 'w')
            with open('passwordgen3.py', 'r') as passinput:
                passwordoutput.write(passinput.read())
            passwordoutput.close()
            passinput.close()
            encrypt2()
            exit()
    elif i == "n":
        print("Okay, No changes were made. Quiting Program")
        exit()
version = 'Unknown'
print("Welcome to eCrypt", version)
print("Majix Co. 2025")
i = "y"
if i == "y":
    try:
        os.path.isfile("passwordgen3.py")
        print('Adding bypass flags')
    
    except Exception as e:
        print("An error has occurred. Please check if the main file is in this directory.")
        print("This error has occurred:", e)
elif i == "n":
    print("This needs to be accepted. Killing program. No changes have been made")
    exit()
else:
   try:
       os.path.isfile("enckey.key")
       os.path.isfile("passwordgen.py")
   except Exception as e:
       print("[ERROR]Failed file test please make sure your files are named corectly and are in this directory. See README for more info. You could also have a broken enc key see readme for more info")
       exit()
