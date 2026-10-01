import random

a= random.randint(1,10) #include upperbound
print(a)

b = random.randrange(1,10) # dosent include upperbound
print(b)


mylist = list("ABCDEFGH")

c=  random.choice(mylist)
print(c)

d= random.sample(mylist,3) #picks three characters from list but dosent pick a single twice
print(d)

e= random.choices(mylist, k=3) #picks three but can pick single element multiple times
print(e)

random.shuffle(mylist)
print(mylist)