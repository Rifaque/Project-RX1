from math import*
import os

username1="1james"
username2="2ahmed"
username3="3raj"
password1="11234"
password2="25678"
password3="3asdf"
namein=input("Enter your username : ")
passin=input("Enter your password : ")
user="none"
void=0

if username1 == namein:
    user="James"
elif username2 == namein:
    user="Ahmed"
elif username3 == namein:
    user="Raj"
else:
    print("Username/Password incorrect")
    exit()

if password1 == passin or password2 == passin or password3 == passin:
    void=1
else:
    print("Username/Password incorrect")
    exit()

if namein[0]==passin[0]:
    is_passauth = True
else:
    print("Password incorrect")
    exit()

if is_passauth:
    print("Login Successful")

print("Hi "+user)