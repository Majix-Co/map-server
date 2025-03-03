import filecmp
import time
import os
print("Majix Installer")
print("2/5 | Comparing files to web versions")
time.sleep(2)
dir = os.getcwd()
source = dir + "/" + "eCryptcm.py"
scheck1 = dir + "/" + "eCrypt4.1.py"
print("Checking values")
filecheck = filecmp.cmp(source,scheck1)
if filecheck == True:
    print("Okay File looks okay")
    source = dir + "/" + "passwordgencm.py"
    scheck1 = dir + "/" + "passwordgen3.py"
    filecheck2 = filecmp.cmp(source,scheck1)
    if filecheck2 == True:
        print("All checks Passed!")
        print("Preparing next check")
        os.system('./postfixinstall3.py')
        exit()
    elif filecheck2 == False:
        print("Looks like the file is not right")
        exit()
elif filecheck == False:
    print("File may have been tampered with they do not match killing script")
    exit()