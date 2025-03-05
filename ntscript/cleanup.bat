@echo off
set olddirectory=%CD%
cd ..
set currentworking=%CD%
del /f posfixinstall.bat
curl https://raw.githubusercontent.com/Majix-Co/eCrypt-Services/refs/heads/Installmain/ntscript/cleanup2.bat -o cleanup2.bat
call cleanup2.bat
exit