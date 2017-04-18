from base import Base
from datetime import date
from datetime import datetime as dt

class User(Base):
    def __init__(self, id = 0, firstname = None, lastname = None, age = None):
        
        
        super(User,self).__init__(id)
        self.firstname = firstname
        self.lastname = lastname
        # self.age = age
        self.age = age
    
    # def get_age(self):
    #     b_date = dt.strptime(self.b_date, '%d/%m/%Y')
    #     today = date.today()
    #     return today - b_date
    
    def __str__(self):
        return "id:{} firstname:{} lastname:{} age:{}".format(self.id,
                                                                    self.firstname,
                                                                    self.lastname,
                                                                    self.age)

    def to_unicode(self):
        data = "{} {} {} {}".format(self.id,
                                    self.firstname,
                                    self.lastname,
                                    self.age)
        return unicode(data)
