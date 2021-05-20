

class Item:

    def __init__(self, category='', condition=None):
        self.category = category
        self.condition = condition
        
    def __str__(self):
        return 'Hello World!'

    def condition_description(self):
        if self.condition == 0:
            return ("You must need this really bad.")
        elif self.condition == 1:
            return ("It really redefines mediocre.")
        elif self.condition == 2:
            return ("The very definition of meh.")
        elif self.condition == 3:
            return("Its not great but not bad either!")
        elif self.condition == 4:
            return("Its nearly perfect! Great choice!")
        elif self.condition == 5:
            return("Absolutely perfect! Just like you!")
        else:
            return("We can't even rate this one!")
