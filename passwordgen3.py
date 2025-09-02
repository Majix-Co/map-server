import random
import string
import secrets
import os
#recenterror = 0

#For bypassing of block list set block list to "None" leave var empty #
passwordlist = []
#Below is version code number
versioncodename = "4.3D"
passwordsymbols = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','<','>','?','/','[',']','{','}','|','`','~']
blocklist = ""
','.join(blocklist)
allowedlist = ['1','2','3','4','5','6','7','8','9','0']
blocklist = ''.join(blocklist)
#print("Current Block list", blocklist)
def startcode():
    print("Welcome to the Password Generator")
    print("Your password will be temporary saved to the script before being deleted")
    print("© Majix Co.")
    print("Current Version is: ", versioncodename)
    print("Please answer the questons below")
    print("\nThis script is a bit old and since does not have MUF(Majix Update Service) capabilities.\nYou may have to check for updates yourself if somthing breaks")
    # Q var is password length
    try:
        O = input("Password Length: ")
        if O == "":
            print("\nPlease enter a number do not leave blank")
            print("\nPlease try again by rerunning the script")
            startcode()
        elif any(char in blocklist for char in O):
            #char in blocklist for char in 0 is checking if a char in the list is in the var O
            print("\nYou typed a invalid charchter please try again\n")
            print("\nPlease try again")
            print("\nERROR")
            startcode()
        elif any(char in allowedlist for char in O):
            q = int(O)
            print("Your password will contain numbers letters")
            p1 = random.choices(string.ascii_uppercase, k=q)
            p2 = random.choices(string.digits, k=q)
            p3 = random.choices(string.ascii_lowercase, k=q)
            ''.join(p1)
            ''.join(p2)
            ''.join(p3)
            p4 = [''.join(passwordsymbols)]
            passwordlist = list(p1 + p2 + p3 + p4)
            # print("Current Vars (Unshuffled Varibals avaible for password generation | Unformated text): ")
            # print(passwordlist)
            random.shuffle(passwordlist)
            print("Final Password: ")
            final_password = ''.join(secrets.choice(passwordlist) for i in range(q))
            print(final_password[:q])
            print("Thank you for using this tool!")
            print("Your password has been cleared")
            print("\nWould you like to save the password to the current working directory?(y/n)")
            i = input("")
            if i == "n":
                print("Okay will not generate file")
                exit()
            else:   
                fileexist = os.path.isfile('password.txt')
                if fileexist == False:
                    fp = open('password.txt', 'x')
                    write = final_password[:q]
                    fp = open('password.txt', 'w')
                    fp.write(write)
                    fp.close
                    del final_password
                    del passwordlist
                    del p1
                    del p2
                    del p3
                    del p4
                elif fileexist == True:
                    print("Whoops, Looks life the file to update already exist!")
                    print("Please move the file out the current directory OR on the following prompt type delete me")
                    print("Majix OnDomand-Prompt use either delete or exit")
                    i = input('majix>')
                    if i == "exit":
                        exit()
                    elif i == "delete":
                        print("Okay deleting file")
                        os.remove('password.txt')
                        exit()
        elif O == "0":
            print("\nPlease use a higher number")
            startcode()
        else:
            print("\nE10: The input given is invalid use numbers only")
            print("\nEither there was a code fault or was a user error.\nA critical error occured")
            print("\nInfo: This is a fault error this happens a piece of code may have skiped checks")
            print("\nCheck if the ""if"" statement on line 23 is correctly parsing blocklist")
            quit()
    except Exception as e:
        print("\nWhoops!, Looks like a letter may have been parsed to the main randomizer")
        print("\nFor debugers the exact error is listed below")
        print("\nFor regular users try getting a updated code system or delete this version and use install.py")
        print("\nIf you changed blocklist set is back to defaults and see if it works again")
        print("\nException caught as:", e)
        quit()
startcode()