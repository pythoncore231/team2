#end = 6
#count = 1
#iteration = 0
#while count < end:
  #  iteration +=1
  #  print "I:{} before: {}", format(iteration, count)
  #  count += 1
   # if count %2:
  #      continue
   # print "I:{} after: {}", format(iteration, count)
#else:
   # print "else:", count

#str1 = "TEST"
#while str1:
   # print str1,
   # str1 = str1[:-1]
   # print str1

#str1 = 5
#while str1:
    #print str1,
    #str1 = str1[:-1]
    #print str1

#str2 = "some text"
#for i in str2:
#    print i
#for i in range(len(str2)):
#    print i, str2[1]

l = (1, "2", (1,2), 4)
for i in l:
    l = l + (1,2)
    print i, type(i), l

l = [1, "2", 4]
for i in l:
    l.append(1)
    print i, type(i), l
if len(l) > 10
    break


l = [1, 2, 3]
l.append(l)
print l
for i in l:
    print i

for i in [(i, j) for i in range(5) for j in range(5)]:
    print i

l = [(i, j) for i in range(5) for j in range(5)]:
for i in l:
    print i

l = []
for i in range(5):
    for j in range(5):
        l.append((i, j))

import this