from base import Base

class Group(Base):
    def __init__(self, id=0, name=None, members=None):
        """
        :param members (list(User))
        """
        super(Group, self).__init__(id)
        self.name = name
        self.members = members

    def __str__(self):
        template = "id:{} nameGroup:{} members:[".format(self.id, self.name)
        for elem in self.members:
            template += "{} ".format(elem)

        template += "]\n"
        return template
        # return "id:{} nameGroup:{}\nlist user:\n{}".format(self.id,
        #                                                       self.firstname,
        #                                                       self.lastname,
        #                                                       self.age)

    def __repr__(self):
        return "<{} {} {}>".format(self.id, self.name, self.members)

    def to_unicode(self):
        template = "{} {} [".format(self.id, self.name)
        for elem in self.members:
            template += "{} ".format(elem)
        template += "]\n"
        return unicode(template)