class Item:
    def __init__(self, category="", condition=0):
        self.category = category if category else ""

    def __str__(self):
        return 'Hello World!'

    def condition_description(self):
        if self.condition == 0:
            return "Just close your eyes & think happy thoughts"
        elif self.condition == 1:
            return "Ehh.. Could be worse... Maybe?"
        elif self.condition == 2:
            return "It'll do..."
        elif self.condition == 3:
            return "You get what you pay for"
        elif self.condition == 4:
            return "Almost perfect"
        elif self.condition == 5:
            return "Like new!"
