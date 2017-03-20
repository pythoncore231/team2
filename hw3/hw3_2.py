import calendar
yyyy = int(raw_input("year from 1 to 5000   "))
mm = int(raw_input("month from 1 to 12   "))
dd = int(raw_input("day from 1 to 31  "))

if yyyy <= 0:
    print "year is incorrect"
    exit(0)

if 12 <= mm <= 1:
    print "month is incorrect"
    exit(0)

if 1 <= dd <= calendar.monthrange(yyyy,mm)[1]:
    print "correct date"
else:
    print "day of month is incorrect"
    exit(0)



