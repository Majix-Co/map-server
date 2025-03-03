import os
import shutil
print("Majix Installer")
print("5/5 | Cleanup")
os.remove('decrypt.py')
os.remove('eCryptcm.py')
os.remove('install.py')
os.remove('passwordgencm.py')
os.remove('posfixinstall2.py')
os.remove('postfixinstall3.sh')
os.remove('cleanup.py')
print("Installer completed okay!")
source = "eCrypt4.1.py"
os.system('chmod +x cleanup.sh')
i = input("Where do you want to save the installed files? Give full directory")
dest = i
shutil.move(source, dest)
source = "passwordgen3.py"
shutil.move(source, dest)
os.system('./cleanup.sh')
exit()


