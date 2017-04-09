from students import students as st
class Student(object):
    def __init__(self, name, age, group, mark):
        self.name = name
        self.age = age
        self.group = group
        self.mark = mark
    def __str__(self):
        return "name:{} age:{} group:{}, mark:{}".format(self.name,
                                                self.age,
                                                self.group,
                                                self.mark)
    def __repr__(self):
        return "{}".format(self.name)

    def isP(self):
        return True if self.age > 20 else False

    def raid(self):
        return sum(self.mark)/len(self.mark)


# students = []
# student = Student("a", 15, "pmi11")
# print student
# students.append(student)

students = [Student(**i) for i in st]
# students = [Student(i["name"], i["age"], i["group"], i["mark"]) for i in st]
print students

for student in students:
    if student.isP():
        print student
print
for student in students:
    if student.group == "pmi11":
        print student
print isinstance(students[0], Student)

print students[0].__class__
for student in students:
    if student.raid() > 4:
        print student
        