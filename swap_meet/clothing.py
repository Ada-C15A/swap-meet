from .item import Item

class Clothing(Item):
    
    def __init__(self, condition = None):
        if condition == None:
            super().__init__(category = "Clothing")
        else:
            super().__init__(condition = condition, category = "Clothing")
            
    def __str__(self):
        return "The finest clothing you could wear."
