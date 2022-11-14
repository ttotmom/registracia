import registracia
import login
import os 
import time
def menu():
    os.system("cls")
    print ("Welcome, are you a registered user ?")
    question = input("Yes=1\nNo=0\n")
    if question =="1":
        login.login()
        time.sleep(5)
        menu()
    elif question =="0":
        registracia.registracia()
        login.login()
menu()

if __name__ == "__main__":
    menu()

