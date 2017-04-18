from base import Base

class Scheduler(Base):
    def __init__(self, id=0, room=None, lesson=None, group=None, para=None):
        super(Scheduler, self).__init__(id)
        self.room = room
        self.lesson = lesson
        self.group = group
        self.para = para

    def __str__(self):
        return "id: {} room: {} lesson: {} group: {} para: {}".format(self.id, self.room, self.lesson, self.group, self.para)

    def __repr__(self):
        return "{} {} {} {} {}".format(self.id, self.room, self.lesson, self.group, self.para)

    def to_unicode(self):
        data = "{} {} {} {} {}".format(self.id, self.room, self.lesson, self.group.to_unicode(), self.para)
        return unicode(data)
