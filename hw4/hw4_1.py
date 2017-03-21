a = int(raw_input("enter number from 1 to 36:  "))
for i in range (1000, 10000):
    string = str(i)
    summ = 0
    for char in string:
        summ += int(char)
    if summ == a:
        print "summ of digits in", i, "=", a

