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
echo "Downloading all other files requried"
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/eCrypt4.1.py -o eCryptcm.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/passwordgen3.py -o passwordgencm.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ntscript/posfixinstall2nt.py -o posfixinstall2.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ntscript/postfixinstall3.bat -o postfixinstall3.bat
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ntscript/decryptnt.py -o decrypt.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ntscript/cleanupnt.py -o cleanup.py
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ntscript/cleanup.bat -o cleanup.bat
@REM curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ufc.muf -o ufc.muf
echo "Returning to Python Codebase"
python3 posfixinstall2.py
