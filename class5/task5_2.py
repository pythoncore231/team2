l = [1,2,3,4,1, "str"]
t = tuple(l)
print l, t
# print dir(t)
print l.__sizeof__(), t.__sizeof__()
print t.count(1)
print t.index(1)



