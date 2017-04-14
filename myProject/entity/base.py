class Base(object):
    __id = 0
    def __init__(self, id=None):
        if not id:
            id = Base.__id
            Base.__id += 1
        self.id = id

    def to_unicode(self):
        return unicode(self.id)

    def get_data_to_save(self):
        template = ""
        for i in self.__dict__:
            template += "{}:{} ".format(i, eval("self.{}".format(i)))
        return unicode(template[:-1])

    @classmethod
    def create(cls, line):
        line = line.split()
        # ("lastname:l4", "age:8", "id:4", "firstname:f4")
        data = {}
        for pair in line:
            # print pair
            key, value = pair.split(":")
            data[key]=value
        data = cls(**data)
        return data