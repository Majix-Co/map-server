@echo off
set olddirectory=%CD%
cd ..
set currentworking=%CD%
del /f posfixinstall.bat
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ntscript/cleanup2.py -o cleanup2.py
python3 cleanup2.py
