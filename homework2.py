# -*- coding: utf-8 -*-

# завдання 1
text = """
and, and, and, and, and.
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!"""

textup = text.upper()

a = textup.count("BETTER")
b = textup.count("NEVER")
c = textup.count("IS")

print 'word "BETTER" found', a, 'times'
print 'word "NEVER" found', b, 'times'
print 'word "IS" found', c, 'times'

print textup.replace("AND", "&") # чому мені не вдається зробити вкладення textup.count(textup.replace("AND", "&")) ?
print ("-"*70)

# завдання 2.а
import math

x = 2
y = 5
z = 10
e = 3

a = (math.sqrt(math.fabs(x-1)) - (math.fabs(y)**1/3) / (1 + (math.pow(x, 2) / 2) + (math.pow(y, 2) / 4))
b = x * (math.atan(z) + e**-(x+3)) # чому не працює функція math.pow(e, -(x+3)) ?

print a
print b
print ("-"*70)

# завдання 2.б
a = (3 + e**y-1)/(1 + x**2 * math.fabs(y - math.tan(z))) # як правилно підносити до степеня у-1 ?
b = 1 + math.fabs(y-x) + ((y-x)**2) / 2 + (math.fabs(y-x)**3) / 3

print a
print b
print ("-"*70)


# завдання 2.в
a = (1 + y) * x + y / (x**2 + 4) / e**-x-2 + x**2 + 4
b = 1 + math.cos(y-2) / x**4 / 2 + math.sin(z)**2 # як правильно визначити синус в квадраті ?

print a
print b
print ("-"*70)