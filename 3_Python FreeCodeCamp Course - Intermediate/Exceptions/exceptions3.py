class valuetoohigh(Exception):
    pass

def testvalue(x):
    if x>100:
        raise valuetoohigh("Value is too high")

try:
    testvalue(300)
except valuetoohigh as e:
    print(e)