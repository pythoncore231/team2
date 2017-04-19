# -*- coding: utf-8 -*-

year = input('Ведіть рік = ')

if 1930 > year or year > 2070:
    print ("Неправильний рік!")

month = input('Ведіть місяць = ')
if 1 > month or month > 12:
    print ("Неправильний місяць!")

day = input('Ведіть день = ')
if 1 > day or day > 31:
    print ("Неправильний день!")

if 28 < day and day < 32:
        print ("Хто його знає!")