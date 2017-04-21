# -*- coding: utf-8 -*-
import math

# точність обчилень
e = 1E-5
# нижня межа обчислень
a = 0.05
# вехня межа обчислень
b = 0.9
# заданий крок
h = 0.1

# шаблон таблиці
template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
# призначаємо ітератору перше значення

tabletitle = "|{:_^15}|{:_^15}|{:_^15}|{:_^15}|".format("x", "S", "y", "Pohubka")
count = tabletitle.__len__()
print "1. y = 2*x/((1-x)**3)"
print "ˍ"*count
print tabletitle
x = a

while x < b:
    # перший ітератор в S
    k = 1
    s = k*(k + 1)*x**k
    S = s

    # ітератор поки точніть не буде заданому
    while s > e:
        k += 1
        s = k*(k+1)*x**k
        S += s

    # обрахунок без циклу
    y = 2*x/((1-x)**3)

    # похибка
    p = math.fabs(((S-y)/y))*100
    print template.format(x, S, y, p)
    x += h

print "ˉ"*count

def my_fakt(x):
    if x < 2:
        return 1
    else:
        return x*my_fakt(x-1)


print "2. y = (x-1)*exp(x)+1"
print "ˍ"*count
print tabletitle
x = a

while x < b:
    # перший ітератор в S
    k = 1.
    s = 1./(my_fakt(k)*(k+2.))*x**(k+2.)
    S = s

    # ітератор поки точніть не буде заданому
    while s > e:
        k += 1
        s = 1./(my_fakt(k)*(k+2.))*x**(k+2.)
        S += s

    # обрахунок без циклу
    y = (x-1)*math.exp(x)+1

    # похибка
    p = math.fabs(((S-y)/y))*100
    print template.format(x, S, y, p)
    x += h

print "ˉ"*count