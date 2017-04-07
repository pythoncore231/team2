# -*- coding: utf-8 -*-

from fixer.data_manager import get_rates, get_rates_by_period
from utils.process import exchange_rates
from fixer.data_manager import BASE
from entity.currency import CurrencySub

# rates = [i for i in get_rates_by_period("2016-12-10", "2016-12-11", "USD")]
rates = [CurrencySub(i["date"], i["base"], i["rates"]) for i in get_rates_by_period("2016-12-10", "2016-12-11", "USD")]

# print '\tDATE\t|\t'+'\t|\t'.join(BASE)
# print rates
print rates
data = get_rates()

myCurrency = CurrencySub(
    date=data["date"], base=data["base"], rates=data["rates"])

print myCurrency
print rates[0]-rates[1]
