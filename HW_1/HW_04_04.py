# -*- coding: utf-8 -*-

n = input('a = ')
mult = 1
summa = 0
while n > 0:
    if n % 10 != 0:
        mult = mult * (n % 10)
    summa = summa + (n % 10)**3
    n = n // 10

print ("Сума кубів = {}".format(summa))