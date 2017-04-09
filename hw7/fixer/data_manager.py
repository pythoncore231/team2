# -*- coding: utf-8 -*-

from requests import get
from datetime import timedelta as td
from datetime import datetime as dt


BASE = ('EUR', 'SD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
                               'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
                               'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
                               'CZK', 'BRL', 'PLN', 'PHP', 'ZAR')

def date_is_correct(date):
    # try:
    #     dt.strptime(date, '%Y-%m-%d')
    # except ValueError:
    #     raise ValueError("Невірна дата, очікується YYYY-MM-DD")
    if dt.strptime(date, '%Y-%m-%d'): return True; return False

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
    if date:
        url += date
    else:
        url += 'latest'

    if base:
        url = "{}?base={}".format(url, base)
    # print url


    data = get(url)
    data = data.json()
    return dict(data)


def get_rates_by_period(start_date, end_date, base=None):
    """
    generator
    
    :param start_date(str):
    :param end_date(str):
    :param base(str or None): {'EUR', 'SD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
                               'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
                               'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
                               'CZK', 'BRL', 'PLN', 'PHP', 'ZAR'}
    :return dict or None (if error):
    """
    date_mask = "%Y-%m-%d"
    end_date = dt.strptime(end_date, date_mask)
    start_date = dt.strptime(start_date, date_mask)
    #datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    cur_date = start_date

    while cur_date <= end_date:
        cur_date += td(days=1)
        yield get_rates(str(cur_date), base)


# for i in rates:
#     print i

# print rates

print '\tDATE\t|\t'+'\t|\t'.join(BASE)