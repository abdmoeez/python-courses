setA = {1,2,3,4,5,6,7,8,9}
setB = {1,2,3,10,11,12}

diff = setA.difference(setB)
print(diff)

symdiff = setA.symmetric_difference(setB) #All elements which are not common in both sets
print(symdiff)