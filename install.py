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
                subprocess.run(check1, check = True, stdout=subprocess.DEVNULL)
                i = input(i = input("Hello!, Are you sure you would like to build the installer? (y[Default]/n) "))
                if i == "y":
                    try:
                        os.mkdir("eCrypt-Installer")
                        print("Okay will get full package")
                        platformcheck = os.name
                        if platformcheck == "posix":
                            shutil.move(finalsource,"eCrypt-Installer")
                            print("\nSystem Deteced as Posfix (Unix Based System)\n")
                            #os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/posfixinstall.sh -o posfixinstall.sh')
                            try:
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
                            except:
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
            except:
                print("Please install ""Curl"" Before attempting to build the installer")  
                exit()      
    elif str(contentver) > str(version):
        print("Looks like there is a update avaible here is some of the things that have changed\n")
        #print(content[12].replace('"','').strip())
        #print(content[13].replace('"','').strip())
        #print(content[14].replace('"','').strip())
        print("\nA update file has been added to the current working directory rember to delete this version before updating")
        os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/install.py -o update.py')
        exit()
import os
import shutil
import datetime
import subprocess
os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/findtext.py -o findtext.py')
import findtext
source = os.getcwd()
source2 = os.path.basename(__file__)
finalsource = source + "/" + source2
year = str(datetime.datetime.now().year)
version = 4.4
print("Majix Installer", version)
print("© Majix Co. " + year)
#open("temp.sh", 'x')
print("Preparing Installer")
print("Current Directory")
print(source)
# Install software type 
print("\nWarning! The offline-installer requires following of instructions listed on github page if you are doing automated install choose basictools\n")
print("\n[INFO] For automated install press enter\n")
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
   


