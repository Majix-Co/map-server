import findtext
import time
import os
import cryptography
from cryptography.fernet import Fernet
print("Hello!, It seems you selected a ofline install")
print('Just so you know there is a limit for errors')
print('\n--------------------------------------')
print("\nCurrent Statistics")
errors = 0
completed = 0
print(f'\nCurrent Errors: {errors} out of limit of 5')
print(f'\nCompleted Jobs: {completed} out of 10')
print('\n--------------------------------------')
'''
 OK Posfixinstall.sh
 OK Posfixinstall2.py
OK postfixinstall3.sh
OK install.py
eCrypt4.4
password3.py

'''
print('Starting Job 1/10: Posfixinstall2.py patch | SubJob 1/5')
findtext.filereplace('posfixinstall2.py', 'print("Please ready the license below\n")', '#', 'Subjob 2/5 Completed')
findtext.filereplace('posfixinstall2.py', 'dirtest = "eCrypt-Installer"', 'dirtest = os.getcwd()', 'Subjob 3/5 Completed')
findtext.filereplace('posfixinstall2.py', 'print("\n")', '#', 'SubJob 4/5 Completed')
findtext.filereplace('posfixinstall2.py', 'print(license.read())', "#", 'SubJob 5/6')
findtext.filereplace('posfixinstall2.py', "os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/LICENSE -o licensecompare.txt')", '#', 'SubJob 6/6')
completed + 1
print('\n--------------------------------------')
print("\nCurrent Statistics")
print(f'\nCurrent Errors: {errors} out of limit of 5')
print(f'\nCompleted Jobs: {completed} out of 10')
print('\n--------------------------------------')
print('Starting Job 2/10: Posfixinstall.sh patch | SubJob 0/1')
time.sleep(3)
print("Clearing old document")
print("Writing New Document")
open('posfixinstall.sh', 'x')
posfixinstall = open('posfixinstall.sh', 'w')
posfixinstall.writelines(
'''
#! /bin/bash
echo -e "eCrypt Self Extracting Script"
echo -e "1/5 | Downloading needed files"
echo Preparing for deployment
echo -e "//////////////////////Preparing Self Extracting Script////////////////////////////////"
sleep 3
# echo Getting needed files
# echo Please enter password to install Curl
# sudo apt-get install curl
cd eCrypt-Installer
echo Getting files
# curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/eCrypt4.4.py -o eCrypt4.4.py
# curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/ufc.muf -o ufc.muf
pip install cryptography
sleep 3
echo Detected as encrypted
# curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/passwordgen3.py -o passwordgen3.py
echo "Switching back to python"
sleep 3
# curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/eCrypt4.4.py -o eCryptcm.py
# curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/LICENSE -o license.txt
# curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/passwordgen3.py -o passwordgencm.py
# curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/posfixinstall2.py -o posfixinstall2.py
# curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/postfixinstall3.sh -o postfixinstall3.sh
# curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/decrypt.py -o decrypt.py
# curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/cleanup.py -o cleanup.py
# curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/cleanup.sh -o cleanup.sh
# curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/findtext.py -o findtext.py
python3 posfixinstall2.py
'''
)
posfixinstall.close()
print('File updated | SubJob 1/1')
completed + 1
print('\n--------------------------------------')
print("\nCurrent Statistics")
print(f'\nCurrent Errors: {errors} out of limit of 5')
print(f'\nCompleted Jobs: {completed} out of 10')
print('\n--------------------------------------')
print('Starting Job 3/10: postfixinstall3.sh patch | SubJob 0/1')
completed + 1
print('\n--------------------------------------')
print("\nCurrent Statistics")
print(f'\nCurrent Errors: {errors} out of limit of 5')
print(f'\nCompleted Jobs: {completed} out of 10')
print('\n--------------------------------------')
print("This step has ended forwarding to next step")
os.system('chmod +x postfixinstall3.sh')
os.system('./postfixinstall3.sh')
