from base import Base

class Group(Base):
    def __init__(self, id=0, name=str, members=list):
        super(Group, self).__init__(id)
        self.name = name
        self.members = members
    def __str__(self):
        return "id: {} name: {} members: {}".format(self.id, self.name, self.members)

    def __repr__(self):
        return "{} {} {}".format(self.id, self.name, self.members)

    def to_unicode(self):
        data = "{} {} {}".format(self.id, self.name, [i.to_unicode() for i in self.members])
        return unicode(data)