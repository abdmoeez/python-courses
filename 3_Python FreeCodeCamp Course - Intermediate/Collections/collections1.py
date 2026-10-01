from collections import Counter

a = "aaaaabbbbccc"

my_counter = Counter(a)

print(my_counter)

print(my_counter.most_common())
print(my_counter.most_common(2))