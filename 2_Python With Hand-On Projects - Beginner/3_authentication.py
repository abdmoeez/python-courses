username = "root"
password = "admin"

name = input("Enter the username : ")
passwrd = input("Enter Password: ")

if name == username and password == passwrd:
    print("Authentication Successful!")
else:
    print("Wrong Username or Password")