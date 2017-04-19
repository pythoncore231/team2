# -*- coding: utf-8 -*-

a = input('Ведіть a = ')
b = input('Ведіть b = ')
c = input('Ведіть c = ')

if not (a < b + c and b < a + c and c < b + a):
    print ("Невийде трикутник!")
else:
    P = a + b + c
    S = (P/2.*(P/2. - a)*(P/2. - b)*(P/2. - c))**0.5
    print ("Периметр {}\tПлоща {}".format(P, S))