# -*- coding: utf-8 -*-

a = input('Ведіть число = ')
kaunt = 0
iteration = 0

if 0 < a < 37:
    for i in range(1,10):
        if i > a:
            iteration += 1
            break
        elif i + 9 + 9 + 9 < a:
            iteration += 1
            continue
        else:
            for j in range(0,10):
                if i + j > a:
                    iteration += 1
                    break
                elif i + j + 9 + 9 < a:
                    iteration += 1
                    continue
                else:

                    for k in range(0,10):
                        if i + j + k > a:
                            iteration += 1
                            break
                        elif i + j + k + 9 < a:
                            iteration += 1
                            continue
                        else:
                            l = a - i - j -k
                            print "{} {} {} {}".format(i, j, k, l)
                            iteration += 1
                            kaunt += 1

if not kaunt:
    print "Бажаних чисел немає!"
else:
    print "Кількість чисел = {}".format(kaunt)

print "Кількість ітерацій = {}".format(iteration)