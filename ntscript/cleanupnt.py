import os
import shutil
import time
dir = os.getcwd() + "\\" + "eCrypt-Installer" + "\\"
rmdir =os.getcwd() + "\\" + "eCrypt-Installer"
print("Majix Installer")
print("\n5/5 | Cleanup\n")
os.remove(dir + 'decrypt.py')
os.remove(dir + 'eCryptcm.py')
os.remove(dir + 'install.py')
os.remove(dir + 'passwordgencm.py')
os.remove(dir + 'posfixinstall2.py')
os.remove(dir + 'postfixinstall3.py')
os.remove(dir + 'cleanup.py')
print("Installer completed okay!")
source = "eCrypt4.1.py"
i = input("Where do you want to save the installed files? Give full directory: ")
try:
  mainvar = open('tempfile.txt', 'r')
  tempvar = mainvar.read().strip()
  finalvar = tempvar + '/' + "posfixinstall.bat"
  mainvar.close()
  os.remove(finalvar)
  os.remove('tempfile.txt')
  dest = i
  shutil.move(source, dest)
  source = "passwordgen3.py"
  shutil.move(source, dest)
  # Add dir file infomation back to rmtree DO NOT DELETE THE ENTIRE DESKTOP!
  # Add Dir and os.cwd() Functions to top lines add os.remove() Brackets
  shutil.rmtree(rmdir)
  exit()
except FileNotFoundError:
  os.mkdir(i)
  print("Directory Made")
  dest = i
  shutil.move(source, dest)
  source = "passwordgen3.py"
  shutil.move(source, dest)
  exit()



