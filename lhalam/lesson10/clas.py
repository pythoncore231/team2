class myClass(object):
    """docstring for myClass"""
    # obj = None
    # def __new__(cls, * dt, ** mp):
    #     print "__new__", type(cls)
    #     if cls.obj is None:
    #        cls.obj = object. __new__ (cls, *dt, **mp)
    #     return cls.obj
    z = 10
    def __init__(self, x=0, y=0, t=100):
        # print "__init__", type(self)
        self.x = x
        self.y = y
        self.__t = t

    def isZero(self):
        return True if self.x==self.y==0 else False

    def __str__(self):
        return "x:{} y:{} z:{} t:{}".format(self.x, self.y,
                                  self.z, self.__t)

    def __repr__(self):
        return "({},{})".format(self.x, self.y)

    def __del__(self):
        # print "__del__ ", self
        pass

    def __add__(self, other):
        x = self.x+other.x
        y = self.y+other.y
        return myClass(x, y)

    def sub(self, other):
        x = self.x-other.x
        y = self.y-other.y
        return myClass(x, y)

    def __eq__(self, other):
        return True if self.x == other.x and self.y == other.y else False
    
    @staticmethod
    def fun(z, k):
        return z+k

    def print_ins(self):
        print self.__dict__

    @classmethod
    def print_cls(cls):
        def temp(self):
            return self.x + self.y + self.z
        cls.temp = temp
        print cls.__dict__


m1 = myClass()
m2 = myClass(3, 2)
m3 = myClass(3, 1)
print m1
print m2
print (m1, m2)
# del m2
print m1.isZero()
print dir(m1)
# data = [i for i in range(10)]
# del data[::2]
# print data
print m2
print m3
m4 = m2 + m3
print m4
print m2 == m3
m5 = m2.sub(m3)
print m5
print myClass.fun(9, 99)
print m5.fun(9, 99)
# m4.print_ins()
print m4.z
# m4.print_cls()
# print m4.temp()
# print myClass.__dict__

print "t:", m4._myClass__t
print m4