def isPrime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n

for number in range(1, 1000):
    if isPrime(number):
        print "Number %d is prime" % number
    else:
        print "Number %d is not prime" % number