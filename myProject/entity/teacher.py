from user import User

class Teacher(User):
    def __init__(self, id = 0, position = None):
        super(Teacher,self).__init__(id)
        self.position = position
    
    def __str__(self):
        return "id:{} position:{}".format(self.id,
                                          self.position)

    def to_unicode(self):
        data = "{} {}".format(self.id,
                              self.position)
        return unicode(data)
