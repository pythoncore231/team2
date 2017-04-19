# -*- coding: utf-8 -*-

a = input('Ведіть a = ')
b = input('Ведіть b = ')
c = input('Ведіть c = ')
Diskrim = b**2 - 4 * a * c

if Diskrim < 0:
    print ("Немає дійсного кореня!")
elif Diskrim == 0:
    x = (-b + Diskrim**(1./2))/(2.*a)
    print ("Корень: x = {}".format(x))
else:
    x1 = (-b + Diskrim**(1. / 2)) / (2. * a)
    x2 = (-b - Diskrim**(1. / 2)) / (2. * a)
    print ("Корені: x1 = {}\tx2 = {}".format(x1,x2))