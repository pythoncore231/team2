def print_dict(obj):
    for key in obj:
        if isinstance(obj[key], dict):  # type(obj[key]) == 'dict':
            print key, ":"
            for j in obj[key]:
                print "\t{} : {}".format(j, obj[key][j])
        else:
            print "\t{} : {}".format(key, obj[key])

def print_dict_table(obj):
    for key in obj:
        pass


def print_temp(data):
    pass