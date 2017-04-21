# -*- coding: utf-8 -*-

a = int(input('Ведіть число = '))

for i in range(2,a//2+1):
    if not a%i and float(a)/i == float(a)//i:
        print "Складне число, ділиться на = {}".format(i)
        break
else:
    print "Просте число"