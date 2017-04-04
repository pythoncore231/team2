students = [{"name":"a","age":15, "group":"pmi11", "mark":(3,2,3,4)},
            {"name":"b","age":16, "group":"pmi21", "mark":(3,2,3,4)},
            {"name":"c","age":103, "group":"pmi31", "mark":(5,5,5,5)},
            {"name":"d","age":21, "group":"pmi12", "mark":(3,2,3,4)},
            {"name":"e","age":55, "group":"pmi41", "mark":(5,2,3,4)},
            {"name":"f","age":32, "group":"pmi41", "mark":(4,2,3,4)},
            {"name":"g","age":21, "group":"pmi11", "mark":(3,2,3,4)}]

def print_group(list_students, group):
    for i in list_students:
        if i["group"] == group:
            print i

def isP(student):
    return True if student["age"] > 20 else False

if __name__ == '__main__':

    print_group(students, "pmi11")
    print
    for i in students:
            if isP(i):
                print i

