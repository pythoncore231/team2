import math
e = 1E-5
a = 0.05
b = 0.9
h = 0.1
template = "|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|{:11.5f}\t|"
print "|\t\tx\t\t|\t\tS\t\t|\t\ty\t\t|\t\tp\t\t|"
print "-"*65

x = a
while x < b:
    k = 0
    s = (x**(k+2))/((math.factorial(k))*(k+2))
    S = s
    while s > e:
        k += 1
        s = (x**(k+2))/((math.factorial(k))*(k+2))
        S += s
    y = (x-1)*((math.exp(x)))+1
    p = math.fabs((S-y)/y)*100
    print template.format(x, S, y, p)

    x += h

