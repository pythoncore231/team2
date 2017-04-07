# # This Python file uses the following encoding: utf-8
# import math

while True:
    try:
        n = int(raw_input("Введіть число \n"))
        break
    except ValueError:
        print("Спробуйте ще раз")

l = [0, 0, 0, 0]

#output all possible combinations of 4 digits, sum of which eq entered number


for i in range(10):
    for j in range(4):
        l[j] = i
        if n == l[0]+l[1]+l[2]+l[3]:
            print l
            break