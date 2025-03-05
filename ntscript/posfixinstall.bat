@echo off
echo -e "eCrypt Self Extracting Script"
echo -e "1/5 | Downloading needed files"
echo -e "\nWindows Version"
echo Preparing for deployment
echo -e "//////////////////////Preparing Self Extracting Script////////////////////////////////"
echo Getting needed files
cd eCrypt-Installer
echo Getting files
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/eCrypt4.1.py -o eCrypt4.1.py
echo Detected as encrypted
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/passwordgen3.py -o passwordgen3.py
echo "Switching back to python"
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/eCrypt4.1.py -o eCryptcm.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/passwordgen3.py -o passwordgencm.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/posfixinstall2.py -o posfixinstall2.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/postfixinstall3.sh -o postfixinstall3.sh
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/decrypt.py -o decrypt.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/cleanup.py -o cleanup.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/cleanup.sh -o cleanup.sh
python3 posfixinstall2.py
