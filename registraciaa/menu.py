import registracia
import login
import os
import sys

def menu():
    while True:
        os.system("cls")
        print("Welcome, are you a registered user ?")
        question = input("Yes(y)\nNo(n)\n")
        if question.lower() == "y" or question.lower() == "yes":
            login.login()
            continue
        
        if question.lower() == "n" or question.lower() == "no":
            registracia.registracia()
            login.login()
            continue
        
        if question.lower() == "exit":
            sys.exit(0)

        # wrong answer

        print("incorrect answer")
        

if __name__ == "__main__":
    menu()
