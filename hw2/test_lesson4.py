# -*- coding: UTF-8 -*-
# end = 6
# count = 1

# while count < end:
# 	print "before: ", count
# 	count += 1
# 	if count%2:
# 		continue
# 	print "after: ", count
# else:
# 	print "else: ", count

# str1 = "TEST"
# while str1:  #len(str1) == 0
# 	print str1,
# 	str1 = str1[:-1]
# 	print str1


# str1 = 5
# while str1:  #len(str1) == 0
# 	print str1,
# 	str1 -= 1
# 	print str1

# str1 = "some text"

# for i in str1:
# 	print i

# for i in range(len(str1)):
# 	print i, str1[i]

# l = (1, "two", (1,2), 4)
# for i in range(len(l)):
# 	print i, type(l[i]), l[i]

# l = [1, 2, 3]
# l.append(l)
# print l

#знайти стрінг1 в стрінг2

MainText = """It determines if string str occurs in string, or in a substring of string if starting index beg and ending index end are given."""

substr = "c"

while MainText:
	p = MainText.find(" ")
	tempText = MainText[:p]
	print MainText

