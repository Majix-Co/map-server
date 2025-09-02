import os
import shutil
import time
dir = os.getcwd() + "\\" + "eCrypt-Installer" + "\\"
rmdir = os.getcwd() + "\\" + "eCrypt-Installer"
print("Majix Installer")
print("\n5/5 | Cleanup\n")
try:
  os.remove(dir + 'decrypt.py')
  os.remove(dir + 'eCryptcm.py')
  os.remove(dir + 'install.py')
  os.remove(dir + 'passwordgencm.py')
  os.remove(dir + 'posfixinstall2.py')
  os.remove(dir + 'postfixinstall3.py')
  os.remove(dir + 'cleanup.py')
  os.remove(dir + 'license.txt')
  os.remove(dir + 'findtext.py')
  print("Installer completed okay!")
  source = dir + "eCrypt4.4.py"
  i = input("\nWhould you like to copy files to original directory you ran this script from or specify? N to specify | Y to autocopy: \n")
  if i == "Y":
    mainvar = open('tempfile.txt', 'r')
    tempvar = mainvar.read().strip()
    shutil.move(source, tempvar)
    source = dir + "passwordgen3.py"
    shutil.move(source, tempvar)
    mainvar.close()
    mainvar = open('tempfile.txt', 'r')
    tempvar = mainvar.read().strip()
    finalvar = tempvar + '\\' + "posfixinstall.bat"
    mainvar.close()
    #os.remove(tempvar + '\\' + 'tempfile.txt')
    dest = tempvar
    shutil.move(source, dest)
    source = dir + "passwordgen3.py"
    shutil.move(source, dest)
    # Add dir file infomation back to rmtree DO NOT DELETE THE ENTIRE DESKTOP!
    # Add Dir and os.cwd() Functions to top lines add os.remove() Brackets
    shutil.rmtree(rmdir)
    os.remove(tempvar + '\\' + 'tempfile.txt')
    os.remove(tempvar + '\\' + 'findtext.py')
    print("Installation Completed Ok")
    exit()
  else:
    i = input("Where do you want to save the installed files? Give full directory: ")
    try:
      mainvar = open('tempfile.txt', 'r')
      tempvar = mainvar.read().strip()
      finalvar = tempvar + '\\' + "posfixinstall.bat"
      mainvar.close()
      #os.remove(tempvar + '\\' + 'tempfile.txt')
      dest = i
      shutil.move(source, dest)
      source = dir + "passwordgen3.py"
      shutil.move(source, dest)
      # Add dir file infomation back to rmtree DO NOT DELETE THE ENTIRE DESKTOP!
      # Add Dir and os.cwd() Functions to top lines add os.remove() Brackets
      shutil.rmtree(rmdir)
      os.remove(tempvar + '\\' + 'tempfile.txt')
      os.remove(tempvar + '\\' + 'findtext.py')
    except FileNotFoundError:
      print("Directory given: " + i)
      u = input("Directory not found would you like to create directory? (y/n)")
      if u == "y":
        os.mkdir(i)
        print("Directory Made")
        dest = i
        shutil.move(source, dest)
        source = "passwordgen3.py"
        shutil.move(source, dest)
        os.remove(tempvar + '\\' + 'tempfile.txt')
        os.remove(tempvar + '\\' + 'findtext.py')
      else:
        print("Aborting, Try a new directory")
        rerun = "python3 " + dir + "\\" + __file__
        os.system(rerun)
except:
  try:
    print("Sorry :(, But I could not delete all files. Now falling back to copy mode")
    mainvar = open('tempfile.txt', 'r')
    tempvar = mainvar.read().strip()
    finalvar = tempvar + '\\' + "posfixinstall.bat"
    mainvar.close()
    os.remove(tempvar + '\\' + 'tempfile.txt')
    os.remove(tempvar + '\\' + 'findtext.py')
    try:
      dest = i
      shutil.move(source, dest)
      source = dir + "passwordgen3.py"
      shutil.move(source, dest)
      # Add dir file infomation back to rmtree DO NOT DELETE THE ENTIRE DESKTOP!
      # Add Dir and os.cwd() Functions to top lines add os.remove() Brackets
      shutil.rmtree(rmdir)
    except FileNotFoundError:
      print("Directory given: " + i)
      u = input("Directory not found would you like to create directory? (y/n)")
      if u == "y":
        os.mkdir(i)
        print("Directory Made")
        dest = i
        shutil.move(source, dest)
        source = "passwordgen3.py"
        shutil.move(source, dest)
      else:
        print("Aborting, Try a new directory")
        rerun = "python3 " + dir + "\\" + __file__
        os.system(rerun)
  except Exception as e:
    print("To many errors occured install can not continue")
    print("\nYou can restart the installer but it may not work\n")
    print("Check permissions and if any files were deleted before the command was issued")
    print("Installation Terminated")
    exit()