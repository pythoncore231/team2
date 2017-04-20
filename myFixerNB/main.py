# -*- coding: utf-8 -*-
import utils.datamanager as ud
from utils.process import print_dict_rates, exchange
BASE = ['EUR', 'USD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
        'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
        'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
        'CZK', 'BRL', 'PLN', 'PHP', 'ZAR']
date = "2017-04-13"

# date = str(raw_input("Please enter date in follow format 'yy-mm-dd': "))
# strdateto = str(raw_input("Please enter date in follow format 'yy-mm-dd': "))
# base = str(raw_input("Please enter currency: "))
# amount = (raw_input("Please enter the amount you want to exchange: ")
base = 'USD'
baseto = 'BGN', 'KRW'
amount = 100


data = ud.get_rates(date, "DKK")
print_dict_rates(data),
print '*'*100

# # вивести суму якa буде при обмінi певної суми DKK на BGN та KRW

exchange(amount, data, 'BGN', 'KRW'),
print '*'*100

# # вивести зміну курсу валют для USD за період з 20 по 27 березня 2017 року
start_date = '2017-03-20'
end_date = '2017-03-27'
base = 'EUR'

data = [i for i in ud.get_rates_by_period(start_date, end_date, base)]

for i in range(len(data)-1):
    key = BASE[i+1]
    print BASE[i+1]
    # print data[i]["date"]

    for i in range(len(data)-1):
        d1 = data[i]
        d2 = data[i+1]
        r = d2["rates"][key] - d1["rates"][key]
        print d2["date"], "USD", d2["rates"][key], r
