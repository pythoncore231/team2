import math
x = int(raw_input("Please enter x: "))
y = int(raw_input("Please enter y: "))
z = int(raw_input("Please enter z: "))

# a)
a = ((((math.fabs(x-1))**1/2)-((math.fabs(y))**1/3))/(1+((x**2)/2)+(y**2)/4))
b = x*(math.atan(z)+math.exp(-(x+3)))
print "a):"
print a
print b

# b)
a = (3 + math.exp(y - 1)) / (1 + (x**2) * math.fabs(y - math.tan(z)))
b = 1 + math.fabs(y - x) + ((y - x)**2)/2 + ((math.fabs(y - x))**3)/3
print "b):"
print a
print b

# v)
a = (1 + y) * (((x + y / (x**2 + 4))) / (math.exp(-x - 2) + (1 / (x**2 + 4))))
b = (a + math.cos(y - 2)) / (x**4/(2 + (math.sin(z))**2))
print "v):"
print a
print b

# h)
a = y + (x/(y**2 + math.fabs(x**2/(y + (x**3)/3))))
b = (1 + (math.tan(z/2))**2)
print "h):"
print a
print b

# d)
a = (2*math.cos(x-math.pi/6))/(1/2 + (math.sin(y))**2)
b = 1 + (z**2/(3 + (z**2)/5))
print "d):"
print a
print b

# e)
a = (1 + (math.sin(x+y))**2)/(2 + math.fabs(x - (2*x)/(1 + (x**2)*(y**2)))) + x
b = (math.cos(math.atan(1/z)))**2
print "e):"
print a
print b

# g)
a = math.log1p((y - (math.fabs(x))**1/2)*(x - (y/(z+(x**2)/4))))
b = x - x**2/(math.factorial(3)) + x**5/(math.factorial(5))
print "g):"
print a
print b
