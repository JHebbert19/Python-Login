# This is a demo to test login

import pickle

# Dictionary to store values
LoginDatabase = {}
filename = "Login"

Loop = "True"
while (Loop == "True"):
    choice = input("Do you want to login (L) or create an account (C)? ")

    if choice == "L":
        infile = open(filename, 'rb')
        LoginDatabase = pickle.load(infile)
        infile.close()
        Username = input("What is your Username? ")
        Password = input("What is your Password? ")
        if LoginDatabase[Username] == Password:
            print("Welcome!")
            Loop = "False"
        else:
            print("I'm sorry but that Username or Password is incorrect")
    elif choice == "C":
        Username = input("Enter a Username ")
        Password = input("Enter a Password ")
        LoginDatabase[Username] = Password
        outfile = open(filename, 'wb')
        pickle.dump(LoginDatabase, outfile)
        outfile.close()
    else:
        print("That was not a correct entry")

