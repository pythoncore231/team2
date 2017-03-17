# -*- coding: UTF-8 -*-
"""this some modiule"""
#make product of digits from etered 4 symbol string
import re

four_digits_in = raw_input("Введіть чотиризначне число: ")

if not re.match("^[1-9]{1,4}$", four_digits_in):
    print "Тільки чотиризначні числа буль-ласка :)"
else:
    print "Добуток цифр у вашому числі:", int(four_digits_in[0])*int(four_digits_in[1])*int(four_digits_in[2])*int(four_digits_in[3]) #супер дебільно
