import requests
import datetime


# url = 'http://api.fixer.io/latest'
# r = requests.get(url)
# r = r.json()

# print r

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

def print_dict(obj):
    for key in obj:
        if isinstance(obj[key], dict):  # type(obj[key]) == 'dict':
            print key, ":"
            for j in obj[key]:
                print "\t{} : {}".format(j, obj[key][j])
        else:
            print "\t{} : {}".format(key, obj[key])


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


value_first = get_rates_by_date()
value_second = get_rates_by_date('2008-05-02')

# print value_first
# print_dict(value_first)
# print
# print value_second
# print_dict(value_second)

data = get_rates_by_period("2017-03-01", "2017-03-28")
for i in data:
    print_dict(i)
    print
