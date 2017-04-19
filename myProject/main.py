# -*- coding: utf-8 -*-
import io
from entity.user import User
from entity.room import Room
from entity.lesson import Lesson
from entity.group import Group
from entity.scheduler import Scheduler

users = []
rooms = []
lessons = []

with io.open("in//users.in", 'r') as _file:
    for line in _file:
        if line:
            id, firstname, lastname, age = line.split(",")
            user = User(id, firstname, lastname, age)
            users.append(user)

with io.open("in//room.in", 'r') as _file:
    for line in _file:
        if line:
            id, room_number, capacity = line.split(",")
            room = Room(id, room_number, capacity)
            rooms.append(room)

with io.open("in//lesson.in", 'r') as _file:
    for line in _file:
        if line:
            id, title, teacher = line.split(",")
            lesson = Lesson(id, title, teacher)
            lessons.append(lesson)

print users
for user in users:
    print user

for user in users:
    print user

with io.open("out//user.out", 'w') as _file:
    for user in users:
        _file.write(user.to_unicode())
        # _file.write(u"\n")

groups = [[i for i in users if i.age % 2],
          [i for i in users if not i.age % 2]]


list_101 = []
list_202 = []

for user in users:
    if int(user.id) % 2:
        list_101.append(user)
    else:
        list_202.append(user)

group_101 = Group(1, "101", list_101)
group_202 = Group(2, "202", list_202)

groups = [group_101, group_202]

with io.open("out\\group.out", 'w') as _file_group:
    for group in groups:
        _file_group.write(group.to_unicode())
        _file_group.write(u"\n")


# на основі вже сформованих даних сформувати довільний розклад і записати у відповідний файл
# scheduler.py: room, lesson, group, para (1,2,3 int)

schedulers_101 = (Scheduler(n + 1, rooms[n], lessons[n], groups[0], n + 1) for n in range(7))
schedulers_202 = (Scheduler(n + 8, rooms[n], lessons[n], groups[1], n + 2) for n in range(7))

schedulers = [schedulers_101, schedulers_202]

with io.open("out\\scheduler.out", 'w') as _file_scheduler:
    for schedul in schedulers:
        for each in schedul:
            _file_scheduler.write(each.to_unicode())
            _file_scheduler.write(u"\n")