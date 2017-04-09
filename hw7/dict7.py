# -*- coding: utf-8 -*-

from datetime import timedelta as td
from datetime import datetime as dt

slovnyk = {"key1":"value1",
            "key2":"value2",
            "key3":"value3",
            "key4":"value4",
            "key5":"value5",
            "key6":"value6",
            "key7":"value7"}

# sl_keys = slovnyk.keys()

# print sl_keys[3]

def date_is_correct(date):
    try:
        dt.strptime(date, '%Y-%m-%d')
    except ValueError:
        raise ValueError("Невірна дата, очікується YYYY-MM-DD")
    # if dt.strptime(date, '%Y-%m-%d'): return True; return False

print date_is_correct("2000-33-12")