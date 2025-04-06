import filecmp
import time
import os
import shutil
mainvar = open('tempfile.txt', 'r')
tempvar = mainvar.read().strip()
finalmove = tempvar + "\\" + "install.py"
mainvar.close()
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
            #os.remove(dir3 + 'install.py')
            os.remove(dir3 + 'passwordgencm.py')
            os.remove(dir3 + 'posfixinstall2.py')
            os.remove(dir3 + 'postfixinstall3.py')
            os.remove(dir3 + 'cleanup.py')
            os.remove(dir3 + 'license.txt')
            shutil.move(dir3 + "install.py", finalmove)
            print("The install file was moved back to the directory it was originaly ran on, please rerun the install file")
            print("The file was moved back to ", tempvar, " Under the name ", finalmove)
            print("The directory has been deleted. Will now rerun script")
            print("If you would like to rerun it yourself press Ctrl + C")
            print("5 Seconds till script is auto-ran to cancel press Ctrl + C now")
            time.sleep(5)
            rerun = "python3 " + finalmove
            shutil.rmtree(rmdir)
            exit()
            os.system(rerun)
            shutil.rmtree(rmdir)
            exit()

    else:
        print("Sorry you need to agree to the license to install this program")
        os.remove(dir3 + 'decrypt.py')
        os.remove(dir3 + 'eCryptcm.py')
        #os.remove(dir3 + 'install.py')
        os.remove(dir3 + 'passwordgencm.py')
        os.remove(dir3 + 'posfixinstall2.py')
        os.remove(dir3 + 'postfixinstall3.py')
        os.remove(dir3 + 'cleanup.py')
        os.remove(dir3 + 'license.txt')
        shutil.move(dir3 + "install.py", finalmove)
        print("The install file was moved back to the directory it was originaly ran on, please rerun the install file")
        print("The file was moved back to ", tempvar, " Under the name ", finalmove)
        print("The directory has been deleted. Will now rerun script")
        print("If you would like to rerun it yourself press Ctrl + C")
        print("5 Seconds till script is auto-ran to cancel press Ctrl + C now")
        time.sleep(5)
        rerun = "python3 " + finalmove
        shutil.rmtree(rmdir)
        os.system(rerun)
        exit()
i = input("Would you like to open the gui license? (yes/no[default]): ")
if i == "yes":
    notepad = "notepad.exe " + source3
    os.system(notepad)
    license.close()
    start()
else:
    print(license.read())
    license.close()
    start()