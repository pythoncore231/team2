n = input('a = ')
mult = 1
summa = 0
while n > 0:
    if n % 10 != 0:
        mult = mult * (n % 10)
    summa = summa + n % 10
    n = n // 10

print ("Suma = {}".format(summa))
print ("Dobutok = {}".format(mult))

a1 = 14
a2 = 52
print ("{}, {}".format(a1,a2))
a1,a2 = a2,a1
print ("{}, {}".format(a1,a2))

