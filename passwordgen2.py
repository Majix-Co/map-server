import random
import string
import secrets
#recenterror = 0
#For bypassing the letter check system add everything in block list to allow list and set block list to none"
passwordlist = []
passwordsymbols = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','<','>','?','/','[',']','{','}','|','`','~']
blocklist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','@','#','$','%','^','&','*','(',')','-','_','+','=','<','>','?','/','[',']','{','}','|','-1','-2','-3','-4','-5','-6','-7','-8','-9']
allowedlist = ['1','2','3','4','5','6','7','8','9','0']
def startcode():
    print("Welcome to the Password Generator")
    print("Your password will be temporary saved to the script before being deleted")
    print("© Caiden Pinter 2025")
    print("Please answer the questons below")
    # Q var is password length
    O = input("Password Length: ")
    if O == "":
        print("Please enter a number do not leave blank")
        print("Please try again by rerunning the script")
        startcode()
    elif any(char in blocklist for char in O):
        #char in blocklist for char in 0 is checking if a char in the list is in the var O
        print("You typed a invalid charchter please try again")
        print("Please try again")
        startcode()
    elif any(char in allowedlist for char in O):
        q = int(O)
        print("Your password will contain numbers letters")
        l = random.choices(string.ascii_uppercase, k=q)
        y = random.choices(string.digits, k=q)
        b = random.choices(string.ascii_lowercase, k=q)
        j = ''.join(l)
        z = ''.join(y)
        o = ''.join(b)
        w = ''.join(passwordsymbols)
        p1 = j
        p2 = z
        p3 = o
        p4 = w
        passwordlist = list(p1 + p2 + p3 + p4)
        print("Current Vars (Unshuffled Varibals avaible for password generation | Unformated text): ")
        print(passwordlist)
        random.shuffle(passwordlist)
        print("Final Password: ")
        final_password = ''.join(secrets.choice(passwordlist) for i in range(q))
        print(final_password[:q])
        print("Thank you for using this tool!")
        print("Your password has been cleared")
        Warning("A problem has occured please try again")
        del final_password
        del passwordlist
        del p1
        del p2
        del p3
        del p4
    elif O == "0":
        print("Please use a higher number")
        startcode()
    else:
        print("E10: The input given is invalid use numbers only")
        print("Either there was a code fault or was a user error.\nA critical error occured")
        quit()
startcode()