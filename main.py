#pip install bcrypt
import bcrypt

username = input("Enter your username please: ")
usernamehash = bcrypt.hashpw(username.encode(), bcrypt.gensalt())

password = input("Enter pass: ")

if username == password:
    print("Error! Username and password is same!")
    exit()

passwordchech = input("Enter pass again: ")


if password != passwordchech:
    print("Password isn't same!")
    exit()
else:
    firsthash = bcrypt.hashpw(password.encode(), bcrypt.gensalt())
    print("Well done, you successfully registered!")