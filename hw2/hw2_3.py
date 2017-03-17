from math import atan, sin, cos, tan, exp, pi, factorial, log
x = 1
y = 2
z = 3

a = (abs(x-1)**0.5-abs(y)**(1/3))/(1+((x**2)/2)+((y**2)/4))
print a

b = x*(atan(z)+exp(-x-3))
print b

a = (3+exp(y-1))/(1+((x**2)*abs(y-tan(z))))
b = 1+abs(y-x)+(((y-x)**2)/2)+(((abs(y-x))**3))/3

print a
print b

a = (1+y)*((x+(y/((x**2)+4)))/(exp(-x-2)+(1/((x**2)+4))))
b = (1+cos(y-2))/(((x**4)/2)+(sin(z))**2)

print a
print b

a = y+(x/((y**2)+abs(((x**2)/(y+((x**3)/3))))))
b = 1+((tan(z/2))**2)

print a
print b

a = 2*(cos(x-(pi/6)))/(0.5+((sin(y))**2))
b = 1+((z**2)/(3+((z**2)/5)))

print a
print b

a = x+((1+((sin(x+y))**2))/(2+abs(x-((2*x)/(1+((x**2)*(y**2)))))))
b = (cos(atan(1/z)))**2

print a
print b

a = log(abs((y-((abs(x))**0.5)*(x-(y/(z+(x*x/4)))))))
b = x-(((x*x)/factorial(3))+((x**5)/factorial(5)))

print a
print b