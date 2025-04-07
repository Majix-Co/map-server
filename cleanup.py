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
  symbol = "/"
  i = input("Where do you want to save the installed files? Give full directory: ")
  if i.endswith(symbol):
    try:
      dest = i
      shutil.move(source, dest)
      source = "passwordgen3.py"
      shutil.move(source, dest)
      os.system('./cleanup.sh')
    
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
      
      else:
        print("Okay Aborting Install")
        os.system('./cleanup.sh')
  else:
    print("Whoops!, That directory is not valid auto corecting")
    i = i + "/"
    print("Added slash to directory (Now is valid)")
    try:
      dest = i
      shutil.move(source, dest)
      source = "passwordgen3.py"
      shutil.move(source, dest)
      os.system('./cleanup.sh')
    
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
      
      else:
        print("Okay Aborting Install")
        os.system('./cleanup.sh')

except:
  print("Whoops!, Looks like one of the files that were attempted to get deleted do not exist")
  print("Falling back to finish install")
  source = "eCrypt4.4.py"
  os.system('chmod +x cleanup.sh')
  i = input("Where do you want to save the installed files? Give full directory: ")
  try:
    symbol = "/"
    if i.endswith(symbol):
      try:
        dest = i
        shutil.move(source, dest)
        source = "passwordgen3.py"
        shutil.move(source, dest)
        os.system('./cleanup.sh')
      
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
        
        else:
          print("Okay Aborting Install")
          os.system('./cleanup.sh')
    else:
      try:
        dest = i
        shutil.move(source, dest)
        source = "passwordgen3.py"
        shutil.move(source, dest)
        os.system('./cleanup.sh')
      
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
        
        else:
          print("Okay Aborting Install")
          os.system('./cleanup.sh')
  except:
    e = Exception
    print("\nA fatal error occured when trying to copy files")
    print("\nThe exception was: " + e)
    print("\nThe install was aborted")
    print("\nSorry for the error but I could not copy files")
    print("\nIf this is a protected directory please run install.py as root")
    print("\nOr login as root user and retry")
    print("Press Ctrl+C withen 5 seconds to cancel retry")
    time.sleep(5)
    rerun5 = "python3 " + "cleanup.py"
    os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/cleanup.py -o cleanup.py')
    os.system(rerun5)
    



