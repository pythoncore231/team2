#! /usr/bin/env python
# -*- coding: utf-8 -*-

"""hw2_04"""
import math


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


x = 10
y = 100
z = 1000

print bcolors.BOLD + "x = ", x
print "y = ", y
print "z = ", z
print bcolors.ENDC

a = (math.fabs(x - 1)**.5 - (math.fabs(y))**(1 / 3.)) / 1 + x**2 / 2 + y**2 / 4
b = x * (math.atan(z) + math.exp(-(x + 3)))

print bcolors.OKGREEN
print "a)", "a = ", a, "\tb = ", b

a = (3 + math.exp(y - 1)) / 1 + x**2 * math.fabs(y - math.tan(z))
b = 1 + math.fabs(y - x) + (y - x)**2 / 2 + math.fabs(y - x)**3 / 3

print "б)", "a = ", a, "\tb = ", b

a = (1 + y) * ((x + y) / ((x**2 + 4)) / math.exp(-(x - 2)) + 1 / (x**2 + 4))
b = 1 + math.cos(y - 2) / x**4 / 2 + math.sin(z)**2

print "в)", "a = ", a, "\tb = ", b

a = y + x / (y**2 + math.fabs(x**2 / y + x**3 / 3))
b = 1 + math.tan(z / 2)**2

print "г)", "a = ", a, "\tb = ", b

a = (2 * math.cos(x - math.pi / 6)) / (1 / 2 + math.sin(y)**2)
b = 1 + ((z**2) / (3 + z**2 / 5))

print "д)", "a = ", a, "\tb = ", b

a = 1 + math.sin(x + y)**2 / 2 + math.fabs(x - 2 * x / (1 + x**2 * y**2)) + x
b = math.cos(math.atan(1 / z))**2

print "е)", "a = ", a, "\tb = ", b

a = math.log((y - math.fabs(x)**0.5) * (x - (y / (z + x**2 / 4))))
b = x - x**2 / 6 + x**5 / math.factorial(5)

print "ж)", "a = ", a, "\tb = ", b

print bcolors.ENDC
