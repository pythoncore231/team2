# d = {}
# d = dict()
#
# l = [1,2,3,1,2,3,1,23,34, "a", "a"]
# s = set(l)
# print s, d
# s1 = set([1,2,3,4])
# print s-s1, s^s1
# print help(set)

d = {"a":1, 1:"a", "b":2}
print d
d = dict(a=1, b=2)
print d
d[1] = [1,2]
print d
print dir(d)
print "as", d.fromkeys(d,["a"])
print d
print d.get("a")
# print d.has_key()

l1 = [1,2,3]
l2 = ["a", "b", "c", "45"]
d = {}
for i in range (len(l1)):
    d[l1[i]] = l2[i]
    print d
d.update({3:4, 5:6})
print d
print d.setdefault(99, "tyhgfg")
print d
del d[99]
print d
print d.pop(1)
print d
print d.popitem()
print d

for i in d:
    print type(i), dir(i) #.__hash__()
str1 = "gfjf lhkugkjyg lhkgjhg khlgkjgmjgh lipoi"
l = str1.split()
print l
l = str1.split("l")
print l
str2 = "".join(l)
print str2
l = ["1", "2", "3"]
m = map(int, l)
print m
def pow(i):
    i = int(i)
    return i**i
m = map(pow, l)
print l
#m = map(lambda i: int(i)**int(i), l)
print m
