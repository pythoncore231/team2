import io
from entity.user import User


# users = []
# # 'r'
# # 'w'
# # 'a'
# with io.open("in//user.txt", 'r') as _file:
#     for line in _file:
#         if line:
#             # id, firstname, lastname, age = line.split()
#             data = line.split()
#             id = data[0]
#             firstname = data[1]
#             lastname = data[2]
#             age = int(data[3])
#             user = User(id, firstname, lastname, age)
#             # user = User(firstname=firstname, id=id, lastname=lastname, age=age)
#             users.append(user)
#         # _file.write(unicode(i))
#         # _file.write(u"\n")
# print users
# for user in users:
#     print user
#     # print user.to_unicode()

# for user in users:
#     user.age -=5

# for user in users:
#     print user

# with io.open("out//user.out", 'w') as _file:
#     for user in users:
#         _file.write(user.to_unicode())
#         _file.write(u"\n")
'''
###########################################################################################################
'''

# from entity.room import Room

# rooms = []
# with io.open("in//room.txt", 'r') as room_file:
#     for str_room in room_file:
#         if str_room:
#             id, name, capacity = str_room.split()
#             capacity = int(capacity)
#             room = Room(id=id, name=name, capacity=capacity)
#             rooms.append(room)
# print rooms
# for room in rooms:
#     print room
#     room.capacity += 2
#     print room.to_unicode()



# with io.open("out//room.txt", 'w') as room_file:
#     for room in rooms:
#         room_file.write(room.to_unicode())
#         room_file.write(u"\n")

'''
###########################################################################################################
'''
from entity.sheduler import Scheduler
from entity.teacher import Teacher
from entity.lesson import Lesson
from entity.group import Group
from entity.user import User
from entity.room import Room

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

groups = []
group_1 = Group(1, "pmi33", [u for u in users if u.age % 2])
groups.append(group_1)
group_2 = Group(2, "pmi52", [u for u in users if not u.age % 2])
groups.append(group_2)
group_3 = Group(3, "pmi12", [u for u in users if u.age >= 23])
groups.append(group_3)
group_4 = Group(4, "pmi42", [u for u in users if u.age < 23])
groups.append(group_4)
group_5 = Group(5, "pmi32", [u for u in users if u.age == 30])
groups.append(group_5)


with io.open("out//group.txt", 'w') as group_file:
    for group in groups:
        group_file.write(group.to_unicode())
        group_file.write(u"\n")


rooms = []
with io.open("in//room.txt", 'r') as room_file:
    for str_room in room_file:
        if str_room:
            id, name, capacity = str_room.split()
            capacity = int(capacity)
            room = Room(id=id, name=name, capacity=capacity)
            rooms.append(room)

schedulers = []

teacher = Teacher(id=id, firstname=firstname, lastname=lastname, age=age, position="position")
lesson = Lesson(id=id, name=name, teacher=teacher)

 # id=0, room=None, lesson=None, group=None, para=None)
scheduler = Scheduler(1, rooms[0], lesson, group_1, 2)
schedulers.append(scheduler)
scheduler = Scheduler(2, rooms[1], lesson, group_2, 2)
schedulers.append(scheduler)
scheduler = Scheduler(3, rooms[2], lesson, group_3, 1)
schedulers.append(scheduler)
scheduler = Scheduler(4, rooms[3], lesson, group_4, 1)
schedulers.append(scheduler)
scheduler = Scheduler(3, rooms[4], lesson, group_5, 1)
schedulers.append(scheduler)


with io.open("out//scheduler.txt", 'w') as scheduler_file:
    for scheduler in schedulers:
        scheduler_file.write(scheduler.to_unicode())
        scheduler_file.write(u"\n")

for i in schedulers:
    print i
    print i.to_unicode()

# with io.open("in//scheduler.txt", 'r') as scheduler_file:
#     for line in scheduler_file:
#         if line:
#             id, room, lesson, group, para = line.split()
#             teacher = Teacher(id=id, firstname=firstname, lastname=lastname, age=age, position=position)
#             lesson = Lesson(id=id, name=name, teacher=teacher)
#             group = Group(id=id, name=name, members=members)
















