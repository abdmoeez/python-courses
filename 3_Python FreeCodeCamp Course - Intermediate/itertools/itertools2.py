from itertools import permutations

a = [1,2,3]

perm = permutations(a)
perm2 = permutations(a, 2) #2 is length here
print(list(perm))
print(list(perm2))