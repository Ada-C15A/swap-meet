class Item:
    def __init__(self, category="", condition=0.0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        if self.condition < 0:
            return "You should not have brought this home"
        elif 0.0 <= self.condition <= 1.0:
            return "Whole lotta gross"
        elif 1.1 <= self.condition <= 2.0:
            return "approaching mediocre"
        elif 2.1 <= self.condition <= 3.0:
            return "not completely terrible"
        elif 3.1 <= self.condition <= 4:
            return "almost the least terrible"
        elif 4.1 <= self.condition == 5.0:
            return "Best of what we got"
        elif self.condition > 5:
            return "something completely unexpected"
