import time
import os
import moduly
import getpass
import registracia
def login():
        print ("To login you'll need to type your username first")
        user_folder = "C:\\coding\\kreativita\\registraciaa\\users\\"
        time.sleep (1.5)
        try:
            userName = input ("username: ")
            filename = user_folder + userName +".txt"
            file = open(filename, "r")       
            realPassWord = file.read().splitlines()[1]
            moduly.loading()
            print ("username: " + userName)
            passWord = getpass.getpass("password: ")
            if passWord == realPassWord:
                print ("successfuly logged in ")
                time.sleep(5)
            elif passWord != realPassWord:
                print ("incorrect password")
                login()
        except FileNotFoundError:
            print ("Seems like you're not a registered user, would you like to register ?")
            question = input("Yes=1\nNo=0\n")
            if question == "1":
                registracia.registracia()
            elif question == "0": 
                print("Goodbye")


        

if __name__ == "__main__":
    login()


