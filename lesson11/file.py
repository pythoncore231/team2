from io import open
data = open("data.txt")

print data
for i in data:
    print i

data.close()

with open("data.txt") as data:
    for i in data:
        print i


