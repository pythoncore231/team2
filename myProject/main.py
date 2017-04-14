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

with io.open("in\\user.in", 'w') as _file:
    for user in users:
        _file.write(unicode(user.__str__()))
        _file.write(u"\n")
with io.open("in\\user.in", 'r') as _file:
    for line in _file:
        if line:
            print line
            # id, firstname, lastname, age = line.split()
            user = User.create(line)
            print user

from entity.room import Room

rooms = []
rooms.append(Room(name="119a", capacity=15))
rooms.append(Room(name="119b", capacity=20))
rooms.append(Room(name="118", capacity=20))

with io.open("out\\room.out", 'w') as _file:
    for room in rooms:
        _file.write(room.get_data_to_save())
        _file.write(u"\n")

with io.open("out\\user2.out", 'w') as _file:
    for user in users:
        _file.write(user.get_data_to_save())
        _file.write(u"\n")


with io.open("out\\room.out", 'r') as _file:
    for line in _file:
        room = Room.create(line)
        print type(room)
        print room
