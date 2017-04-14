from base import Base

class User(Base):
    def __init__(self, id=0, firstname=None, lastname=None, age=0):
        super(User, self).__init__(id)
        self.firstname = firstname
        self.lastname = lastname
        self.age = int(age)

    def __str__(self):
        return "id:{} firstname:{} lastname:{} age:{}".format(self.id,
                                                              self.firstname,
                                                              self.lastname,
                                                              self.age)

    def __repr__(self):
        return "<{} {}>".format(self.id, self.firstname)

    def to_unicode(self):
        data = "{} {} {} {}".format(self.id,
                                    self.firstname,
                                    self.lastname,
                                    self.age)
        return unicode(data)