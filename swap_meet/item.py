class Item:
    def __init__(self, category="", condition=None):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        if self.condition == 5:
            return "Excellent"
        elif self.condition == 4:
            return "good"
        elif self.condition == 3:
            return "acceptable"
        elif self.condition == 2:
            return "worn"
        elif self.condition == 1:
            return "Poor"
        elif self.condition == 0:
            return "Very Poor"
        