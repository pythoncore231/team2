# -*- coding: utf-8 -*-
from fixer import data_manager
from fixer.data_manager import BASE


def exchange_rates(data=[]):
    """ToDo
    вивести таблицю курсів в заданому проміжку дат
    перевірка на відсутність повторів у вибірці(optional)
    DATE  |  USD  |       EUR(+/-)     |  ..  
    Y-m-d |  rate | rate(rate_changes) |  .. 
    """
    


    # for i in range(len(data)-1):
    #     print BASE[i]
    #     print data[i]["date"]

    # for i in data:
    #     print data[i]
    # for i in range(len(data)-1):
    #     d1 = data[i]
    #     d2 = data[i+1]
    #     r =  d2["rates"]["USD"] - d1["rates"]["USD"]
    #     print d2["date"], "USD", d2["rates"]["USD"], r

    # #     for j in d:
    # #         print j, d["rates"][j]

    # # TEMPLATE = data[0]["date"]
    # # TEMPLATE = data[0]["base"]
    # # TEMPLATE = data[0]["rates"]["USD"]
    # # TEMPLATE = data[]["date"]
    # # TEMPLATE = data[]["date"]
    # # TEMPLATE = data[]["date"]
    # # pass


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
        `rates` - словник який повертає `get_rates()` для валюти з якиї ми збираємось обмінювати,
        `to` - абрівіатура валюти в яку необхідно обсміняти,
        повертає суму після обміну
    """


""" ToDo
   1) вивести зміну курсу валют для USD за період з 20 по 27 березня 2017 року
   2) вивести суму яку буде при обміня певної суми DKK на BGN та KRW
"""
pass


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


    pass

