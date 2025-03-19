#! /bin/bash
echo ////////////////////////////////////////////[Majix Installer]//////////////////////////////////////////
echo \n3/5 | Preparing for Decryption
curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/ecryptinkey.key -o ecryptinkey.key
curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/password3key.key -o password3key.key
sleep 5
echo \nAlright!, Files were downloaded sucsefully running python code
python3 decrypt.py
