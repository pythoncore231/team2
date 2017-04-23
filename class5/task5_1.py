# l1 = list()
# print l1, type(l1)
#
# l1 = []
# print l1, type(l1)
#
# t1 = (1, 2, 3, 2, 3)
# print t1, type(t1)
#
# l1 = list(t1)
# print l1, type(l1)

l = [1, "str", 1.5, (1, 2, 3), {1:1, "a":"a"}]
print l
for i in l:
    print i, type(i)

l.append(99)
print l

l.append(l)
print l
for i in l:
    print i, type(i)
l[0] = 55
print l
l[6][0] = 88
print l
l[4]["0"] = 88
print l
print len(l)
print l.__len__()

for i in range(len(l)):
    print l[i], type(l[i])

l = [1, [1, 2]]*5
print l
l = [1, [1, 2]]
print l
l1 = l
print l is l1
l1 = l1 + [99]
print l
print l1

l = [1, [1, 2]]*5
print l
l = [1, [1, 2]]
print l
l1 = l
print l is l1
l1 += [99]
print l
print l1
print l is l1
print dir(l)
l.append([11, 12, 13])
print l
l.extend("[11, 12, 13]")
print l
# print l.index(99)
l.insert(1,9)
print l
l.insert(-2,9)
print l
a = l.pop()
print l, a
print l.pop(5)
print l
print l.remove("1")
print l
l.reverse()
print l
print l[::-1], l
l.sort()
print l
print help(l.sort)
l.sort(reverse=True)
print l
print sorted(l)
print l

