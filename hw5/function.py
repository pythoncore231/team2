def get_rates_by_date(date=None):
    url = "http://api.fixer.io/"

    if date:
        # ToDO validete date
        url += date

    else:
        url += 'latest'

    data = requests.get(url)
    data = data.json()

    return data


def print_dict(obj):
    for key in obj:
        if isinstance(obj[key], dict):  # type(obj[key]) == 'dict':
            print key, ":"
            for j in obj[key]:
                print "\t{}: {}".format(j, obj[key][j])
        else:
            print "{}: {}".format(key, obj[key])


value_first = get_rates_by_date()
value_second = get_rates_by_date('2008-05-02')
print value_first
print_dict(value_first)
print
print value_second
print_dict(value_second)