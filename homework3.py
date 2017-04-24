-*- coding: utf-8 -*-

# завдання 1
x = int(raw_input("Please enter your birth year: "))
if x % 4 == 0:
    print "It's a leap year!"
else:
    print "This is not year"

# завдання 2
day = int(raw_input("Please enter day in range of 1 to 31: "))
if day < 1 or day > 31:
    print "Uncorrect day format"

month = int(raw_input("Please enter month in range of 1 to 12: "))
if month < 1 or month > 12:
    print "Uncorrect month format"

year = int(raw_input("Please enter year in range of 1900 to 2017: "))
if year < 1900 or year > 2017:
    print "Uncorrect month format"