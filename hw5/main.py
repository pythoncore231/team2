# -*- coding: utf-8 -*-

import requests

base_list = ['EUR', 'SD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY', 'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW', 'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN', 'CZK', 'BRL', 'PLN', 'PHP', 'ZAR']


def is_correct_date_format(date=None):
    if date:
        date_chunks = date.split('-')
        if len(date_chunks) == 3:
            if date_chunks[0].isdigit() and len(date_chunks[0]) == 4 and date_chunks[1].isdigit() and len(date_chunks[1]) == 2 and date_chunks[2].isdigit() and len(date_chunks[2]) == 2:
                return True
        else:
            return False
    return False


def get_rates(date=None, base=None):
    """
    :param date(str or None): format "2000-01-03"
    :param base(str or None): {'EUR', 'SD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
                               'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
                               'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
                               'CZK', 'BRL', 'PLN', 'PHP', 'ZAR'}
    :return dict or None (if error):
    """

    """ ToDo
        1) додати перевірку у випадку якщо `date` не None на коректність введення згідно формату
        2) додати перевірку у випадку якщо `base` не None на коректність введення,
           є конкретна множина допустимих значень
    """

    url = "http://api.fixer.io/"
    if is_correct_date_format(date):
        url += date
    else:
        url += 'latest'

    if base and base.upper() in base_list:
        url = "{}?base={}".format(url, base)
    # print url


    data = requests.get(url)
    data = data.json()
    return dict(data)


def print_dict_rates(obj):
    """
    :param obj(dict):
    :return None:
    """

    """ ToDo
    додати реалізацію яка видруковує вхідний словник у вигдаді:
        date: 2017-03-27
        base: EUR
        rates
            USD: 1.0889
            IDR: 14486.0
        	BGN: 1.9558
        	...
    """
    for key in obj:
        if isinstance(obj[key], dict):  # type(obj[key]) == 'dict':
            print key, ":"
            for j in obj[key]:
                print "\t{}: {}".format(j, obj[key][j])
        else:
            print "{}: {}".format(key, obj[key])



def exchange(amount, rates, to):
    """
    :param amount(int):
    :param rates(dict):
    :param to(str):
    :return (float):
    """

    """ ToDo
        функція приймає 3 параметри,
        `amount` - сума яку требе обміняти,
        `rates` - словник який повертає `get_rates()` для валюти з якої ми збираємось обмінювати,
        `to` - абрівіатура валюти в яку необхідно обсміняти,
        повертає суму після обміну
    """
    return float(rates['rates'][to.upper()])*amount


""" ToDo
   1) вивести зміну курсу валют для USD за період з 20 по 27 березня 2017 року
   2) вивести суму яку буде при обміні певної суми DKK на BGN та KRW
"""

if __name__ == "__main__":

    print("1) вивести зміну курсу валют для USD за період з 20 по 27 березня 2017 року")
    for i in range(20, 28):
        rate_date = "2017-03-{}".format(i)
        rate = get_rates(date=rate_date, base="EUR")
        print("{} | {}".format(rate_date, rate['rates']["USD"]))

    print("2) вивести суму яку буде при обміні певної суми DKK (amount=100) на BGN та KRW")
    rates = get_rates(date="2017-03-21", base="DKK")
    print(exchange(100, rates, "BGN"))
    print(exchange(100, rates, "KRW"))

    amount = int(raw_input("Enter amount for exchange: "))
    to = raw_input("Enter currency: ")
    print(exchange(amount, get_rates(date="2017-03-21", base="EUR"), to))
