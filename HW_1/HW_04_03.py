# -*- coding: utf-8 -*-

def my_fibo(n,pri):
    if n < 3:
        if pri == 1:
            print "1"
            print "1"
        return 1
    else:

        # fibon = my_fibo(n-1,0) + my_fibo(n-2,0)
        fibon = my_fibo(n - 1, pri) + my_fibo(n - 2, 0)
        if pri == 1:
            pri -= 1
            print fibon
        return fibon

a = int(input('Ведіть число фібоначі = '))
print "Число {} фібоначі = ".format(a),
print my_fibo(a,0)
my_fibo(a,1)

# йомайо ліпше закрити то фібоначі на гайку