from calendar import weekday, isleap, day_name
k = int(raw_input("enter k from 1 to 365:  "))
years = range(1970, 3000, 1)


for year in years:
    if 1 <= k <= 365:
        if 0 == weekday(year, 1, 1) and not isleap(year):
            m = k % 7
            n = day_name[m]
            print k, "day of", year, "is", n



