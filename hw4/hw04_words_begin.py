# This Python file uses the following encoding: utf-8
"""вивести всі слова, що починаються із введеного рядка"""

import requests

while True:
    try:
        sub = raw_input("Введіть стрічку які потрібно знайти \n")
        break
    except ValueError:
        print("Спробуйте ще раз")

txt = requests.get('http://www.ietf.org/rfc/rfc3092.txt')

txt = txt.text

lstxt = txt.split(' ')

for i in range(len(lstxt)):
    if sub in lstxt[i]:
        print lstxt[i]