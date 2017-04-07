# -*- coding: utf-8 -*-
# ax2+bx+c=0
# enter a,b,c
# out sqrt(x)
import cmath

print "Введіть кофіцієнти квадратичного рівняння ax^2+bx+c=0"
a = int(raw_input("a = "))
b = int(raw_input("b = "))
c = int(raw_input("c = "))

D = (b**2) - (4 * a * c)  # дискримінант

if D > 0:
    x_1 = (-b + D**0.5) / (2 * a)
    x_2 = (-b - D**0.5) / (2 * a)
    print "чудово, в нас буде 2 дійсних рішення:", x_1, x_2
elif D == 0:
    x_1 = (-b + D**0.5) / (2 * a)
    print "в нас буде 2 однакових дійсних рішення:", x_1
else:
    x_1 = (-b + cmath.sqrt(D)) / (2 * a)
    x_2 = (-b - cmath.sqrt(D)) / (2 * a)
    print "нажаль, існують тільки комплексні рішення:", x_1, x_2
