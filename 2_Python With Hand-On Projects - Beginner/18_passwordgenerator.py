import random

def pass_gen(plen):
    password = ""
    charset = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM1234567890_"

    for i in range(1,plen+1):
        password = password + random.choice(charset)
    return password


passlength = int(input("Enter Password Length: "))
if passlength < 8:
    print("Password must be atleast 8 characters long!")
    exit()

passgenerated = pass_gen(passlength)
print(passgenerated)