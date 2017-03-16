import math

# 1)
year = int(raw_input("Please enter year: "))
if not(year % 4):
    print("It's a leap year!")
else:
    print("This is not a leap year!")

# 2)
year = raw_input("Please enter year: ")
month = int(raw_input("Please enter month: "))
day = int(raw_input("Please enter day: "))

if len(str(year)) and (0 < month <= 12) and (0 < day <= 31):
    print ("This is proper date format")
else:
    print "This is not a proper date format"

# 3)
a = float(raw_input("Please enter a: "))
b = float(raw_input("Please enter b: "))
c = float(raw_input("Please enter c: "))
D = (math.fabs(b**2 - 4*a*c))**0.5

if a != 0:
    x1 = (-b + D) / 2*a
    x2 = (-b - D) / 2*a
    if x1 == x2:
        print ("This function has one root: ", x1)
    else:
        print("This function has two roots: ", x1, x2)
else:
    x = -c/b
    print("a = 0 and x = ", x)

# 4)

a = int(raw_input("Please enter a: "))
b = int(raw_input("Please enter b: "))
c = int(raw_input("Please enter b: "))

if a <= 0 or b <= 0 or c <= 0:
    print "It's not possible to build a triangle"
else:
    if (a+b < c) or (a+c < b) or (c+b < a):
        print "t's not possible to build a triangle"
    else:
        Perimeter = a+b+c
        Square = (Perimeter*(Perimeter - a)*(Perimeter - b)*(Perimeter-c))**0.5
        print ("Perimeter of triangle", Perimeter)
        print ("Square of triangle", Square)


# 5)
k_day = int(raw_input("Please enter k-day of year: "))
week_days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
if 1 <= k_day <= 7:
    print ("k-day is ", week_days[k_day-1])
else:
    if 8 <= k_day <= 365:
        week_day = k_day - (k_day / 7) * 7
        print ("k-day is", week_days[week_day-1])
    else:
        print "Wrong day"
