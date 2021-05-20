from .item import Item

class Electronics(Item):
    def __init__(self, category="Electronics", condition=0, age=0):
        self.category =  category
        self.condition = condition
        self.age = age

    def __str__(self):
        return 'A gadget full of buttons and secrets.'