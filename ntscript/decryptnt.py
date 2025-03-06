import cryptography
from cryptography.fernet import Fernet
import os
import time
mainvar = open('tempfile.txt', 'r')
tempvar = mainvar.read().strip()
mainvar.close()
dir = os.getcwd() + "\\" + "eCrypt-Installer" + "\\"
print("\nMajix Installer")
print("\n4/5 | Decrypting files")
def decrypt2():
    i = "y"
    if i == "y":
        print("\nDecrypting 2/2")
        with open(dir + "password3key.key", 'rb') as filekey:
            key = filekey.read()
            fernet = Fernet(key)
            with open(dir + "passwordgen3.py", 'rb') as enc_file:
                encrypted = enc_file.read()
                decrypted = fernet.decrypt(encrypted)
                with open(dir + "passwordgen3.py", 'wb') as dec_file:
                    dec_file.write(decrypted)
                    #print("\nMaking backup of old key")
                    f = open(dir + "password3key.key", 'r')
                    open(dir + "encbackup.key", 'x')
                    v = open(dir + "encbackup.key", 'w')
                    v.write(f.read())
                    time.sleep(3)
                    #print("\nBackup created")
                    i = "n"
                    if i == "y":
                        os.remove(dir + "enckey.key")
                        print("Thank you for using eCrypt")
                        exit()
                    elif i == "n":
                        os.remove(dir + "password3key.key")
                        os.remove(dir + "encbackup.key")
                        #print("Thank you for using eCrypt")
                        run = "python3" + " " + dir + "\\" + "cleanup.py"
                        os.system(run)
                        exit()
                        
    # END OF DECRYPT CODE
    elif i == "n":
        print("Will not decrypt file killing current process")
        exit()
def decrypt1():
    i = "y"
    if i == "y":
        print("\nDecrypting 1/2")
        with open(dir + "ecryptinkey.key", 'rb') as filekey:
            key = filekey.read()
            fernet = Fernet(key)
            with open(dir + "eCrypt4.1.py", 'rb') as enc_file:
                encrypted = enc_file.read()
                decrypted = fernet.decrypt(encrypted)
                with open(dir + "eCrypt4.1.py", 'wb') as dec_file:
                    dec_file.write(decrypted)
                    #print("\nMaking backup of old key")
                    f = open(dir + "ecryptinkey.key", 'r')
                    open(dir + "encbackup.key", 'x')
                    v = open(dir + "encbackup.key", 'w')
                    v.write(f.read())
                    time.sleep(3)
                    #print("\nBackup created")
                    i = "n"
                    if i == "y":
                        os.remove(dir + "enckey.key")
                        print("Thank you for using eCrypt")
                        exit()
                    elif i == "n":
                        os.remove(dir + "ecryptinkey.key")
                        os.remove(dir + "encbackup.key")
                        print("Fully decrypted file")
                        decrypt2()
    # END OF DECRYPT CODE
    elif i == "n":
        print("Will not decrypt file killing current process")
        exit()
decrypt1()
