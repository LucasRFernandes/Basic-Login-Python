# Importing time module to use sleep function in my code
import time
import level_1

# Here we have some default login, I know this is not a secure aproach for this, but this does not have the intention of being a secure app, just a working app.
global username,password
username = "admin" #
password = "password" 


# This is the central menu of the aplication where you can do all the app lets you do.
def menu():
    
    global username,password
    print("Welcome To the app, here you can store your personal data \n")
    menuchoice = int(input("What do you want to do? \n See my login info (1) \n Change my login info (2) \n return to login (3) \n App credits (4) \n"))
    if menuchoice == int("1"):
        print("Your Username is:", username)
        print("Your password is:", password)
        print("Sending you back to the menu \n \n")
        time.sleep(3)
        menu()
    if menuchoice == int("2"):
        username = input("What will your new username be?: ")
        password = input("What will your new password be?: ")
        print("Changes done, new username and password are,", username, password)
        print("Sending you back to the menu")
        time.sleep(3)
        menu()
    if menuchoice == int("3"):
        print("\n")
        login()
    if menuchoice == int("4"):
        print("Hi, I'm Lucas Rocha Fernandes, I'm a 19 years old programmer and the person who")
        print("developed this app, it was made using python 3.10, probably when you read this")
        print("there will be a new version of this same app avaible, one much more secure and")
        print("fast, and it will have a data base in SQL, so you will be able to store different")
        print("logins, so, thats bassicaly it, you can contact me through my email \n Lucasrochafernandes20@gmail.com")
        print("Or trough my Instagram \n @Bemol_Luxca \n \n \n ")
        input("Press any key to return to menu \n")
        menu()

        
        pass
    
# This is the login system
def login():
        global username,password
        First_check = input("Do you have an account? Y/N = ")
        if First_check == "Y":
            check_1 = input("Username: ")
            check_2 = input("Password: ")
            if check_1 == username:
                if check_2 == password:
                    print("The Username and the password are correct")
                    input("Continue to the menu?")
                    menu()
                else:
                    print("your credentials are incorrect")
                    input("Wait")
                    
            else:
                    print("There is no matching username")
                    print(username)
                    print(password)
                    input("Wait") 
        else:
            Second_Check = input("Do you want to register? Y/N = ")
            if Second_Check == "Y":
                username = input("What will your username be? = ")
                password = input("What will your password be? = ")
                print("Data Saved") 
                input("Press any key to return to login")
                login()
            else:
                input("Press any key to close")
        return


login()
