import os
import shutil
mainvar = open('tempfile.txt', 'r')
tempvar = mainvar.read().strip()
mainvar.close()
dir = os.getcwd() + "\\" + "eCrypt-Installer"
print("////////////////////////////////////////////[Majix Installer]//////////////////////////////////////////")
print("3/5 | Preparing for Decryption")
os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ecryptinkey.key -o ecryptinkey.key')
shutil.move(tempvar + "\\" + "ecryptinkey.key", dir)
os.system('curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/password3key.key -o password3key.key')
shutil.move(tempvar + "\\" + "password3key.key", dir)
print("\nAlright!, Files were downloaded sucsefully running python code")
run = "python3" + " " + dir + "\\" + "decrypt.py"
os.system(run)
exit