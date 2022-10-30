import time 
import moduly
import getpass
import os
import login
def registracia():
    print ("To register you'll need to type your username and your password.")
    time.sleep (1.5)
    userName = input("username: ")
    user_folder = "C:\\coding\\kreativita\\registraciaa\\users\\"
    filename = user_folder + userName + ".txt"
    check = os.path.exists(filename)
    moduly.loading()
    if check == True:
        print ("User already registered, would you like to log in?")
        question = input("Yes=1\nNo=0\n")
        if question == "1":
            login.login()
        elif question == "0": 
            print ("Goodbye")
    if check == False:
        print ("username: " + userName)
        passWord = getpass.getpass("password: ")
        file = open(filename, "+w")
        file.write (userName+"\n")
        file.write (passWord)
        file.close
        print("successfully registered")

    
    
    


if __name__ == "__main__":
    registracia()