# l = [1,2,3]
# t = (1,2,3)
# def my_func(a, b):
#     i = 1
#     a.append("str")
#     print a
#     b = b + (1,)
#     print b
#     return i, a, b

# print my_func(l, t)
# print l, t
# print my_func(b=t, a=l)

# def my_func(a=["a", "b"], b = (1,2,3)):
#     print "start: a:{} b:{}".format(a, b)
#     a.append("str")
#     # print a
#     b = b *2
#     # print b
#     return a, b

# print l, t
# print my_func(l, t)
# print l, t
# print my_func(l)
# print l, t
# print my_func(b=l)

# def my_func(a=["a", "b"], b = (1,2,3)):
#     print "start: a:{} b:{}".format(a, b)
#     a.append("str")
#     # print a
#     b = b *2
#     # print b
#     return a, b

# print l, t
# print my_func(l, t)
# print l, t
# print my_func(l)
# print l, t
# print my_func(b=l)

# def my_func_2(a, b=None, *l, **d):
#     print a
#     print b
#     print l
#     print d

# my_func_2(1)
# my_func_2(1, b = 22)
# my_func_2(1, 22)
# my_func_2(1, 22, 3, 4, 4, "dsf")
# my_func_2(1, 22, 3, 4, c=4, f="dsf")

# var = (1,2,3,4,5,6,7,8,9,0)
# # my_func_2(var)
# # my_func_2(None, *var)
# key = {"b":"b", "c":"c"}
# my_func_2(None, **key)

# def my_func_2(a, b=None):
#     print a
#     print b
import requests


# url = 'http://api.fixer.io/latest'
# # url = "http://api.fixer.io/2000-01-03"
# r = requests.get(url)
# r = r.json()
# print r
# print type(r)
# url = "http://api.fixer.io/2000-01-03"
# r = requests.get(url)
# r = r.json()
# print r

def get_rates_by_date(date=None):
    
    url = "http://api.fixer.io/"

    if date:
        #ToDO validete date
        url += date

    else:
        url += 'latest'

    data = requests.get(url)
    data = data.json()
    
    return data

def print_dict(obj):
    for key in obj:
        if isinstance(obj[key], dict): # type(obj[key]) == 'dict':
            print key, ":"
            for j in obj[key]:
                print "\t{}: {}".format(j,  obj[key][j])
        else:
            print "{}: {}".format(key,  obj[key])

value_first =  get_rates_by_date()
value_second = get_rates_by_date('2008-05-02')
print value_first
print_dict(value_first)
print
print value_second
print_dict(value_second)