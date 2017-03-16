# -*- coding: utf-8 -*-

# Дано чотирицифрове  натуральне число.  Знайти добуток цифр цього числа.
number = int(raw_input("Please enter the four-digit integer: "))

# receiving numbers by using the math operations
number1 = number // 1000
number2 = number // 100 - number1 * 10
number3 = number // 10 - number2 * 10 - number1 * 100
number4 = number - number3 * 10 - number2 * 100 - number1 * 1000
numberMul = number1 * number2 * number3 * number4
print "First Multiplication: ", numberMul

Number = int(raw_input("Please enter the four-digit integer again: "))
# receiving numbers by using the string options
str1 = str(Number)
print str1
NumberMul = int(str1[0]) * int(str1[1]) * int(str1[2]) * int(str1[3])
print "Second Multiplication: ", NumberMul

# Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
numberMul, NumberMul = NumberMul, numberMul
print "First Multiplication: ", numberMul
print "Second Multiplication: ", NumberMul
