import cryptography
from cryptography.fernet import Fernet
import os
import time
from datetime import datetime
year = datetime.now().year
updateskip = 0
# START OF DECRYPT SCRIPT #
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
                                try:
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
                                except:
                                        print("\nWhoops!, Look like you already have a backup in this directory. Could not auto make a backup but key was saved\n")
                                        print("Thank you for using eCrypt!")
                                        exit()
                except IsADirectoryError:
                    print("\nWhoops! Looks like the path you gave is a directory please point to a file or double check your path\n")
                    exit()
                except PermissionError:
                    print("\nWhoops! Looks like the file can't be written to make sure it is not in a system protected directory and can be written to without sudo if that does not work run this script with the sudo command\n")
            except ValueError:
                print("\n[ERROR] Your key is not valid or is couropted make sure it is the .key format and is the original copy or correctly formated please try again\n")
                exit()


        elif filecheck == False:
            print("Sorry that path is not valid please try again")
            exit()
# END OF DECRYPT #
# START OF ENCRYPT #
def encrypt():    
    i = input("Are you sure you would like to encrypt? Once encrypted if you lose the key you CAN NOT access the data. See README for more info(y/n): ")
    if i == "y":
            try:
                i = input("What would you like to name your key? Only type the name NOT the file extension: ")
                filecheck = i + ".key"
                filecheckfin = os.path.isfile(filecheck)
                name = i
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
                        exit()
                elif filecheckfin == True:
                    print("\n[WARNING] The key name specified already exist using that name would overwrite the file please try another\n")
                    print("\n[BE ALERT!] This script auto deletes the key IF used to decrypt your file.\nMeaning this key could be ACTIVE it is recommended to just move the key instead of formating\n")
                    i = input("Format Key? (Will allow you to use that name) (y/n): ")
                    if i == "y":
                        print("\nWill be formating the file: ", name + '.key')
                        i = input("\nThis will FORMAT your key you can NOT recover the key. Are you sure? (y/n)")
                        if i == "y":
                            print("Formating key")
                            os.remove(name + '.key')
                            print("\nKey Formated restarting script\n")
                            encrypt()
                        elif i == "n":
                            print("Ending Program no chanegs made")
                            exit()
                    elif i == "n":
                        print("Ending Program No changes made")
                        exit()
                    encrypt()
            except PermissionError:
                print("\nWhoops! Looks like that file cant be accesed please check the file is not in a write protected directory if that does not work try running the script with sudo or putting it in the current working directory\n")
                exit()
            except IsADirectoryError:
                print("\nWhoops! Looks like the path you gave is a directory please point to a file or double check your path\n")
                os.remove(name + '.key')
                exit()
    elif i == "n":
        print("Okay, No changes were made. Quiting Program")
        exit()
# END OF ENCRYPT SCRIPT #
source = os.getcwd()
version = 4.4
print("[WARN] This script uses the OS module")
#print("\nWill create new working directory to add files\n")
def enccheck():
        print("\nFunction was successfully called!")
        #print("\nKey will be made by user discression")
        i = input("\nDo you agree to allow this program to access the required files? (y[encrypt]/n/decrypt): ")
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
        elif i == "decrypt":
            try:
                os.path.isfile(i + '.key')
                os.path.isfile(encfile)
                decrypt()
            except FileNotFoundError as e:
                print("[ERROR]Failed file test please make sure your files are named corectly and are in this directory. See README for more info. You could also have a broken enc key see readme for more info")
                exit()
        else:
            print("That option is not a option please try again")
            exit()


dir = os.getcwd()
source = dir + "/" + "ufc.muf"
os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/updateserv.muf -o temp.txt')
file = open('temp.txt')
#print("Removed temp file")
content = file.readlines()
contentver = content[3].replace('"','').strip()
if updateskip == 0:
    if str(contentver) == str(version):
        file.close()
        os.remove('temp.txt')
        print("Welcome to eCrypt", version)
        print("Majix Co.", year)
        i = input("What file do you want to use?\nexample (/home/user/Downloads/example.txt) or if in same directory as script (example.txt): ")
        print("Okay, This file will be prepared for encryption")
        print("\nChecking if path is valid\n")
        doesexist = os.path.exists(i)
        if doesexist == True:
            print("\nYour path is valid calling encrypt function")
            print("\nStating File structure")
            encfile = i
            print("\nThis file is selected: ", encfile)
            print("\nCalling check")
            enccheck()
        elif doesexist == False:
            print("That file path is invalid or does not exist please try again")
            exit()
    elif str(contentver) > str(version):
        print("Looks like there is a update avaible here is some of the things that have changed\n")
        print(content[12].replace('"','').strip())
        print(content[13].replace('"','').strip())
        print(content[14].replace('"','').strip())
        print(content[15].replace('"','').strip())
        print(content[15].replace('"','').strip())
        print("\nA update file has been added to the current working directory rember to delete this version before updating")
        os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/eCrypt4.4.py -o update.py')
        file.close()
        os.remove('temp.txt')
        exit()
    else:
        contentver = version
        if str(contentver) == str(version):
            print("\nThe current Majix Update File is broken on server level falling back")
            print("This is NOT a client side issue")
            file.close()
            os.remove('temp.txt')
            print("Welcome to eCrypt", version)
            print("Majix Co.", year)
            i = input("What file do you want to use?\nexample (/home/user/Downloads/example.txt) or if in same directory as script (example.txt): ")
            print("Okay, This file will be prepared for encryption")
            print("\nChecking if path is valid\n")
            doesexist = os.path.exists(i)
            if doesexist == True:
                print("\nYour path is valid calling encrypt function")
                print("\nStating File structure")
                encfile = i
                print("\nThis file is selected: ", encfile)
                print("\nCalling check")
                enccheck()
            elif doesexist == False:
                print("That file path is invalid or does not exist please try again")
                exit()
        else:
            exit()
else:
    print("Welcome to eCrypt", version)
    print("Majix Co.", year)
    i = input("What file do you want to use?\nexample (/home/user/Downloads/example.txt) or if in same directory as script (example.txt): ")
    print("Okay, This file will be prepared for encryption")
    print("\nChecking if path is valid\n")
    doesexist = os.path.exists(i)
    if doesexist == True:
        print("\nYour path is valid calling encrypt function")
        print("\nStating File structure")
        encfile = i
        print("\nThis file is selected: ", encfile)
        print("\nCalling check")
        enccheck()
    elif doesexist == False:
        print("That file path is invalid or does not exist please try again")
        exit()