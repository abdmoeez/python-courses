import random

def mac_gen():
    macaddress = ""
    charset = "1234567890abcdef"
    count=0

    for i in range(1,12+1):
        macaddress = macaddress + random.choice(charset)
        count = count+1
        if count ==2 and i < 12:
            macaddress = macaddress + "-"
            count = 0
    return macaddress

mac = mac_gen()
print(mac)

#or print(mac[:-1]) can be used if "-" displays as the last character and "and" condition is not used in the loop