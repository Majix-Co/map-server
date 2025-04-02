import filecmp
import time
import os
import shutil
rmdir = os.getcwd() + "\\" + "eCrypt-Installer"
print("\nMajix Installer")
print("\n2/5 | Comparing files to web versions\n")
time.sleep(2)
dir = os.getcwd() + "\\" + "eCrypt-Installer"
dir3 = dir = os.getcwd() + "\\" + "eCrypt-Installer" + "\\"
source3 = dir.strip() + "\\" + "license.txt"
source = dir + "\\" + "eCryptcm.py"
scheck1 = dir + "\\" + "eCrypt4.4.py"
license = open(source3, 'r')
def start():
    dir = os.getcwd() + "\\" + "eCrypt-Installer"
    source = dir + "\\" + "eCryptcm.py"
    scheck1 = dir + "\\" + "eCrypt4.4.py"
    i = input("Do you agree to the license agreement (yes/no[default]): ")
    if i == "yes":
        print("Checking values")
        filecheck = filecmp.cmp(source,scheck1)
        if filecheck == True:
            print("\nOkay File looks okay")
            source = dir + "\\" + "passwordgencm.py"
            scheck1 = dir + "\\" + "passwordgen3.py"
            filecheck2 = filecmp.cmp(source,scheck1)
            if filecheck2 == True:
                print("All checks Passed!")
                print("Preparing next check")
                run = "python3" + " " + dir + "\\" + "postfixinstall3.py"
                os.system(run)
                exit()
            elif filecheck2 == False:
                print("Looks like the file is not right")
                exit()
        elif filecheck == False:
            print("File may have been tampered with they do not match killing script")
            print("This will leave a partial install please clear this directory and rerun the script OR rerun the install.py script in the same diredctory it was originaly in to clear this directory")
            print("\nAuto cleaning up directory\n")
            os.remove(dir3 + 'decrypt.py')
            os.remove(dir3 + 'eCryptcm.py')
            os.remove(dir3 + 'install.py')
            os.remove(dir3 + 'passwordgencm.py')
            os.remove(dir3 + 'posfixinstall2.py')
            os.remove(dir3 + 'postfixinstall3.py')
            os.remove(dir3 + 'cleanup.py')
            os.remove(dir3 + 'license.txt')
            shutil.rmtree(rmdir)
            exit() 
    else:
        print("Sorry you need to agree to the license to install this program")
        deldir = "rmdir /s /q " + dir
        os.remove(deldir)
        exit()
i = input("Would you like to open the gui license? (yes/no[default])")
if i == "yes":
    notepad = "notepad.exe " + source3
    os.system(notepad)
    license.close()
    start()
else:
    print(license.read())
    license.close()
    start()