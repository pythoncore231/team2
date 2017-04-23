# class B():
#     pass


class A(object):
    atr1 = "name"
    atr2 = [1, 2, 3]

    def __init__(self):
        self.atr3 = "name"
        self.atr4 = [1, 2, 3]
        atr5 = "abs"
        # print self.__dict__

    def __str__(self):
        print self.__dict__

        return "{} {} {} {}".format(self.atr1,
                                    self.atr2,
                                    self.atr3,
                                    self.atr4)


# print dir()
# print type(A), type(B)
# print dir(A)
# print dir(B)
a = A()
# print a.atr1
# print a.atr2
# print a.atr3
# print a.atr4
# print a
# print dir(a)
# print dir(A)
# print a.__dict__
# print A.__dict__
b = A()
print b
print a
a.atr3 = "new"
a.atr4.append(4)
print b
print a
A.atr1 = "new"
b.atr2.append(4)
print b
print a
A.atr3 = ""
print b
print a
print A.__dict__