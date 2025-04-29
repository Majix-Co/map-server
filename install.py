def licensedec():
    i = "y"
    if i == "y":
        print("\nDecrypting 1/2")
        with open('licensekey.key', 'rb') as filekey:
            key = filekey.read()
            fernet = Fernet(key)
            with open('projectkey.key', 'rb') as enc_file:
                encrypted = enc_file.read()
                decrypted = fernet.decrypt(encrypted)
                with open('projectkey.key', 'wb') as dec_file:
                    dec_file.write(decrypted)
                    #print("\nMaking backup of old key")
                    #f = open('ecryptinkey.key', 'r')
                    #open('encbackup.key', 'x')
                    #v = open('encbackup.key', 'w')
                    #v.write(f.read())
                    #print("\nBackup created")
                    i = "n"
                    if i == "y":
                        os.remove('enckey.key')
                        print("Thank you for using eCrypt")
                        exit()
                    elif i == "n":
                        #filekey.close()
                        #f.close()
                        #v.close()
                        enc_file.close()
                        dec_file.close()
                        os.remove('ecryptinkey.key')
                        os.remove('encbackup.key')
                        print("Fully decrypted file")
                        return
def install():
    if str(contentver) == str(version):
        if installpak == "basicTools":
            print('Using majixpak', installpak)
            i = input("Hello!, Would you like to start the install? (y/n)")
            if i == "y":
                try:
                    os.mkdir("eCrypt-Installer")
                    print("Okay will get full package")
                    platformcheck = os.name
                    if platformcheck == "posix":
                        shutil.move(finalsource,"eCrypt-Installer")
                        print("\nSystem Deteced as Posfix (Unix Based System)\n")
                        os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/posfixinstall.sh -o posfixinstall.sh')
                        os.system('chmod +x posfixinstall.sh')
                        os.system('./posfixinstall.sh')
                        exit()
                    elif platformcheck == "nt":
                        shutil.move(finalsource,"eCrypt-Installer")
                        print("NT DETECTED")
                        move2 = source + "/" + "tempfile.txt"
                        if os.path.isfile(move2):
                            shutil.copy(move2,"eCrypt-Installer")
                            print("Windows support is still beta and may have some issues")
                            print("Please report any on the issue page on github")
                            os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/ntscript/posfixinstall.py -o posfixinstall.py')
                            os.system('python3 posfixinstall.py')
                        else:
                            x = open('tempfile.txt', 'x')
                            x.write(os.getcwd())
                            x.close()
                            shutil.copy(move2,"eCrypt-Installer")
                            print("Windows support is still beta and may have some issues")
                            print("Please report any on the issue page on github")
                            os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/ntscript/posfixinstall.py -o posfixinstall.py')
                            os.system('python3 posfixinstall.py')
                    else:
                        print("This script is not compatible with your OS (yet)")
                except FileExistsError:
                    platformcheck = os.name
                    if platformcheck == "posix":
                        print("Partial Install Detected")
                        print("Removing old files please re-run this script")
                        os.system('rm -rf eCrypt-Installer')
                        os.system('rm -rf posfixinstall.py')
                        print("Cleaned up")
                        exit()
                    elif platformcheck == "nt":
                        print("Partial Install Detected")
                        print("Removing old files please re-run this script")
                        os.system('rmdir /s /q eCrypt-Installer')
                        os.remove('posfixinstall.py')
                        print("\nCleaned up")
                        exit()
            elif i == "n":
                print("Whoops!, Minimal Install Not supported")
                exit()                  
        elif installpak == "basicTools-Offline":
            print("The Update Server is not enabled here")
            print('Using majixpak', installpak)
            print("Hello!, Before installing we need to test if you have the required packages")
            check1 = ["curl", "--help"]
            try:
                print("\n[DISCLAMER] If building the installer you MUST run this script with sudo or a admin user\n")
                #subprocess.run(check1, check = True, stdout=subprocess.DEVNULL)
                i = input("Hello!, Are you sure you would like to build the installer? (y[Default]/n) ")
                if i == "y":
                    try:
                        print("Okay will get full package")
                        platformcheck = os.name
                        if platformcheck == "posix":
                            print("\nSystem Deteced as Posfix (Unix Based System)\n")
                            #icheck = findtext.filecheck('majix.conf', 'Active12')
                            try:
                                open('majix.conf', 'r')
                                os.system('chmod +x posfixinstall.sh')
                                os.system('./posfixinstall.sh')
                                exit()
                            except:
                                source = os.getcwd()
                                os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/posfixinstall.sh -o posfixinstall.sh')
                                source2 = os.path.basename(__file__)
                                finalsource = source + "/" + source2
                                os.mkdir("eCrypt-Installer")
                                shutil.move(finalsource,"eCrypt-Installer")
                                print("Okay will get full package")
                                open('majix.conf', 'x')
                                configfile = open('majix.conf', 'w')
                                configfile.writelines(
'''
Majix Installer LiveConfig File
Offline-Installer Config
Install Mode:
Active12
# Modify Above Line to Active to re generate
'''
                                    )
                                configfile.close()
                                source = os.getcwd()
                                source2 = 'majix.conf'
                                finalsource = source + "/" + source2
                                shutil.move(finalsource,"eCrypt-Installer")
                                os.system('chmod +x posfixinstall.sh')
                                os.system('./posfixinstall.sh')
                                exit()
                        elif platformcheck == "nt":
                            #shutil.move(finalsource,"eCrypt-Installer")
                            #print("NT DETECTED")
                            #move2 = source + "/" + "tempfile.txt"
                            #if os.path.isfile(move2):
                                #shutil.copy(move2,"eCrypt-Installer")
                                #print("Windows support is still beta and may have some issues")
                                #print("Please report any on the issue page on github")
                                #os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/ntscript/posfixinstall.py -o posfixinstall.py')
                                #os.system('python3 posfixinstall.py')
                            #else:
                                #x = open('tempfile.txt', 'x')
                                #x.write(os.getcwd())
                                #x.close()
                                #shutil.copy(move2,"eCrypt-Installer")
                                #print("Windows support is still beta and may have some issues")
                                #print("Please report any on the issue page on github")
                                #os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/ntscript/posfixinstall.py -o posfixinstall.py')
                                #os.system('python3 posfixinstall.py')
                                print("Whoops!, Looks like this pak does not have NT Support")
                        else:
                            print("This script is not compatible with your OS (yet)")
                    except FileExistsError:
                        platformcheck = os.name
                        if platformcheck == "posix":
                            print("Partial Install Detected")
                            print("Removing old files please re-run this script")
                            os.system('rm -rf eCrypt-Installer')
                            os.system('rm -rf posfixinstall.py')
                            print("Cleaned up")
                            exit()
                        elif platformcheck == "nt":
                            print("Partial Install Detected")
                            print("Removing old files please re-run this script")
                            os.system('rmdir /s /q eCrypt-Installer')
                            os.remove('posfixinstall.py')
                            print("\nCleaned up")
                            exit()
                elif i == "n":
                    print("Whoops!, Minimal install is not currently supported please use full install")
                    exit()
            except Exception as e:
                print("Please install ""Curl"" Before attempting to build the installer")  
                print(e)
                exit()      
    elif str(contentver) > str(version):
        print("Looks like there is a update avaible here is some of the things that have changed\n")
        #print(content[12].replace('"','').strip())
        #print(content[13].replace('"','').strip())
        #print(content[14].replace('"','').strip())
        print("\nA update file has been added to the current working directory rember to delete this version before updating")
        os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/install.py -o update.py')
        exit()
