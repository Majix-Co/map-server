const crypto = require('crypto');

let passwordlist = [];
const versioncodename = "V2BETA -- Javascript conversion";
const passwordsymbols = ['!','@','#','$','%','^','&','*','(',')','-','_','+','=','<','>','?','/','[',']','{','}','|','`','~'];
const blocklist = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','!','@','#','$','%','^','&','*','(',')','-','_','+','=','<','>','?','/','[',']','{','}','|','-1','-2','-3','-4','-5','-6','-7','-8','-9'];
const allowedlist = ['1','2','3','4','5','6','7','8','9','0'];

function startcode() {
    console.log("Welcome to the Password Generator");
    console.log("Your password will be temporary saved to the script before being deleted");
    console.log("© Caiden Pinter 2025");
    console.log("Current Version is: ", versioncodename);
    console.log("Please answer the questions below");

    const readline = require('readline').createInterface({
        input: process.stdin,
        output: process.stdout
    });

    readline.question("Password Length: ", O => {
        if (O === "") {
            console.log("Please enter a number do not leave blank");
            console.log("Please try again by rerunning the script");
            readline.close();
            startcode();
        } else if (Array.from(O).some(char => blocklist.includes(char))) {
            console.log("You typed an invalid character please try again");
            console.log("Please try again");
            readline.close();
            startcode();
        } else if (Array.from(O).some(char => allowedlist.includes(char))) {
            const q = parseInt(O, 10);
            console.log("Your password will contain numbers letters");
            let l = Array.from({ length: q }, () => String.fromCharCode(65 + Math.floor(Math.random() * 26)));
            let y = Array.from({ length: q }, () => Math.floor(Math.random() * 10).toString());
            let b = Array.from({ length: q }, () => String.fromCharCode(97 + Math.floor(Math.random() * 26)));
            l = l.join('');
            y = y.join('');
            b = b.join('');
            let p4 = passwordsymbols.join('');
            let p1 = l;
            let p2 = y;
            let p3 = b;
            passwordlist = Array.from(p1 + p2 + p3 + p4);
            console.log("Current Vars (Unshuffled Variables available for password generation | Unformatted text): ");
            console.log(passwordlist);
            passwordlist = passwordlist.sort(() => Math.random() - 0.5);
            console.log("Final Password: ");
            let final_password = Array.from({ length: q }, () => passwordlist[Math.floor(Math.random() * passwordlist.length)]).join('');
            console.log(final_password.slice(0, q));
            console.log("Thank you for using this tool!");
            console.log("Your password has been cleared");
            console.log("A problem has occurred please try again");
            readline.close();
            startcode();
        } else if (O === "0") {
            console.log("Please use a higher number");
            readline.close();
            startcode();
        } else {
            console.log("E10: The input given is invalid use numbers only");
            console.log("Either there was a code fault or was a user error.\nA critical error occurred");
            readline.close();
            process.exit(1);
        }
    });
}

startcode();

