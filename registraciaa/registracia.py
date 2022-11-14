import time 
import loading
import getpass
import os
import login
def registracia():
    print ("To register you'll need to type your username and your password.")
    time.sleep (1.5)
    user_name = input("username: ")
    user_folder = "registraciaa\\users\\"
    filename = user_folder + user_name + ".txt"
    check = os.path.exists(filename)
    loading.loading()
    if check == True:
        print ("User already registered, would you like to log in?")
        question = input("Yes=1\nNo=0\n")
        if question == "1":
            login.login()
        elif question == "0": 
            print ("Goodbye")
    if check == False:
        print ("username: " + user_name)
        pass_word = getpass.getpass("password: ")
        file = open(filename, "+w")
        file.write (user_name+"\n")
        file.write (pass_word)
        file.close
        print("successfully registered")

    
    
    


if __name__ == "__main__":
    registracia()