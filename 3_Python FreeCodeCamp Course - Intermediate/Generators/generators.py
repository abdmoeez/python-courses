

def mygenerator():
    yield 3
    yield 2
    yield 1

g = mygenerator()

for i in g:
    print(i)

print(sum(g))
print(sorted(g))
