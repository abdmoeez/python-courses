import numpy as np

a = np.random.rand(3) #create array with 3 values
#a = np.random.rand(3,3) This would create a 3x3 array 
#a = np.random.randint(0,10,3)  random integers from 1-9 10 is excluded (3 is the size of the array)
print(a)

b= np.random.randint(0,10, (3,4)) # this creates 3x4 array

#shuffles am array of numpy
arr = np.array([[1,2,3], [4,5,6], [7,8,9]])
print(arr)
np.random.shuffle(arr)
print(arr)