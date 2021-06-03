from .item import Item

class Decor(Item):
    
    def __init__(self, condition = None, age = Item.DEFAULT_ITEM_AGE):
        if condition == None:
            super().__init__(category = "Decor", age = age)
        else:
            super().__init__(condition = condition, category = "Decor", age = age)
    
    def __str__(self):
        return "Something to decorate your space."
