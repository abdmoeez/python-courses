import sys
import timeit

my_list= [0,1,2,"Hello", True]
my_tuple = (0,1,2,"Hello", True)

print(sys.getsizeof(my_list), "Bytes")
print(sys.getsizeof(my_tuple), "Bytes") 

###############

print(timeit.timeit(stmt="[0,1,2,3,4,5]", number=1000000))
print(timeit.timeit(stmt="(0,1,2,3,4,5)", number=1000000))

#timeit creates the stmt(statement) list or tuples for number of times which is 1 millionn here and tells how much time it took to create