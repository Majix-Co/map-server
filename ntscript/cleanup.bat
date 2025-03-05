@echo off
move cleanup.bat %UserProfile%\cleanup.bat
cd ..
rmdir /s /q eCrypt-Installer
del /f posfixinstall.bat
del /f %UserProfile%\cleanup.bat


