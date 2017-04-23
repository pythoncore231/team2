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
    s = ((2*k)+1)*(x**k)
    S = s
    while s > e:
        k += 1
        s = ((2*k)+1)*(x**k)
        S += s
    y = (1+x)/((1-x)**2)
    p = math.fabs((S-y)/y)*100
    print template.format(x, S, y, p)

    x += h

