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
            # Insert curl link
            os.system('chmod +x posfixinstall.sh')
        elif platformcheck == "nt":
            print("NT DETECTED")
            # Get windows script
        else:
            print("This script is not compatible with your OS")
    except FileExistsError:
        print("Directory Already exist")
        print("Script was already ran cleaning up")
        os.remove(__file__)
        os.rmdir("eCrypt-Installer")
        print("Cleaned up")
        exit()
                  


