# -*- coding: utf-8 -*-
import requests
import datetime
BASE = {'EUR', 'USD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
        'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
        'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
        'CZK', 'BRL', 'PLN', 'PHP', 'ZAR'}

def validate_date(input_date):
    # input_date = map(int, input_date.split("-"))
    # try:
    #     input_date = datetime.strptime(input_date, '%Y, %m, %d')
    # except ValueError:
    #     print "Incorrect format"
    #     return None
    i_date = input_date.split("-")
    if (1 < int(i_date[0]) < 9999) and (len(i_date[0]) == 4) and (0 < int(i_date[1]) <= 12) and (0 < int(i_date[2]) <= 31):
        return input_date
    else:
        return None

def get_rates(date=None, base=None):
    """
    :param date(str or None): format "2000-01-03"
    :param base(str or None): {'EUR', 'USD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
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
    if date:
        if validate_date(date):
            url += date
    else:
        url += 'latest'

    if base:
        if base in BASE:
            url = "{}?base={}".format(url, base)
        else:
            return None 
    # print url

    data = requests.get(url)
    data = data.json()
    return dict(data)

    """ ToDo
    1) вивести зміну курсу валют для USD за період з 20 по 27 березня 2017 року
    DATE  |  USD  |       EUR(+/-)     |  ..  
    Y-m-d |  rate | rate(rate_changes) |  .. 
    2) вивести суму якa буде при обмінi певної суми DKK на BGN та KRW
    """





def get_rates_by_period(start_date, end_date, base=None):
    """
    # generator
    :param start_date(str):
    :param end_date(str):
    ::param base(str or None): {'EUR', 'USD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
                               'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
                               'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
                               'CZK', 'BRL', 'PLN', 'PHP', 'ZAR'}
    :return dict or None (if error):
    """


    start_date = map(int, start_date.split("-"))
    start_date = datetime.date(*start_date)

    end_date = map(int, end_date.split("-"))
    end_date = datetime.date(*end_date)

    while start_date <= end_date:
        date = str(start_date)
        data = get_rates(date, base)
        yield data
        start_date = start_date + datetime.timedelta(days=1)

    



