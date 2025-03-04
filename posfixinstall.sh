#! /bin/bash
echo eCrypt Self Extracting Script
echo 1/5 | Downloading needed files
echo \nPreparing for deployment\n
echo \n//////////////////////Preparing Self Extracting Script////////////////////////////////\n
sleep 5
echo Getting needed files
sudo apt-get install curl
cd eCrypt-Installer
echo Getting files
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/eCrypt4.1.py -o eCrypt4.1.py
sleep 5
echo \nDetected as encrypted\n
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/passwordgen3.py -o passwordgen3.py
echo \nSwitching back to python\n
sleep 5
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/eCrypt4.1.py -o eCryptcm.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/passwordgen3.py -o passwordgencm.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/posfixinstall2.py -o posfixinstall2.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/postfixinstall3.sh -o postfixinstall3.sh
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/decrypt.py -o decrypt.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/cleanup.py -o cleanup.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/cleanup.sh -o cleanup.sh
python3 posfixinstall2.py
