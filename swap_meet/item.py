class Item:
    def __init__(self, category='', condition=0.0):
        self.category = category

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0.0:
            return "Oh, no, no, no, no, no"
        elif self.condition == 1.0:
            return "Yeah, but no"
        elif self.condition == 2.0:
            return "It's risky"
        elif self.condition == 3.0:
            return "Could be better"
        elif self.condition == 4.0:
            return "We can overlook minor issues"
        elif self.condition == 5.0:
            return "Can't go wrong with this."
        else:
            return "Not sure what condition this is in"