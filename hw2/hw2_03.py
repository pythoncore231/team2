#Поміняти між собою значення двох змінних, не використовуючи третьої змінної.
a = "a"
b = "b"
c = a + b
print "before replacement:", c
a,b = b,a
c = a + b
print "after replacement:", c
