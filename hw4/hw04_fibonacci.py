# This Python file uses the following encoding: utf-8
# Fibonacci series up to n

# while True:
#     try:
#         n = int(raw_input("До якого числа будуємо ряд Фібоначчі?\n"))
#         break
#     except ValueError:
#         print("Спробуйте ще раз")

while True:
    try:
        n = int(raw_input("Якої довжини має бути ряд Фібоначчі?\n"))
        break
    except ValueError:
        print("Спробуйте ще раз")
i = 0
a, b = 0, 1
while i < n:
    print "{}-> {}".format(i+1, a)
    i += 1
    a, b = b, a + b
