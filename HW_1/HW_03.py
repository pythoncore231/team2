# -*- coding: utf-8 -*-
#
# year = input('Ведіть рік = ')
#
# if 1930 > year or year > 2070:
#     print ("Неправильний рік!")
#
# if(year%4):
#     print ("This is not a leap year!")
# else:
#     print ("It's a leap year!")
#
# month = input('Ведіть місяць = ')
# if 1 > month or month > 12:
#     print ("Неправильний місяць!")
#
# day = input('Ведіть день = ')
# if 1 > day or day > 31:
#     print ("Неправильний день!")
#
# if 28 < day and day < 32:
#         print ("Хто його знає!")
#
# a = input('Ведіть a = ')
# b = input('Ведіть b = ')
# c = input('Ведіть c = ')
# Diskrim = b**2 - 4 * a * c
#
# if Diskrim < 0:
#     print ("Немає дійсного кореня!")
# elif Diskrim == 0:
#     x = (-b + Diskrim**(1./2))/(2.*a)
#     #x2 = (-b - Diskrim**(1./2))/(2.*a)
#     print ("Корень: x = {}".format(x))
# else:
#     x1 = (-b + Diskrim**(1. / 2)) / (2. * a)
#     x2 = (-b - Diskrim**(1. / 2)) / (2. * a)
#     print ("Корені: x1 = {}\tx2 = {}".format(x1,x2))


a = input('Ведіть a = ')
b = input('Ведіть b = ')
c = input('Ведіть c = ')
l = [a, b, c]
l.sort()

if not (l[2]<l[1]+l[0] and l[1]<l[2]+l[0] and l[0]<l[2]+l[1]):
    print ("Невийде трикутник!")
else:
    P = l[2]+l[1]+l[0]
    S = (P/2.*(P/2.-l[2])*(P/2.-l[1])*(P/2.-l[0]))**0.5
    print ("Периметр {}\tПлоща {}".format(P, S))