my_file = open("simfli.txt", "r")
my_string = my_file.read()

print ("Было прочитано:")
print (my_string.upper())
print ("Кількість входжень better:")
print (my_string.lower().count('better'))
print ("Кількість входжень never:")
print (my_string.lower().count('never'))
print ("Кількість входжень is:")
print (my_string.lower().count('is'))

i=0
m=""
while i < len(my_string)-1:
    x=my_string[i:i+1]
    if x=="i":
        z='&'
    else:z=x
    m=m+z
    i=i+1

print (m)
my_file.close()