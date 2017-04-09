# This Python file uses the following encoding: utf-8
# Решето Ератосфена
"""
#1 Якщо потрібно знайти всі прості числа менші за певне число N, виписуються всі числа від 1 до N.
#2 Перше просте число - два.
#3 Викреслимо всі числа більші двох, які діляться на два (4, 6, 8 …).
#4 Наступне число, яке залишилося незакресленим (три), є простим. Викреслюємо всі числа більші трьох та кратні трьом (6, 9 …).
#5 Наступне незакреслене число (п'ять) є простим. Викреслимо всі числа більші п'яти та кратні п'яти (10, 15, 20, 25 …).
#6 Повторюємо операцію поки не буде досягнуто число N:
    Наступне незакреслене число є простим. Викреслимо всі числа більші нього та кратні йому.
Числа, які залишилися незакресленими після цієї процедури - прості
"""
while True:
    try:
        limit = int(raw_input("Введіть число \n"))
        break
    except ValueError:
        print("Мабуть це не число, \nСпробуйте ще раз")

# ls_primes = []

# for i in range(2, int(limit**0.5)):
#     for j in range(i*2, limit, i):
#         list_primes[j] = False

# list_primes = [i for i in range(2, limit) if list_primes[i]]

ls_not_primes = [j for i in range(2, limit) for j in range(i*2, limit, i)]
ls_primes = [x for x in range(2, limit) if x not in ls_not_primes]

print ls_primes
print len(ls_primes)
