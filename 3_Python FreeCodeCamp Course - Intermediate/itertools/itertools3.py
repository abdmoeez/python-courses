from itertools import combinations, combinations_with_replacement

a = [1,2,3,4]

comb = combinations(a, 2) #2 is length and putting length is mandatory

print(list(comb))

comb_wr = combinations_with_replacement(a,2)

print(list(comb_wr))