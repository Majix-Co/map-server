import os
import shutil
import time
print("Majix Installer")
print("\n5/5 | Cleanup\n")
os.remove('decrypt.py')
os.remove('eCryptcm.py')
os.remove('install.py')
os.remove('passwordgencm.py')
os.remove('posfixinstall2.py')
os.remove('postfixinstall3.bat')
os.remove('cleanup.py')
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
  shutil.rmtree()
  exit()
except FileNotFoundError:
  os.mkdir(i)
  print("Directory Made")
  dest = i
  shutil.move(source, dest)
  source = "passwordgen3.py"
  shutil.move(source, dest)
  exit()



