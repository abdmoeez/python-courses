from itertools import product

a = [1,2]
b= [3,4]
c=[3]

prod = product(a,b)
prod2 = product(a,c, repeat =2)
print(list(prod))
print(list(prod2))