import loading
import getpass
import registracia
import os

basedir = os.path.dirname(__file__)

def login():
    print("To login you'll need to type your username first")
    user_folder = os.path.join(basedir, "users")
    user_name = input("username: ")
    filename = os.path.join(user_folder, f"{user_name}.txt")
    
    logged_in = False
    while not logged_in:
        # try - checks if the txt file is existing, except if theres an error what will happen
        # if os.path.exists(filename):

        try:
            with open(filename, "r") as file:
                realPassWord = file.read().splitlines()[1]
        except FileNotFoundError:
            print("Seems like you're not a registered user, would you like to register?")
            while True:
                question = input("Yes(y)\nNo(n)\n")
                if question.lower() == "y" or question.lower() =="yes":
                    registracia.registracia()
                    continue
                
                elif question.lower() == "n" or question.lower() =="no":
                    print("Goodbye")
                    return
                else:
                    print("incorrect answer")

        loading.loading()
        print("username: " + user_name)
        pass_word = getpass.getpass("password: ")



        if pass_word == realPassWord:
            logged_in = True
            loading.loading()
            print("Successfuly logged in.")
            print("Would you like to change your password?")
            while True:
                question = input("Yes(y)\nNo(n)\n")
                if question.lower() == "y" or question.lower() == "yes":
                    pwchange(user_name, realPassWord)
                    break
                elif question.lower() == "n" or question.lower() =="no":
                    print("Goodbye")
                    return
                else:
                    print("incorrect answer")
        else:
            print ("incorrect password, would you like a hint ?")
            logged_in = False
            question = input("Yes(y)\nNo(n)\n")
            if question.lower() == "y" or question.lower() == "yes":
                print (user_name, realPassWord)
                safety_question(user_name, realPassWord)
                break
            elif question.lower() == "n" or question.lower() =="no":
                print("Goodbye")
                return
            else:
                    print("incorrect answer")

def pwchange(user_name, realPassWord):
    user_folder = os.path.join(basedir, "users")
    filename = os.path.join(user_folder, f"{user_name}.txt")

    print("First we need to make sure that you know your original password... ")
    old_passwd = getpass.getpass("old password: ")

    if realPassWord == old_passwd:
        print("What would you like to change your password to")
        pass_word = getpass.getpass("new password :")
        with open(filename, "w") as file:
            file.write(f"{user_name}\n{pass_word}\n")
        print("Password successfully changed")
        login()

        # next_fun = login
        # while True:
        #     next_fun()

    else:
        while True:
            print("incorrect password try again ?")
            question = input("Yes(y)\nNo(n)\n")
            if question.lower() == "y" or question.lower() == "yes":
                pwchange(user_name, realPassWord)
                break
            else:
                print("Goodbye")
                return

def safety_question(user_name, realPassWord):
    answer = ""
    user_folder = os.path.join(basedir, "users")
    filename = os.path.join(user_folder, f"{user_name}.txt")
    with open(filename, "r") as file:
                safety_question = file.read().splitlines()[2]
                safety_answer = file.read().splitlines()[3]
    print (safety_answer)
    print (safety_question)
    while answer.lower != safety_answer:
        print (safety_question)
        answer = input("answer: \n")
        if answer == safety_answer:
            print (f"Your password is {realPassWord}")
            break
        else:
            print ("Incorrect answer!")
            return




if __name__ == "__main__":
    login()
