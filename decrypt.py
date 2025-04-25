import cryptography
from cryptography.fernet import Fernet
import os
import time
print("\nMajix Installer")
print("\n4/5 | Decrypting files")
def decrypt2():
    i = "y"
    if i == "y":
        print("\nDecrypting 2/2")
        with open('password3key.key', 'rb') as filekey:
            key = filekey.read()
            fernet = Fernet(key)
            with open('passwordgen3.py', 'rb') as enc_file:
                encrypted = enc_file.read()
                decrypted = fernet.decrypt(encrypted)
                with open('passwordgen3.py', 'wb') as dec_file:
                    dec_file.write(decrypted)
                    #print("\nMaking backup of old key")
                    f = open('password3key.key', 'r')
                    open('encbackup.key', 'x')
                    v = open('encbackup.key', 'w')
                    v.write(f.read())
                    time.sleep(3)
                    #print("\nBackup created")
                    i = "n"
                    if i == "y":
                        os.remove('enckey.key')
                        print("Thank you for using eCrypt")
                        exit()
                    elif i == "n":
                        #print("Thank you for using eCrypt")
                        installconfig = open('majix.conf', 'r')
                        iconfig = installconfig.readlines()
                        icheck = iconfig[4].strip()
                        try:
                            if icheck == 'Active12':
                                print("All checks Passed!")
                                print("Preparing next check")
                                os.system('chmod +x postfixinstall3.sh')
                                os.system('./postfixinstall3.sh')
                                os.remove('postfixinstall3.sh')
                                print('Modifying file')
                                open('postfixinstall3.sh', 'x')
                                postfixinstall3 = open('postfixinstall3.sh', 'w')
                                postfixinstall3.writelines(
                                '''
                                #! /bin/bash
                                echo ////////////////////////////////////////////[Majix Installer]//////////////////////////////////////////
                                echo \n3/5 | Preparing for Decryption
                                # curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/ecryptinkey.key -o ecryptinkey.key
                                # curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/password3key.key -o password3key.key
                                sleep 5
                                echo \nAlright!, Files were downloaded sucsefully running python code
                                python3 decrypt.py
                                '''
                                )
                                postfixinstall3.close()
                                os.system('chmod +x postfixinstall3.sh')
                                os.system('python3 cleanup.py')
                                exit()
                            else:
                                filekey.close()
                                dec_file.close()
                                f.close()
                                v.close()
                                enc_file.close()
                                os.remove('password3key.key')
                                os.remove('encbackup.key')
                                #print("Thank you for using eCrypt")
                                os.system('python3 pathfinsh.py')
                                exit()
                        except:
                            filekey.close()
                            dec_file.close()
                            f.close()
                            v.close()
                            enc_file.close()
                            os.remove('password3key.key')
                            os.remove('encbackup.key')
                            #print("Thank you for using eCrypt")
                            os.system('python3 cleanup.py')
                            exit()
                        
    # END OF DECRYPT CODE
    elif i == "n":
        print("Will not decrypt file killing current process")
        exit()
def decrypt1():
    i = "y"
    if i == "y":
        print("\nDecrypting 1/2")
        with open('ecryptinkey.key', 'rb') as filekey:
            key = filekey.read()
            fernet = Fernet(key)
            with open('eCrypt4.4.py', 'rb') as enc_file:
                encrypted = enc_file.read()
                decrypted = fernet.decrypt(encrypted)
                with open('eCrypt4.4.py', 'wb') as dec_file:
                    dec_file.write(decrypted)
                    #print("\nMaking backup of old key")
                    f = open('ecryptinkey.key', 'r')
                    open('encbackup.key', 'x')
                    v = open('encbackup.key', 'w')
                    v.write(f.read())
                    time.sleep(3)
                    #print("\nBackup created")
                    i = "n"
                    if i == "y":
                        os.remove('enckey.key')
                        print("Thank you for using eCrypt")
                        exit()
                    elif i == "n":
                        filekey.close()
                        f.close()
                        v.close()
                        enc_file.close()
                        dec_file.close()
                        os.remove('ecryptinkey.key')
                        os.remove('encbackup.key')
                        print("Fully decrypted file")
                        decrypt2()
    # END OF DECRYPT CODE
    elif i == "n":
        print("Will not decrypt file killing current process")
        exit()
decrypt1()
