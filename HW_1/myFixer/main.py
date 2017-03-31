from utils.proces import print_dict, get_rates_by_period, print_dict_table, print_temp

#value_first = Rt.get_rates_by_date()
#value_second = Rt.get_rates_by_date('2008-05-02')

# print value_first
# print_dict(value_first)
# print
# print value_second
# print_dict(value_second)

data = [i for i in get_rates_by_period("2017-03-01", "2017-03-5")]

print_temp(data)
# for i in data:
#     print_dict_table(i, temp)
#     temp = i
#     print

#data = Rt.get_rates("2017-03-01", "BRL")

#date = "fddffg"
#start_date = map(int, date.split("-"))
#datetime.date(*start_date)