
from math import sqrt
print "is it triangle?"
a = int(raw_input("enter lenght a:  "))
b = int(raw_input("enter lenght b:  "))
c = int(raw_input("enter lenght c:  "))

if c < (a + b) and b < (a + c) and a < (b + c):
    p = (a + b + c) / 2
    s = sqrt(p*(p-a)*(p-b)*(p-c))
    print "perimeter: ", p
    print "square:  ", s
else:
    print "try again"
