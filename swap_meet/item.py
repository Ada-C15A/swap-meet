class Item:
    def __init__(self, category="",condition=0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 5:
            return "Brand Spankin' New"
        elif self.condition == 4:
            return "Like New, Still clean enough to eat off of"
        elif self.condition == 3:
            return "Acceptable if you really had to save money"
        elif self.condition == 2:
            return "I wouldnt buy it, but you do you boo boo"
        elif self.condition == 1:
            return "I wouldn't take it even if it were free"
        else:
            return "Worse than a hoarder's trash room, set it on fire"