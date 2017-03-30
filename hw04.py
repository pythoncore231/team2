# -*- coding: utf-8 -*-
import math
# 1
"""
Знайти всі чотирьохзначні числа, сума цифер яких рівна заданому числу.
"""
# number = int(raw_input("Enter the number:"))
# index = 0
# if number == 36:
#     print "9999"
# else:
#     for i in range(1000, 9999):
#         istr = str(i)
#         if number == int(istr[0]) + int(istr[1]) + int(istr[2]) + int(istr[3]):
#             print i,
#             index += 1
#     if not index:
#         print "No numbers for current value. 36 is max."

number = int(raw_input("Enter the number:"))

numbers = [i for i in range(1000, 10000) if number == sum( int(j) for j in str(i) )]

if numbers:
    print numbers
else:
    print "No numbers for current value. 36 is max."
# *************************************************************************************

# 2
"""
Задано число, перевірити чи дане число являється простим числом.
"""
# number = int(raw_input("Please enter number: "))
# if number == 1 or number == 2:
#     print "This is prime number"
# else:
#     for i in range(3, number/2):
#         if (number % i) == 0:
#             print "This is not prime number"
#             break
#     else:
#         print "This is prime number"

number = int(raw_input("Please enter number: "))
if number == 1 or number == 2:
    print "This is prime number"
else:
    prime = [i for i in range(3, number/2+1) if (number % i) == 0]
    if prime:
        print "This is not prime number"
    else:
        print "This is prime number"
# *************************************************************************************

# 3
"""
Задано ціле число N, вивести перші N чисел фібоначі.
"""
number = int(raw_input("Please enter number: "))
fibs = [1, 1]
k = 1
while k < number:
    fibs.append(fibs[-2] + fibs[-1])
    k += 1
print(fibs),
# *************************************************************************************

# 4
"""
Знайти суму кубів цифер заданого натурального числа.
"""
# number = int(raw_input("Please enter number: "))
# str1 = str(number)
# Sum = 0
# for i in range(len(str1)):
#     Sum += int(str1[i])**3
# print "Sum of the cubes: ", Sum

number = int(raw_input("Please enter number: "))
str1 = str(number)
Sum = 0
Sum = sum( int(str1[i])**3 for i in range(len(str1)) )
print "Sum of the cubes: ", Sum
# *************************************************************************************

# 5
"""
Заданий текст, вивести всі слова які починаються на певну послідовність символів.
"""
# str1 = "tast test testas teest tust"
# sub_str = "te"
# list_str = str1.split()
# for i in range(len(list_str)):
#     if list_str[i].startswith(sub_str):
#         print list_str[i],

str1 = "tast test testas teest tust"
sub_str = "te"
list_str = str1.split()
list1 = [list_str[i]  for i in range(len(list_str)) if list_str[i].startswith(sub_str)]
print list1

# *************************************************************************************

# 6

e = 1E-5  # 10**-5
a = 0.05
b = 0.9
h = 0.05
# template = "| {} | {} | {} | {} |"
template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
print "|\t\tx\t\t|\t\tS\t\t|\t\ty\t\t|\t\tp\t\t|"
print "-"*65
# **************************************

# # #1

x = a
while x < b:
    k = 1
    s = k*(k+1)*x**k
    S = s
    while s > e:
        k += 1
        s = k*(k+1)*x**k
        S += s
    y = 2*x/((1-x)**3)
    p = math.fabs(((S-y)/y))*100
    print template.format(x, S, y, p)
    x += h
print "-"*65
# **************************************

# # #2

e = 1E-5
a = 0.05
b = 0.9
h = 0.05
x = a
while x < b:
    k = 0
    s = (x**(k+2))/(math.factorial(k)*(k+2))
    S = s
    while s > e:
        k += 1
        s =  (x**(k+2))/(math.factorial(k)*(k+2))
        S += s
    y = ((x-1)*math.exp(x))+1
    p = math.fabs(((S-y)/y))*100
    print template.format(x, S, y, p)
    x += h
print "-"*65
# **************************************

# # #3
e = 1E-5
a = 0.05
b = 0.9
h = 0.05
x = a
while x < b:
    n = 1
    s = n*(n+2)*(x**n)
    S = s
    while s > e:
        n += 1
        s = n*(n+2)*(x**n)
        S += s
    y = (x*(3-x))/((1-x)**3)
    p = math.fabs(((S-y)/y))*100
    print template.format(x, S, y, p)
    x += h
print "-"*65
# **************************************

# # #4 Not done yet!
# **************************************

# #5
e = 1E-5
a = 0.05
b = 0.9
h = 0.05
x = a
while x < b:
    k = 0
    m = 0
    s = (1+m)*(x**k)
    S = s
    while s > e:
        k += 1
        m += 2
        s = (1+m)*(x**k)
        S += s
    y = (1+x)/((1-x)**2)
    p = math.fabs(((S-y)/y))*100
    print template.format(x, S, y, p)
    x += h
print "-"*65

