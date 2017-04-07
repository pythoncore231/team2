# This Python file uses the following encoding: utf-8
# Решето Ератосфена

while True:
    try:
        n = int(raw_input("Введіть число \n"))
        break
    except ValueError:
        print("Мабуть це не число, \nСпробуйте ще раз")

l = [int(i) for i in str(n)] 

for i in len(l)+1:
    