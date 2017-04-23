
str = raw_input("enter integer number:  ")
n = len(str)
summ = 0
for i in range(0, n):
    summ += (int(str[i]))**3

print "summ of digits cubs =", summ


