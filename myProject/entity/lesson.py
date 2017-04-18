from base import Base

class Lesson(Base):
    def __init__(self, id=0, name=None, teacher=None):
        super(Lesson, self).__init__(id)
        self.name = name
        self.teacher = teacher
    def __str__(self):
        return "id: {} name: {} teacher: {}".format(self.id, self.name, self.teacher)

    def __repr__(self):
        return "{} {} {}".format(self.id, self.name, self.teacher)

    def to_unicode(self):
        data = "{} {} {}".format(self.id, self.name, self.teacher)
        return unicode(data)
