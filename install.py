import os
import shutil
source = os.getcwd()
source2 = os.path.basename(__file__)
finalsource = source + "/" + source2
print("eCrypt Installer 3")
print("© Majix Co.")
#open("temp.sh", 'x')
print("Preparing Installer")
print(source)
print("Getting needed files")
i = input("Hello!, Would you like to full package or just the minimal packages? (f/m): ")
if i == "f":
    try:
        os.mkdir("eCrypt-Installer")
        print("Okay will get full package")
        platformcheck = os.name
        if platformcheck == "posix":
            shutil.move(finalsource,"eCrypt-Installer")
            os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/posfixinstall.sh -o posfixinstall.sh')
            os.system('chmod +x posfixinstall.sh')
            os.system('./posfixinstall.sh')
            exit()
        elif platformcheck == "nt":
            print("NT DETECTED")
            print("Windows support is being worked on currently")
            print("It is expected to be released eventually")
            # Get windows script
        else:
            print("This script is not compatible with your OS")
    except FileExistsError:
        print("Partial Install Detected")
        print("Removing old files please re-download this script")
        os.remove(__file__)
        os.rmdir("eCrypt-Installer")
        print("Cleaned up")
        exit()
elif i == "x":
    print("Whoops!, Minimal install is not currently supported please use full install")
    exit()                  


