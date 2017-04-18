"""lesson.py (=> base)
    name (str)
    teacher (Teacher)"""
from base import Base

class Lesson(Base):
    def __init__(self, id = 0, title = None, teacher = None):
        super(Lesson,self).__init__(id)
        self.title = title
        self.teacher = teacher
        
    def __str__(self):
        return "id:{} firstname:{} lastname:{}".format(self.id,
                                                       self.title,
                                                       self.teacher)
    def to_unicode(self):
        data = "{} {} {}".format(self.id,
                                 self.title,
                                 self.teacher)
        return unicode(data)