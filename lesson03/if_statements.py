# -*- coding: utf-8 -*-

a = 1
b = 5
c = 3

if a < c < b:
	print True
else:
	print False
str1 = ""
if str1 :
	print True
else:
	print False

l = [1, 2, 3, 4]

print 1 in l
print 5 in l

str2 = "dsafgvh"
print "af" in str2
print "5" in str2
print 12 in l
for i in l:
	print i,
print
for i in str2:
	print i,
print

t1 = (1,2,3,4)
t2 = t1
print t1 is t2
t3 = t1[:]
print t1 is t3

l1 = [1,2,3,4]
l2 = l1
print l1 is l2
l3 = l1[:]
print l1 is l3

a = 2**7+1
b = 2**7+1
print a is b
a = 2**8+1
b = 2**8+1
print a is b

# a = []
# for i in range(10**5):
# 	a.append(i)
# print "test"
# print a

if True:
	print "foo"

if False:
	print "foo"
else:
	print "boo"
a = 1.1
if a < 0:
	print "-"
elif a == 0:
	print "0"
elif a < 1:
	print "0..1"
else:
	print "+"


# додатнє парне "+e"
# додатнє не парне "+о"
# відємне парне "-e"
# відємне не парне "-о"
b = -2
if b > 0:
	if not b % 2:
		print "+e"
	else:
		print "+o"
else:
	if not b % 2:
		print "-e"
	else:
		print "-o"

if b > 0:
	print "+e" if not b % 2 else "+o"
	print ["+e", "+o"][b % 2]
else:
	print "-e" if not b % 2 else "-o"
	print ["-e", "-o"][b % 2]

a = raw_input("ss") 
print a
