from user import User

class Teacher(User):
    def __init__(self, id=0, firstname=None, lastname=None, age=0, position=str):
        super(Teacher, self).__init__(id)
        self.firstname = firstname
        self.lastname = lastname
        self.age = age
        self.position = position

    def __str__(self):
        return "id:{} firstname:{} lastname:{} age:{} position: {}".format(self.id, 
                                                                        self.firstname, self.lastname, self.age, self.position)
    def __repr__(self):
        return "{} {} {} {} {}".format(self.id, self.firstname, self.lastname, self.position)

    def to_unicode(self):
        data = "{} {} {} {} {}".format(self.id, self.firstname, self.lastname, self.position)
        return unicode(data)
        