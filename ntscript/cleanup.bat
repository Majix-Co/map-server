@echo off
set olddirectory=%CD%
cd ..
set currentworking=%CD%
del /f posfixinstall.bat
move %olddirectory% %CD%
rmdir /s /q eCrypt-Installer