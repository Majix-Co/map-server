import os
import shutil
import time
print("Majix Installer")
print("\n5/5 | Cleanup\n")
try:
  os.remove('decrypt.py')
  os.remove('eCryptcm.py')
  os.remove('install.py')
  os.remove('license.txt')
  os.remove('passwordgencm.py')
  os.remove('posfixinstall2.py')
  os.remove('postfixinstall3.sh')
  os.remove('cleanup.py')
  os.remove('licensecompare.txt')
  print("Installer completed okay!")
  source = "eCrypt4.4.py"
  os.system('chmod +x cleanup.sh')
  i = input("Where do you want to save the installed files? Give full directory: ")
  try:
    dest = i
    shutil.move(source, dest)
    source = "passwordgen3.py"
    shutil.move(source, dest)
    os.system('./cleanup.sh')
    exit()
  except FileNotFoundError:
    print("You selected the directory " + i)
    u = input("The directory does not exist would you like to create it? (y/n)")
    if u == "y":
      os.mkdir(i)
      dest = i
      shutil.move(source, dest)
      source = "passwordgen3.py"
      shutil.move(source, dest)
      os.system('./cleanup.sh')
      exit()
    else:
      print("Okay Aborting Install")
      os.system('./cleanup.sh')
      exit()
except:
  print("Whoops!, Looks like one of the files that were attempted to get deleted do not exist")
  print("Falling back to finish install")
  source = "eCrypt4.4.py"
  os.system('chmod +x cleanup.sh')
  i = input("Where do you want to save the installed files? Give full directory: ")
  try:
    try:
      dest = i
      shutil.move(source, dest)
      source = "passwordgen3.py"
      shutil.move(source, dest)
      os.system('./cleanup.sh')
      exit()
    except FileNotFoundError:
      print("You selected the directory " + i)
      u = input("The directory does not exist would you like to create it? (y/n)")
      if u == "y":
        os.mkdir(i)
        dest = i
        shutil.move(source, dest)
        source = "passwordgen3.py"
        shutil.move(source, dest)
        os.system('./cleanup.sh')
        exit()
      else:
        print("Okay Aborting Install")
        os.system('./cleanup.sh')
        exit()
  except:
    e = ""
    Exception == e
    print("\nA fatal error occured when trying to copy files")
    print("\nThe exception was: " + e)
    print("\nThe install was aborted")
    print("\nSorry for the error but I could not copy files")
    print("\nIf this is a protected directory please run install.py as root")
    print("\nOr login as root user and retry")
    print("Press Ctrl+C withen 5 seconds to cancel retry")
    time.sleep(5)
    rerun5 = "python3 " + __file__
    os.system(rerun5)
    exit()



