import findtext
print("Hello!, It seems you selected a ofline install")
print('Just so you know there is a limit for errors')
print('\n--------------------------------------')
print("\nCurrent Statistics")
errors = 0
completed = 0
print(f'\nCurrent Errors: {errors} out of limit of 5')
print(f'\nCompleted Jobs: {completed} out of 10')
print('\n--------------------------------------')
print('Starting Job 1/10: Posfixinstall2.py patch | SubJob 1/5')
findtext.filereplace('posfixinstall2.py', 'print("Please ready the license below\n")', '#', 'Subjob 2/5 Completed')
findtext.filereplace('posfixinstall2.py', 'dirtest = "eCrypt-Installer"', 'dirtest = os.getcwd()', 'Subjob 3/5 Completed')
findtext.filereplace('posfixinstall2.py', 'print("\n")', '#', 'SubJob 4/5 Completed')
findtext.filereplace('posfixinstall2.py', 'print(license.read())', "#", 'SubJob 5/6')
findtext.filereplace('posfixinstall2.py', "os.system('curl https://raw.githubusercontent.com/Majix-Co/map-server/refs/heads/Installmain/LICENSE -o licensecompare.txt')", '#', 'SubJob 6/6')
completed + 1
print('\n--------------------------------------')
print("\nCurrent Statistics")
print(f'\nCurrent Errors: {errors} out of limit of 5')
print(f'\nCompleted Jobs: {completed} out of 10')
print('\n--------------------------------------')
print('Starting Job 2/10: Posfixinstall.sh patch | SubJob 0/19')
