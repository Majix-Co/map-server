@echo off
set olddirectory=%CD%
cd ..
set currentworking=%CD%
del /f posfixinstall.bat
move "%olddirectory%" "%currentworking%"
cd %currentworking%
rmdir /s /q eCrypt-Installer
