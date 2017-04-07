import requests
import datetime

def get_rates_by_date(date=None):
    date = None
    url = 'http://api.fixer.io/'
    if date:
        url += date
    else:
        url += 'latest'

    date = requests.get(url)
    date = date.json()
    return date

def get_rates(date=None, base=None):
    url = "http://api.fixer.io/"
    try:
        start_date = map(int, date.split("-"))
        datetime.date(*start_date);
    except ValueError:
        date = None


    if date:
        url += date
    else:
        url += 'latest'

    if base:
        url = "{}?base={}".format(url, base)
    print url


    data = requests.get(url)
    data = data.json()
    return dict(data)

def get_rates_by_period(start_date, end_date, base=None):
    start_date = map(int, start_date.split("-"))
    start_date = datetime.date(*start_date)

    end_date = map(int, end_date.split("-"))
    end_date = datetime.date(*end_date)

    while start_date <= end_date:
        date = str(start_date)
        data = get_rates(date, base)
        yield data
        start_date += datetime.timedelta(days=1)