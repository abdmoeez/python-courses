#Unpacking tuples
my_tuple = "Max",28,"Boston"

name, age, city = my_tuple
print(name)
print(age)
print(city)

############

mytuple = (0,1,2,3,4)

i1, *i2, i3 = mytuple #i1 = first item, i3= last item , *i2 = all elements in between first and last stored as a list
print(i2) 