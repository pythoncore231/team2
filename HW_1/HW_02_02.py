# -*- coding: utf-8 -*-
import math

n = input('a = ')
mult = 1
summa = 0
while n > 0:
    if n % 10 != 0:
        mult = mult * (n % 10)
    summa = summa + n % 10
    n = n // 10

print ("Сума = {}".format(summa))
print ("Добуток = {}".format(mult))

a1 = 14
a2 = 52
print ("{}, {}".format(a1,a2))
a1,a2 = a2,a1
print ("{}, {}".format(a1,a2))

a = 45
b = 61
print ("{}, {}".format(a,b))
a = a + b
b = a - b
a = a - b
print ("{}, {}".format(a,b))

x = float(input('x = '))
y = float(input('y = '))
z = float(input('z = '))

a = (math.fabs(x-1.)**(1./2)-math.fabs(y)**(1./3))/(1.+x**2/2+y**2/4)
b = x*(math.atan(z)) + math.exp(-(x+3.))
print "A) a){:11.5f}\tb){:11.5f}".format(a,b)

a = (3 + math.exp(y-1.))/(1+x**2*math.fabs(y - math.tan(z)))
b = 1 + math.fabs(y - x) + (y - x)**2/2 + math.fabs(y - x)**3/3
print "Б) a){:11.5f}\tb){:11.5f}".format(a,b)

a = (1 + y)*(x + y/(x**2 + 4))/(math.exp(-x-2.)+ 1./(x**2+4))
b = (1 + math.cos(y - 2.))/(x**4/2. + math.sin(z)**2)
print "В) a){:11.5f}\tb){:11.5f}".format(a,b)

a = y + x/(y**2 + math.fabs(x**2/(y+x**3/3.)))
b = 1 + math.tan(z/2)**2
print "Г) a){:11.5f}\tb){:11.5f}".format(a,b)

a = 2.*math.cos(x - math.pi/6)/(1./2 + math.sin(y)**2)
b = 1 + z**2/(3 + z**2./5)
print "Д) a){:11.5f}\tb){:11.5f}".format(a,b)

a = (1+math.sin(x+y)**2)/(2+math.fabs(x-2*x/(1+x**2*y**2)))+x
b = math.cos(math.atan(1./z))**2
print "Е) a){:11.5f}\tb){:11.5f}".format(a,b)

a = math.log10((y - math.fabs(x)**(1./2))*(x - y/(z + x**2/4)))
b = x - x**2./math.factorial(3) + x**5/math.factorial(5)
print "Ж) a){:11.5f}\tb){:11.5f}".format(a,b)