import time
import os
import loading
import getpass
import registracia
import pwchange
def login():
        print ("To login you'll need to type your username first")
        user_folder = "registraciaa\\users\\"
        time.sleep (1.5)
        try:
            user_name = input ("username: ")
            filename = user_folder + user_name +".txt"
            file = open(filename, "r")       
            realPassWord = file.read().splitlines()[1]
            loading.loading()
            print ("username: " + user_name)
            pass_word = getpass.getpass("password: ")
            if pass_word == realPassWord:
                print ("successfuly logged in ")
                loading.loading()
                print ("Would you like to change your password?")
                change = input("Yes=1\nNo=0\n")
                if change == "1":
                    pwchange.pwchange(user_name, realPassWord)
                else:
                    print("goodbye")
            elif pass_word != realPassWord:
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


