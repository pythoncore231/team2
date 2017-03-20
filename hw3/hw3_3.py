a = int(raw_input("a:  "))
b = int(raw_input("b:  "))
c = int(raw_input("c:  "))

d = (b**2)-(4*a*c)
x = (-b+(((b*b)-(4*a))**0.5))/(2*a)

if d >= 0:
    print x
else:
    print "no results"
