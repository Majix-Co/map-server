import filecmp
import time
import os
print("\nMajix Installer")
print("\n2/5 | Comparing files to web versions\n")
time.sleep(2)
dir = os.getcwd()
source3 = dir + "/" + "license.txt"
license = open(source3, 'r')
print("Please ready the license below")
print(license.read())
license.close()
os.remove(source3)
i = input("Do you agree to the license? (yes/no[default])")
if i == "yes":
    source = dir + "/" + "eCryptcm.py"
    scheck1 = dir + "/" + "eCrypt4.4.py"
    print("Checking values")
    filecheck = filecmp.cmp(source,scheck1)
    if filecheck == True:
        print("\nOkay File looks okay")
        source = dir + "/" + "passwordgencm.py"
        scheck1 = dir + "/" + "passwordgen3.py"
        filecheck2 = filecmp.cmp(source,scheck1)
        if filecheck2 == True:
            print("All checks Passed!")
            print("Preparing next check")
            os.system('chmod +x postfixinstall3.sh')
            os.system('./postfixinstall3.sh')
            exit()
        elif filecheck2 == False:
            print("Looks like the file is not right")
            exit()
    elif filecheck == False:
        print("File may have been tampered with they do not match killing script")
        exit()
else:
    print("Whoops!, This program can not install if the license was not agreeded to")
    os.rmdir(dir)
    print("Please rerun the install script")
    exit()