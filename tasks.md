entity

    base.py
        id(int)
	to_unicode()
    room.py (Base)
        name (str)
        capacity (int)
    user.py(=> Base)
        firstname (str)
        lastname (str)
        age (int)
    teacher.py (=> User)
	position (str)
    lesson.py (=> base)
        name (str)
        teacher (Teacher)
    group.py (base)
        name (str)
        members (list(User))
    sheduler.py (=> base)
        room (=> Room)
        lesson (Lesson)
        group (Group)
        para (1,2,3 int)

main.py
* зчитати дані  про кімнати, предмети, користувачів з файлів
* створити дві групи і заповнити користувачами, після чого записати результат у файл 
* на основі вже сформованих даних сформувати довільний розклад і записати у відповідний файл
