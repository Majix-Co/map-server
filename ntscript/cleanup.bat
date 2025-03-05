@echo off
copy cleanup.bat C:\Users\cleanup.bat
cd ..
rmdir /s /q eCrypt-Installer
del /f posfixinstall.bat
del /f C:\Users\cleanup.bat


