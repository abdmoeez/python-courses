from collections import namedtuple

Point = namedtuple('Point','x,y') #this will create class point with x,y arhguments
pt= Point(1,-4)

print(pt.x,pt.y)