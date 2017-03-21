
def sum_of_cubs_of_digits(value):
    return sum(int(c) ** 3 for c in str(value))

string = raw_input("enter numer: ")
print "Sum of cubes %d" % sum_of_cubs_of_digits(string)
