# -*- coding: utf-8 -*-
import io

"""""
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
        _file.write(u"n")
"""
""""
from entity.room import Room

rooms = []

with io.open("in\\room.txt", 'r') as _file:
    for line in _file:
        if line:
            id, name, capacity = line.split()
            # user = User(firstname=firstname, id=id, lastname=lastname, age=age)
            rooms.append(Room(id, name, capacity))

print rooms
for room in rooms:
    print room

for room in rooms:
    room.name += u"a"

with io.open("out\\room.out", 'w') as _file:
    for room in rooms:
        _file.write(room.to_unicode())
        _file.write(u"\n")

"""
from entity.teacher import Teacher

teachers = []

with io.open("in\\teacher.txt", 'r') as _file:
    for line in _file:
        if line:
            line = line.encode('cp1251')
            id, firstname, lastname, age, position = line.split()

            teachers.append(Teacher(id, firstname, lastname, age, position))

print teachers
for teacher in teachers:
    print teacher

for teacher in teachers:
    teacher.position += u"^"

with io.open("out\\teacher.out", 'w') as _file:
    for teacher in teachers:
        _file.write(teacher.to_unicode())
        _file.write(u"\n")