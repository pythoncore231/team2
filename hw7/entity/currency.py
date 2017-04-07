"""override __sub__, return dict"""

class CurrencySub(object):
    def __init__(self, date, base, rates):
        self.date = date
        self.base = base
        self.rates = rates

    def __repr__(self):
        return "<{} {}>".format(self.base, self.date)

    def __str__(self):
        template = "{} {}\n".format(self.base, self.date)
        count = 0
        for i in self.rates:
            template += "{}:{}\t".format(i, self.rates[i])
            if not count%8 and count:
                template += "\n"
            # else:
            #     template +=  template += "{}:{}\t".format(i, self.rates[i])
            count += 1
        return template
    
    def __sub__(self, other):
        result = {}
        for i in self.rates:
            result[i]=self.rates[i] - other.rates[i]
        return result

    # def cur_dict(self, rate1, rate2):
    #     for 
    #     return 