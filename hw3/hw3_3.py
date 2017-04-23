print "a*x*x+b*x+c=0, let`s find x:"
a = int(raw_input("enter a:  "))
b = int(raw_input("enter b:  "))
c = int(raw_input("enter c:  "))

d = (b**2)-(4*a*c)
x = (-b+(((b*b)-(4*a))**0.5))/(2*a)

if d >= 0:
    print "x = ", x
else:
    print "no results"
