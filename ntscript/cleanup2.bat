@echo off
taskkill /IM cleanup.bat /f
del /f cleanup.bat
rmdir /s /q eCrypt-Installer
del /f cleanup2.bat
exit