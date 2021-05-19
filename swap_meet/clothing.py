from .item import Item

class Clothing(Item):
    
    def __init__(self, condition = None, age = Item.DEFAULT_ITEM_AGE):
        if condition == None:
            super().__init__(category = "Clothing", age = age)
        else:
            super().__init__(condition = condition, category = "Clothing", age = age)
            
    def __str__(self):
        return "The finest clothing you could wear."
