class Point(object):

    def __init__(self, x=0, y=0, z=0):
        self.x = x
        self._y = y
        self.__z = z

    def get_z(self):
        print "get_z"
        return self.__z
    # @property
    # def y(self):
    #     return self._y
    
    def set_z(self, z):
        print "set_z"
        self.__z = z


    def __repr__(self):
        return "({}, {}, {})".format(self.x, self._y, self.__z)
    z = property(get_z, set_z)

p = Point(1,2,3)
# print p.x
# print p._y
# # print p.__z
# print p.get_z()
# print p._Point__z
# p._Point__z = 99
# print p.get_z()
# print p
# print p.get_z()
# p.set_z(99)
# print p
# print p.z
# p.z = 88
# print p.z
# print p.z
print dir(p)

p.z
p.z = 10
p.z
