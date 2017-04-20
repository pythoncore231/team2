
# -*- coding: utf-8 -*-

def print_dict_rates(obj):
    """
    :param obj(dict):
    :return None:
    """

    """ ToDo
    + додати реалізацію яка видруковує вхідний словник у вигляді:
        date: 2017-03-27
        base: EUR
        rates
            USD: 1.0889
            IDR: 14486.0
            BGN: 1.9558
            ...
    """

    for key in obj:
        if isinstance(obj[key], dict):  # type (obj[key]) == "dict"
            print key, ":"
            for j in obj[key]:
                print "\t{} : {}".format(j, obj[key][j]),
        else:
            print "{}: {}".format(key, obj[key]),



def exchange(amount, rates, *baseto):
    """
    :param amount(int):
    :param rates(dict):
    :param to(str):
    :return (float):
    """

    """ ToDo
        функція приймає 3 параметри,
        `amount` - сума яку требе обміняти,
        `rates` - словник який повертає `get_rates()` для валюти з якoї ми збираємось обмінювати,
        `to` - абрівіатура валюти в яку необхідно обміняти,
        повертає суму після обміну
    """

    data = rates
    print "\tExchange\t{}\t{}\tto:\t".format(amount, 'base')
    for key in data:
        if isinstance(data[key], dict):
            print key, ":"
            for i in baseto:
                data[key][i] *= amount
                print "\t{} : {}".format(i, data[key][i])
