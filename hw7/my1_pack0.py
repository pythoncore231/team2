# -*- coding: utf-8 -*-

from requests import get
from datetime import timedelta as td
from datetime import datetime as dt


BASE = ('EUR', 'SD', 'IDR', 'BGN', 'ILS', 'GBP', 'DKK', 'CAD', 'JPY',
                               'HF', 'RON', 'MYR', 'SEK', 'SGD', 'HKD', 'AD', 'CHF', 'KRW',
                               'CNY', 'TRY', 'HRK', 'NZD', 'THB', 'NOK', 'RB', 'INR', 'MXN',
                               'CZK', 'BRL', 'PLN', 'PHP', 'ZAR')

def get_rates(date=None, base=None):


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

    date_mask = "%Y-%m-%d"
    end_date = dt.strptime(end_date, date_mask)
    start_date = dt.strptime(start_date, date_mask)
    #datetime_object = datetime.strptime('Jun 1 2005  1:33PM', '%b %d %Y %I:%M%p')
    cur_date = start_date

    while cur_date <= end_date:
        cur_date += td(days=1)
        yield get_rates(str(cur_date), base)

rates = [i for i in get_rates_by_period("2016-12-01", "2016-12-10", "USD")]

print 
# for i in rates:
#     print i

# print rates