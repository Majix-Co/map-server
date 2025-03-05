@echo off
REM Store the current directory path
set currentDir=%cd%

REM Navigate to the directory above the current one
cd ..

REM Check if the directory to delete exists before attempting to delete it
IF EXIST %currentDir% (
    rd /s /q %currentDir%
) ELSE (
    echo Directory %currentDir% not found, skipping deletion.
)


REM Exit the script
exit
