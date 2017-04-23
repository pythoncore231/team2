import io
from entity.user import User
from entity.room import Room
from entity.teacher import Teacher
from entity.lesson import Lesson
from entity.group import Group
from entity.sheduler import Sheduler

from random import choice


def is_prime(value):
    if (value % 2) == 0:
        return True
    else:
        return False

# Load user data from file
users = []

with io.open("in//user.txt", 'r') as _file:
    for line in _file:
        if line:
            data = line.split()
            id = data[0]
            firstname = data[1]
            lastname = data[2]
            age = int(data[3])
            user = User(id, firstname, lastname, age)
            users.append(user)

# Load group data from file
groups = []

with io.open("in//group.txt", 'r') as _file:
    for line in _file:
        if line:
            data = line.split()
            id = data [0]
            name = data[1]
            group = Group(id, name)
            groups.append(group)

# Link users to groups
for user in users:
    if (int(user.id) % 2) == 0:
        groups[0].add_user(user)
    else:
        groups[1].add_user(user)

# Create output file with group information
with io.open("out//group.out", 'w') as _file:
    for group in groups:
        _file.write(group.to_unicode())
        _file.write(u"\n")

# Load teacher data from file
teachers = []

with io.open("in//teacher.txt", 'r') as _file:
    for line in _file:
        if line:
            # id, firstname, lastname, age, position = line.split()
            data = line.split()
            id = data[0]
            firstname = data[1]
            lastname = data[2]
            age = int(data[3])
            position = data[4]
            teacher = Teacher(id, firstname, lastname, age, position)
            teachers.append(teacher)

# Load lessons data from file
lessons = []

with io.open("in//lesson.txt", 'r') as _file:
    for line in _file:
        if line:
            data = line.split()
            id = data [0]
            name = data[1]
            lesson = Lesson(id, name, [teacher for teacher in teachers if teacher.position == name][0])
            lessons.append(lesson)

# Load rooms data from file
rooms = []

with io.open("in//room.txt", 'r') as _file:
    for line in _file:
        if line:
            data = line.split()
            id = data [0]
            room_number = data[1]
            capacity = data[2]
            room = Room(id, room_number, capacity)
            rooms.append(room)

# Create schedule
schedules = []

para = 1

for i in range(0, 6, 2):
    rooms_for_a = [room for room in rooms if room.capacity >= len(groups[0].members)]
    rooms_for_b = [room for room in rooms if room.capacity >= len(groups[1].members)]
    room_for_a = choice(rooms_for_a)
    room_for_b = choice(rooms_for_b)

    while room_for_a.id == room_for_b.id:
        room_for_a = choice(rooms_for_a)
        room_for_b = choice(rooms_for_b)

    lesson_for_a = choice(lessons)
    lesson_for_b = choice(lessons)

    while lesson_for_a.id == lesson_for_b.id:
        lesson_for_a = choice(lessons)
        lesson_for_b = choice(lessons)

    schedule_a = Sheduler(i, room_for_a, lesson_for_a, groups[0], para)
    schedule_b = Sheduler(i+1, room_for_b, lesson_for_b, groups[1], para)

    schedules.append(schedule_a)
    schedules.append(schedule_b)

    para += 1

for schedule in schedules:
    print schedule

# with io.open("out//lesson.out", 'w') as _file:
#     for Lesson in Lessons:
#         _file.write(Lesson.to_unicode())
#         _file.write(u"\n")

# print users
# for user in users:
#     print user
#     # print user.to_unicode()

# for user in users:
#     user.age -=5
#
# for user in users:
#     print user
#
# with io.open("out//user.out", 'w') as _file:
#     for user in users:
#         _file.write(user.to_unicode())
#         _file.write(u"\n")
#
# Places = []
#
# with io.open("in//room.txt", 'r') as _file:
#     for line in _file:
#         if line:
#             data = line.split()
#             id = data [0]
#             Room = data[1]
#             capacity = data[2]
#             place = Place(id, Room, capacity)
#             Places.append(place)
#
# print Places
# for Place in Places:
#     print Place
#
# with io.open("out//room.out", 'w') as _file:
#     for Place in Places:
#         _file.write(Place.to_unicode())
#         _file.write(u"\n")

#
# teachers = []
# # 'r'
# # 'w'
# # 'a'
# with io.open("in//teacher.txt", 'r') as _file:
#     for line in _file:
#         if line:
#             # id, firstname, lastname, age, position = line.split()
#             data = line.split()
#             id = data[0]
#             firstname = data[1]
#             lastname = data[2]
#             age = int(data[3])
#             position = data[4]
#             teacher = Teacher(id, firstname, lastname, age, position)
#             # user = User(firstname=firstname, id=id, lastname=lastname, age=age)
#             teachers.append(teacher)
#         # _file.write(unicode(i))
#         # _file.write(u"\n")
# print teachers
# for teacher in teachers:
#     print teacher
#     # print user.to_unicode()
#
#
# with io.open("out//staff.out", 'w') as _file:
#     for teacher in teachers:
#         _file.write(teacher.to_unicode())
#         _file.write(u"\n")
#
# Lessons = []
#
# with io.open("in//lesson.txt", 'r') as _file:
#     for line in _file:
#         if line:
#             data = line.split()
#             id = data [0]
#             name = data[1]
#             lesson = Lesson(id, name, teacher[id(i)])
#             Lessons.append(lesson)
#
# print Lessons
# for Lesson in Lessons:
#     print Lesson
#
# with io.open("out//lesson.out", 'w') as _file:
#     for Lesson in Lessons:
#         _file.write(Lesson.to_unicode())
#         _file.write(u"\n")
#
# Groups = []
#
# with io.open("in//group.txt", 'r') as _file:
#     for line in _file:
#         if line:
#             data = line.split()
#             id = data [0]
#             name = data[1]
#             group = Group(id, name, members[id(i)])
#             Groups.append(group)
#
# print Groups
# for Group in Groups:
#     print Group
#
# with io.open("out//group.out", 'w') as _file:
#     for Group in Groups:
#         _file.write(Group.to_unicode())
#         _file.write(u"\n")
#
# Shedulers = []
#
# with io.open("in//Sheduler.txt", 'r') as _file:
#     for line in _file:
#         if line:
#             data = line.split()
#             id = data [0]
#             room = room
#             lesson = lesson
#             group = Group
#             para = data [0]
#             sheduler = Sheduler(id, room, lesson, group, para)
#             Shedulers.append(sheduler)
#
# print Shedulers
# for Sheduler in Shedulers:
#     print Sheduler
#
# with io.open("out//sheduler.out", 'w') as _file:
#     for Sheduler in Shedulers:
#         _file.write(Sheduler.to_unicode())
#         _file.write(u"\n")
