class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
       return "({}, {})".format(self.x, self.y)
    def len(self):
        return (self.x**2+self.y**2)**0.5

class Point3D(Point):
    """bdhjsvfjdzsbvjesw"""
    def __init__(self, x, y, z):
        super(Point3D, self).__init__(x,y)
        self.z = z
    def __repr__(self):
       return "({}, {}, {})".format(self.x, self.y, self.z)
    def __str__(self):
       return "({} {})".format(super(Point3D, self).__repr__(), self.z)
       
    def my_repr(self):
        return self.__repr__()
    def len(self):
        return (self.x**2+self.y**2+self.z**2)**0.5
    def len_parent(self):
        return super(Point3D, self).len()

p = Point(1,1)
print p
print p.len()
p3 = Point3D(1,1,1)
print p3
print p3.my_repr()
print p3.len()
print p3.len_parent()
print dir(p3)
print p3.__class__
p3.__class__ = Point
print p3
print p3.__dict__
p3.__class__ = Point3D
print p3.__doc__

class Triangle(object):
    class Point(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
       return "({}, {})".format(self.x, self.y)
    def len(self):
        return (self.x**2+self.y**2)**0.5

    """docstring for triangle"""
    def __init__(self, arg):
        self.points = [Point(1,1),Point(1,1),Point(1,1)]
        
