# This Python file uses the following encoding: utf-8

"""calculating sum of cubes of every digit from entered number"""

while True:
    try:
        n = int(raw_input("Введіть число, а я порахую суму кубів його цифр \n"))
        break
    except ValueError:
        print("Спробуйте ще раз\n\n")

l = [int(i) for i in str(n)]

sum_of_cubes = 0
i = 0
#print l

for i in range(len(l)):
    sum_of_cubes += l[i-1]**3

print sum_of_cubes