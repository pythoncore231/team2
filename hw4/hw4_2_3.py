from math import factorial

n = int(raw_input("enter the number over 1:  "))
if ((factorial(n-1))+1) % n == 0:
    print n, "is prime number"
else:
    print n, "is not prime number"

n1 = 1
n2 = 1
print n1
print n2
for i in range(1, n-1):
    fib = n2 + n1
    n2 = n1
    n1 = fib
    print fib