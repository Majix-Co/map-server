#! /bin/bash
echo Majix Installer for eCrypt
echo Please enter password below to install curl
sudo apt-get install curl
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/install.py -o install.py
python3 install.py
