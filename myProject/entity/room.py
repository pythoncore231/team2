from base import Base


class Room(Base):
        def __init__(self, id=0, room_number=None, capacity=0):
            super(Room, self).__init__(id)
            self.room_number = room_number
            self.capacity = capacity

        def __str__(self):
            return "id:{} room:{}, capacity:{}".format(self.id,
                                                       self.room_number,
                                                       self.capacity)
        def __repr__(self):
            return "<{} {} {}>".format(self.id, self.room_number, self.capacity)

        def to_unicode(self):
            data = "{} {} {}".format(self.id,
                                     self.room_number,
                                     self.capacity)
            return unicode(data)

