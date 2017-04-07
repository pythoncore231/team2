# The year can be evenly divided by 4;
# If the year can be evenly divided by 100, it is NOT a leap year, unless;
# The year is also evenly divisible by 400. Then it is a leap year.
"""leap year"""

import calendar

yearToCheck = int(raw_input("""
It's checking Gregorian calendar only
Enter year to check: """))

if yearToCheck % 4 == 0 and yearToCheck % 100 != 0 or yearToCheck % 400 == 0:
    print "It's a leap year!"
else:
    print "This is not a leap year!"

# alternative checking with calendar module

if calendar.isleap(yearToCheck):
    print "Python calendar also thinks that entered year is a leap year!"
else:
    print "Python calendar also thinks that entered year is NOT a leap year!"
