from base import Base

class Room(Base):
    """docstring for Room"""
    def __init__(self, id=None, name=None, capacity=None):
        super(Room, self).__init__(id)
        self.name = name
        self.capacity = capacity
    def __str__(self):
        return self.get_data_to_save()
