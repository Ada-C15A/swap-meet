class Item:
    def __init__(self, category = '', condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 0:
            return "Acceptable"
        elif self.condition == 1:
            return "Functional"
        elif self.condition == 2:
            return "Very good"
        elif self.condition == 3:
            return "A fresh home for tired eyes"
        elif self.condition == 4:
            return "It's new to you"
        elif self.condition == 5:
            return "Amazing!"
