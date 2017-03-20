import calendar
year = int(raw_input("year   "))
if calendar.isleap(year):
    print "It's a leap year!"
else:
    print "This is not a leap year!"
