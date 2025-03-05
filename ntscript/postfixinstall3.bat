@echo off
echo ////////////////////////////////////////////[Majix Installer]//////////////////////////////////////////
echo "3/5 | Preparing for Decryption"
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ecryptinkey.key -o ecryptinkey.key
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/password3key.key -o password3key.key
echo \nAlright!, Files were downloaded sucsefully running python code
python3 decrypt.py