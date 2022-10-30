import getpass
import menu
import time
import login
import os
def pwchange(userName, realPassWord):
    user_folder = "registraciaa\\users\\"
    filename = user_folder + userName +".txt"
    print ("First we need to make sure that you know your original password... ")
    old_word_pass = getpass.getpass("old password: ")
    file = open(filename,"r")
    user_name = file.read().splitlines()[0]
    if realPassWord == old_word_pass:
        print ("What would you like to change your password to")
        pass_word =getpass.getpass("new password :")
        fajl = open(filename,"w")
        fajl.write (user_name +"\n")
        fajl.write (pass_word)
        file.close
        print("password successfully changed")
        time.sleep(1.5)
        login.login()
    else:
        print ("incorrect password try again ?")
        q1=input("Yes=1\nNo=0\n")
        if q1 == "1":
            pwchange()
        else:
            menu.menu()
        





if __name__ == "__main__":
    pwchange()
