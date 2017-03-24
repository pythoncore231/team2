import requests

#url = 'http://api.fixer.io/latest'
#r = requests.get(url)
#r = r.json()

#print r

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

def print_dict(obj):
    for key in obj:
        if isinstance(obj[key], dict): #type(obj[key]) == 'dict':
            print key, ":"
            for j in obj[key]:
                print "\t{} : {}".format(j, obj[key][j])
        else:
            print "\t{} : {}".format(key, obj[key])

value_first = get_rates_by_date()
value_second = get_rates_by_date('2008-05-02')

print value_first
print_dict(value_first)
print
print value_second
print_dict(value_second)