import os
import shutil
mainvar = open('tempfile.txt', 'r')
tempvar = mainvar.read().strip()
mainvar.close()
print("////////////////////////////////////////////[Majix Installer]//////////////////////////////////////////")
print("3/5 | Preparing for Decryption")
os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ecryptinkey.key -o ecryptinkey.key')
os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/password3key.key -o password3key.key')
print("\nAlright!, Files were downloaded sucsefully running python code")
os.system('python3 decrypt.py')
exit