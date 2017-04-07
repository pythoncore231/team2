"""hw04_math"""
import math

e = 1E-5  # 10**-5

a = 0.05
b = 0.9
h = 0.05

TEMPLATE = "|{:12.5f}\t|{:12.5f}\t|{:12.5f}\t|{:12.5f}\t|"

print "-" * 65
print "|\tx\t|\tS\t|\ty\t|\tp\t|"
print "-" * 65

x = a

while x < b:
    k = 1
    s = k * (k + 1) * x**k
    S = s
    while s > e:
        k += 1
        s = k * (k + 1) * x**k
        S += s
    y = 2 * x / ((1 - x)**3)
    p = math.fabs(((S - y) / y) * 100)

    
    print TEMPLATE.format(x, S, y, p)

    x += h

print "-" * 65
