from .item import Item

class Electronics(Item):
    
    def __init__(self, condition = None, age = Item.DEFAULT_ITEM_AGE):
        if condition == None:
            super().__init__(category = "Electronics", age = age)
        else:
            super().__init__(condition = condition, category = "Electronics", age = age)
    
    def __str__(self):
        return "A gadget full of buttons and secrets."

