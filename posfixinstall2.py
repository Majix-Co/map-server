import filecmp
import time
import os
import subprocess
print("\nMajix Installer")
print("\n2/5 | Comparing files to web versions\n")
time.sleep(2)
dir = os.getcwd()
dirtest = "eCrypt-Installer"
source3 = dir + "/" + "license.txt"
def startgui():
    #print("Please ready the license below\n")
    #print("\n")
    #print(license.read())
    i = input("\nDo you agree to the license? (yes/no[default])")
    license.close()
    os.remove(source3)
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
        print("Please rerun the install script")
        deldir = "rm -rf " + dir
        os.system(deldir)
        exit()
def start():
    print("Please ready the license below\n")
    print("\n")
    print(license.read())
    i = input("\nDo you agree to the license? (yes/no[default])")
    license.close()
    os.remove(source3)
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
        print("Please rerun the install script")
        deldir = "rm -rf " + dir
        os.system(deldir)
        exit()
if dirtest in dir:
    try:
        file = open('guiused.mef', 'r')
        print("Whoops! Looks like you tried to use gui and it failed before now defaulting to text")
        file.close()
        os.remove('guiused.mef')
        print(Exception)
        start()
    except:
        license = open(source3, 'r')
        x = input("Would you like to use a GUI license viewer? (y/n): ")
        if x == "y":
            i = input("What editor would you like to use?(kate/gedit/xed/nano): ")
            if i == "kate":
                #Kde Plasma text Editor lines 87-96
                try:
                    print("Okay launching kate")
                    kate = ["kate", source3]
                    subprocess.run(kate, check = True)
                    startgui()
                except:
                    print("Your system could not launch kate will rerun script try using text instead")
                    rerun = "python3 " + __file__
                    os.system(rerun)
                    file = open('guiused.mef', 'x')
                    file.close()
            elif i == "gedit":
                # Gnome Editor lines 97-106
                try:
                    print("Okay launching gedit")
                    gedit = ["gedit", source3]
                    subprocess.run(gedit, check = True)
                    startgui()
                except:
                    print("Your system could not launch gedit will rerun script try using text instead")
                    rerun = "python3 " + __file__
                    os.system(rerun) 
                    file = open('guiused.mef', 'x')
                    file.close()
            elif i == "xed":
                # XED Editor Lines 107-116
                try:
                    print("Okay launching XED")
                    xed = ["xed", source3]
                    subprocess.run(xed, check = True)
                    startgui()
                except:
                    print("Your system could not launch xde will rerun script try using text instead")
                    rerun = "python3 " + __file__
                    os.system(rerun)
                    file = open('guiused.mef', 'x')
                    file.close()
            elif i =="nano":
                # Nano Editor Lines 117-128
                try:
                    print("Opening in nano")
                    nano = ["nano", source3]
                    print(nano)
                    subprocess.run(nano, check = True)
                    startgui()
                except:
                    print("Your system could not launch nano will rerun script try using text instead")
                    rerun = "python3 " + __file__
                    os.system(rerun)
                    file = open('guiused.mef', 'x')
                    file.close()
            else:
                print("Whoops!, Looks like you did not type a valid editor name defaulting to text")
                start()
        else:
            start()
    else:
        print('\nWhoops!, A critical error was detected kill script to save system')
        print('\nWhat happened? You are NOT running this in the install directory')
        print("\nDoing this can delete dierectory's you do not want to be deleted")
        print('\nDelete this and ONLY use install.py DO NOT attempt to run any scripts in that folder manually')
        print("\nRunning one of the install scripts manually can have unexpected results")
        print("\nPlease use the automated installer if it fails Rerun the main installer.py. Please do not attempt to run any other script manually\n")
        os.remove(__file__)
        exit('E-Exit: System Failsafe')
