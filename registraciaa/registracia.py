import loading
import getpass
import os
import login

basedir = os.path.dirname(__file__)

def registracia():
    print("To register you'll need to type your username and your password.")
    user_name = input("username: ")

    user_folder = os.path.join(basedir, "users")
    filename = os.path.join(user_folder, f"{user_name}.txt")
    check = os.path.exists(filename)

    loading.loading()
    while True:
        if check == True:
            print("User already registered, would you like to log in?")
            question = input("Yes(y)\nNo(n)")
            if question.lower() == "y" or question.lower() == "yes":
                login.login()
            elif question.lower() == "n" or question.lower() == "no":
                print("Goodbye")
                break
            else:
                print("incorrect answer registracia1")
        else:
            print ("username: " + user_name)
            pass_word = getpass.getpass("password: ")
            with open(filename, "w") as file:
                file.write(f"{user_name}\n{pass_word}\n")
            print("Successfully registered")
            break

    while True:
        print ("Would you like a hint if you forget your password?")
        question = input("Yes(y)\nNo(n)\n")
        if question.lower() == "y" or question.lower() == "yes":
            hint_question=input("What would you like your safety question to be ? (Favorite food, fathers name etc.)\n")
            hint_answer=input("Safety question answer: ")
            with open(filename,"a") as file:
                file.write(f"{hint_question}\n{hint_answer}")
            print(f"Successfully set - {hint_question} - as your safety question ")
            print(f"Answer to your question : {hint_answer}")
            print("Thank you for your registration!")
            break
        elif question.lower() == "n" or question.lower() == "no":
            print("Thank you for your registration!")
            break
        else:
            print("incorrect answer ")


if __name__ == "__main__":
    registracia()
