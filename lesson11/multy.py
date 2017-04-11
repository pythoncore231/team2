class A(object):
    def f1(self):
        return "a_f1"
    def f2(self):
        return "a_f2"       
class B(object):
    def f2(self):
        return "B_f2"
    def f3(self):
        return "B_f3"       

class C(B, A):
    pass
c = C()
print c.f1()
print c.f2()
print c.f3()
try:
    print c.f4()
except AttributeError as e:
    print "stuped user", e

except Exception, e:
    raise e

# else:
#     pass
# finally:
#     pass
print 1+1