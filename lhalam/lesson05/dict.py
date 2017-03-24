# d = {}
# d = dict()
# l = [1,2,3,1,2,3,1,23,34, "a", "a"]
# s = set(l) 
# print s, d
# s1 = set([1,2,3,4]) 
# print s - s1, s^s1
# print help(set)
d = {"a": 1, 1:"a", "b":2}
print d
d = dict(a=1, b=2,mhnsabdja={"a":"a", "b":"b"})
print d
d[1] = [1,2]
print d
print dir(d)
print "as", d.fromkeys(d, ["a"])
print d
print d.get("a")
print d.get("hdsbfhjds")
print d.keys()
print d.values()
print d.items()
for i in d:
    print i, d[i]
l1 = [1,2,3, "45"]
l2 = ["a", "b", "c", 4]
d = {}

for i in range(len(l1)):
    d[l1[i]] = l2[i]
print d 
d.update({3:4, 5:6})
print help(d.setdefault)
a = d.setdefault(99)
print d
del d[99]
print d
print d.pop(1)
print d
for i in d:
    print type(i), dir(i) #.__hash__()
    print 

