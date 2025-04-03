import os
import shutil
import datetime
source = os.getcwd()
source2 = os.path.basename(__file__)
finalsource = source + "/" + source2
# Install software type 
# For others forking this project if all else fails use "basicTools"
installpak = "basicTools"
# End of pak set
year = str(datetime.datetime.now().year)
version = 4.4
print("Majix Installer", version)
print("© Majix Co. " + year)
#open("temp.sh", 'x')
print("Preparing Installer")
print(source)
print("Getting needed files")
os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/updateserv.muf -o temp.txt')
file = open('temp.txt')
print("Removed temp file")
content = file.readlines()
contentver = content[3].replace('"','').strip()
file.close()
os.remove('temp.txt')
if str(contentver) == str(version):
    print('Using majixpak ', installpak)
    i = input("Hello!, Would you like to full package or just the minimal packages? (f/m): ")
    if installpak == "basicTools":
        if i == "f":
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
        elif i == "m":
            print("Whoops!, Minimal install is not currently supported please use full install")
            exit()                  
    else:
        print("Whoops!, Looks like you tried to install a majixPak before the required files exists")
        print("Please specify your pak or simply use the basic one")
elif str(contentver) > str(version):
    print("Looks like there is a update avaible here is some of the things that have changed\n")
    print(content[12].replace('"','').strip())
    print(content[13].replace('"','').strip())
    print(content[14].replace('"','').strip())
    print("\nA update file has been added to the current working directory rember to delete this version before updating")
    os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/install.py -o update.py')
    exit()
   


