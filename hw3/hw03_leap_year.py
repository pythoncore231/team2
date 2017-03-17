# The year can be evenly divided by 4;
# If the year can be evenly divided by 100, it is NOT a leap year, unless;
# The year is also evenly divisible by 400. Then it is a leap year.
import calendar

yearToCheck = int(raw_input("Enter year to check: "))

if yearToCheck%4 == 0 and yearToCheck % 100 != 0 or yearToCheck % 400 == 0:
    print "Entered year is leap year!"
else:
    print "Entered year is NOT leap year!"

#alternative checking with calendar module

if calendar.isleap(yearToCheck):
    print "Python also thinks that entered year is leap year!"
else:
    print "Python also thinks that entered year is NOT leap year!"
