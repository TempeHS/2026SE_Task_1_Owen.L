import csv
import sys

def menuinputs():

    Menu = input(" do you want to register, login or quit?")
    print (Menu)
if Menu == Login:
    def userandpasswordcheck():
            User = input("Username")
            Pswrd = input("Password")
if User != grogu:
    print('Incorrect Username')
elif Pswrd != patu:
    print("incorrect Password")
else: 
    print("Welcome In!")

if Menu == register:
    def makenewaccount():
        NewUser= input("What do you want your Username to be?")
        NewPswrd= input("What do you want your new passwor to be?")
        print(NewUser)
        if NewUser > [4]:
            print(NewPswrd)
            if NewPswrd <= [4]:
                print ("password has to be longer than 4 characters")
        else:
            print("Username And Password set")
            print("Try Logging in")
            #Save new Username and Password 


if Menu == quit:
    print("Stopping Program")