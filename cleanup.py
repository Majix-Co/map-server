import os
import shutil
print("Majix Installer")
print("5/5 | Cleanup")
os.remove('decrypt.py')
os.remove('eCryptcm.py')
os.remove('install.py')
os.remove('passwordgencm.py')
os.remove('posfixinstall2.py')
os.remove('postfixinstall.sh')
os.system('cd ..')
os.remove('posfixinstall.sh')
os.system('cd eCrypt-Installer')
source = os.cwd()
source2 = "eCrypt4.1.py"
finalsource = source + "/" + source2
os.system('cd ..')
dest = os.getcwd()
shutil.move(finalsource, dest)
source2 = "passwordgen3.py"
finalsource = source + "/" + source2
shutil.move(finalsource, dest)

