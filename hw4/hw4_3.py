def fib(n):
    a = 0
    b = 1
    for i in range(n):
        a, b = b, a + b
    return a

max_range = int(raw_input("max fibo: "))

for i in range(0, max_range):
    print "Fibo number %d, for %d" % (fib(i), i)
