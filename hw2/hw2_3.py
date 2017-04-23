from math import atan, sin, cos, tan, exp, pi, factorial, log
x = int(raw_input("input x-number: "))
y = int(raw_input("input y-number: "))
z = int(raw_input("input z-number: "))

a1 = (abs(x-1)**0.5-abs(y)**(1/3))/(1+((x**2)/2)+((y**2)/4))
b1 = x*(atan(z)+exp(-x-3))
print "task a:"
print "a=", a1
print "b=", b1

a2 = (3+exp(y-1))/(1+((x**2)*abs(y-tan(z))))
b2 = 1+abs(y-x)+(((y-x)**2)/2)+(((abs(y-x))**3))/3
print "task b:"
print "a=", a2
print "b=", b2

a3 = (1+y)*((x+(y/((x**2)+4)))/(exp(-x-2)+(1/((x**2)+4))))
b3 = (1+cos(y-2))/(((x**4)/2)+(sin(z))**2)
print "task c:"
print "a=", a3
print "b=", b3

a4 = y+(x/((y**2)+abs(((x**2)/(y+((x**3)/3))))))
b4 = 1+((tan(z/2))**2)
print "task d:"
print "a=", a4
print "b=", b4

a5 = 2*(cos(x-(pi/6)))/(0.5+((sin(y))**2))
b5 = 1+((z**2)/(3+((z**2)/5)))
print "task e:"
print "a=", a5
print "b=", b5

a6 = x+((1+((sin(x+y))**2))/(2+abs(x-((2*x)/(1+((x**2)*(y**2)))))))
b6 = (cos(atan(1/z)))**2
print "task f:"
print "a=", a6
print "b=", b6

a7 = log(abs((y-((abs(x))**0.5)*(x-(y/(z+(x*x/4)))))))
b7 = x-(((x*x)/factorial(3))+((x**5)/factorial(5)))
print "task g:"
print "a=", a7
print "b=", b7