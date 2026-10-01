# Ordered, Immutable, allows duplicate elements
mytuple = ("max",) #for single item add an extra comma
print(type(mytuple))

#############

mytuple2 = ("max",28,"boston")
item = mytuple2[2]
print(item)

for i in mytuple2:
    print(i)

if "boston" in mytuple2:
    print("Yes")
else:
    print("No")

#############

my_tuple = ('a','p','p','l','e')
print(my_tuple.count('p'))
print(my_tuple.index('l'))

mylist = list(my_tuple) #creates a list by passing the tuple. makes a copy 
print(mylist)

################