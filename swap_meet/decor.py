from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition=None):
        if condition == None:
            super().__init__(category="Decor")
        else:
            super().__init__(condition = condition, category = "Decor")
        
        
    def __str__(self):
        return "Something to decorate your space."

    def condition_description(self):
        return super().condition_description()