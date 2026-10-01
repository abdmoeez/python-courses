from itertools import accumulate
import operator


a= [1,2,3,4]

acc= accumulate(a, func=operator.mul) #As fuction is now mul so it will multiply all the elements with the past result
print(a)
print(list(acc))

#basically summing all the past values