import io
from entity.user import User


users = []
# 'r'
# 'w'
# 'a'
with io.open("in\\user.txt", 'r') as _file:
    for line in _file:
        if line:
            # id, firstname, lastname, age = line.split()
            data = line.split()
            id = data[0]
            firstname = data[1]
            lastname = data[2]
            age = int(data[3])
            user = User(id, firstname, lastname, age)
            # user = User(firstname=firstname, id=id, lastname=lastname, age=age)
            users.append(user)
        # _file.write(unicode(i))
        # _file.write(u"\n")
print users
for user in users:
    print user
    # print user.to_unicode()

for user in users:
    user.age -=5

for user in users:
    print user

with io.open("out\\user.out", 'w') as _file:
    for user in users:
        _file.write(user.to_unicode())
        _file.write(u"\n")