def encrypt3():    
    i = "y"
    if i == "y":
        # Generate a key and save it
        key = Fernet.generate_key()
        with open('licensekey.key', 'wb') as filekey:
            filekey.write(key)
    # specify type and use that UNLESS you are using a varibal
        # Read the key from the file
        with open('licensekey.key', 'rb') as filekey:
            key = filekey.read()

        # Read the file to be encrypted
        with open('projectkey.key', 'rb') as file:
            original = file.read()

    # Create a Fernet cipher suite and encrypt the data
        cipher_suite = Fernet(key)
        encrypted = cipher_suite.encrypt(original)

        # Write the encrypted data back to the file
        with open('projectkey.key', 'wb') as encrypted_file:
            encrypted_file.write(encrypted)
            print("Encrypted!")
            return
import os
import shutil
import datetime
import subprocess
from cryptography.fernet import Fernet
os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/findtext.py -o findtext.py')
import findtext
source = os.getcwd()
source2 = os.path.basename(__file__)
finalsource = source + "/" + source2
year = str(datetime.datetime.now().year)
version = 4.4
offlinekiosk = 0
print("Majix Installer", version)
print("© Majix Co. " + year)
#open("temp.sh", 'x')
print("Preparing Installer")
print("Current Directory")
print(source)
# Install software type 
print("\nWarning! The offline-installer requires following of instructions listed on github page if you are doing automated install choose basictools\n")
print("\n[INFO] For automated install press enter\n")
if offlinekiosk == 0:
    i = input("This version of Majix Installer has 2 packs which would you like to use? basictools[default]/offline: ")
    if i == "offline":
        installpak = "basicTools-Offline"
        contentver = str(version)
        print("Update Bypass ran starting main install")
        install()
    else:
        # For others forking this project if all else fails use "basicTools"
        installpak = "basicTools"
        # End of pak set
        print("Getting needed files")
        os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/updateserv.muf -o temp.txt')
        file = open('temp.txt')
        print("Removed temp file")
        content = file.readlines()
        contentver = content[3].replace('"','').strip()
        file.close()
        os.remove('temp.txt')
        # contentver = str(version)
        install()
elif offlinekiosk == 1:
    try:
        licensedec()
        key = open('projectkey.key', 'r')
        lines = key.readlines()
        datecheck = key[4].strip()
        date = str(datetime.datetime.now().year())
        if datecheck == date:
            #print("Please enter the majix OTP for today")
            installpak = "basicTools-Offline"
            contentver = str(version)
            print("Update Bypass ran starting main install")
            encrypt3()
            install()
        else:
            print("Your license has expired please redownload the most recent one")
    except:
        print("Since this is a offline install to prove this is the correct installer please download and add 'projectkey.key' and enter the pin within")
        exit()


