"""group.py (base)
    name (str)
    members (list(User))"""

from base import Base

class Group(Base):
    def __init__(self, id = 0, group_n = None, members = None):
        super(Group,self).__init__(id)
        self.group_n = group_n
        self.members = members
        
    def __str__(self):
        return "id:{} firstname:{} lastname:{}".format(self.id,
                                                       self.group_n,
                                                       self.members)
    def to_unicode(self):
        data = "{} {} {}".format(self.id,
                                 self.group_n,
                                 self.members)
        return unicode(data)