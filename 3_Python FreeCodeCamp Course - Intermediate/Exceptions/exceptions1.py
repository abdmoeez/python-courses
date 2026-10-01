#Exception using Raise and assertion

x = -5

if x<0:
    raise Exception("x should be positive")

x= -5

assert(x==0), "x is not positive"