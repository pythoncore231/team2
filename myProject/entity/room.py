from base import Base

class Room(Base):
    def __init__(self, id=0, name=None, capacity=None):
        super(Room, self).__init__(id)
        self.name = name
        self.capacity = int(capacity)

    def __str__(self):
        return "id:{} name:{} capacity:{}".format(self.id,
                                                  self.name,
                                                  self.capacity)

    def __repr__(self):
        return "<{} {}>".format(self.id, self.name)

    def to_unicode(self):
        data = "{} {} {}".format(self.id,
                                 self.name,
                                 self.capacity)
        return unicode(data)