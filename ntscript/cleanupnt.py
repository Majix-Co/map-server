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
  finalvar = mainvar + "/" + "posfixinstall.bat"
  mainvar.close()
  os.remove(finalvar)
  os.remove('tempfile.txt')
  dest = i
  shutil.move(source, dest)
  source = "passwordgen3.py"
  shutil.move(source, dest)
  shutil.rmtree(os.getcwd())
  exit()
except FileNotFoundError:
  os.mkdir(i)
  print("Directory Made")
  dest = i
  shutil.move(source, dest)
  source = "passwordgen3.py"
  shutil.move(source, dest)
  os.system('cleanup.bat')
  exit()



