import cryptography
from cryptography.fernet import Fernet
import os
import time
version = "4.1ES"
print("[WARN] This script uses the OS module")
# To run encrypt module run encrypt() to run decrypt run decrypt()
# when opening a file make use "w" for writable 'X' for create 'r' for read only 'b' for enc
def encrypt():    
    i = input("Are you sure you would like to encrypt? Once encrypted if you lose the key you CAN NOT access the data. See README for more info(y/n): ")
    if i == "y":
        # Generate a key and save it
        key = Fernet.generate_key()
        with open('enckey.key', 'wb') as filekey:
            filekey.write(key)
    # specify type and use that UNLESS you are using a varibal
        # Read the key from the file
        with open('enckey.key', 'rb') as filekey:
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
    elif i == "n":
        print("Okay, No changes were made. Quiting Program")
        exit()
# Define of decrypt
def decrypt():
    i = input("Are you sure you would like to decrypt (y/n) ")
    if i == "y":
        print("\nThis will decrypt the file and delete the old key a new key will need to be genereated")
        with open('enckey.key', 'rb') as filekey:
            key = filekey.read()
            fernet = Fernet(key)
            with open('passwordgen3.py', 'rb') as enc_file:
                encrypted = enc_file.read()
                decrypted = fernet.decrypt(encrypted)
                with open('passwordgen3.py', 'wb') as dec_file:
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
    # END OF DECRYPT CODE
    elif i == "n":
        print("Will not decrypt file killing current process")
        exit()
print("Welcome to eCrypt", version)
print("© Caiden Pinter 2025 | Majix Co. 2025")

i = input("Do you agree to allow this program to access the required files? (y[encrypt]/n/decrypt): ")
if i == "y":
    try:
        os.path.isfile("passwordgen3.py")
        encrypt()
    
    except Exception as e:
        print("An error has occurred. Please check if the main file is in this directory.")
        print("This error has occurred:", e)
elif i.lower() == "n":
    print("This needs to be accepted. Killing program. No changes have been made")
    exit()
else:
   try:
       os.path.isfile("enckey.key")
       os.path.isfile("passwordgen.py")
       decrypt()
   except Exception as e:
       print("[ERROR]Failed file test please make sure your files are named corectly and are in this directory. See README for more info. You could also have a broken enc key see readme for more info")
       exit()
