import secrets

a= secrets.randbelow(10) #random integer 1-9 10 is not included
print(a)

b= secrets.randbits(4)
print(b)

mylist = list("ABCDEFGH")
c= secrets.choice(mylist)
print(c)