# group.py (base)
#     name (str)
#     members (list(User))

from base import Base

class Group(Base):
    def __init__(self, id=0, name=None):
        super(Group, self).__init__(id)
        self.name = name
        self.members = []

    def add_user(self, user):
        self.members.append(user)

    def __str__(self):
        return "id:{} name:{} members:{}".format(self.id,
                                                 self.name,
                                                 self.members)

    def __repr__(self):
        return "<{} {} {}>".format(self.id, self.name, self.members)
    def to_unicode(self):
        data = "{} {} {}".format(self.id,
                                 self.name,
                                 self.members)
        return unicode(data)