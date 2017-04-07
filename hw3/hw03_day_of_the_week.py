# This Python file uses the following encoding: utf-8
"""hw03_day_of_the_week"""
# enter int (1..365)
# out day of the week
# not leap year where 1 JAN is Monday

day_nmbr = int(raw_input("Введіть номер дня: "))

DAYS = ["Понеділок", "Вівторок", "Середа",
        "Червер", "П'ятниця", "Субота", "Неділя"]

if 0 < day_nmbr < 366:
    week_day = day_nmbr % 7
    print DAYS[week_day - 1]
else:
    print("тільки для землян, пробачте за дискримінацію")
