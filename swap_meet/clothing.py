from typing import cast
from .item import Item
from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, category="Clothing", condition=0):
        super().__init__(category, condition)
        # if condition == None:
        #     super().__init__(category="Clothing")
        # else:
        #     super().__init__(category="Clothing", condition=None)
    
    def __str__(self): #overwritten the string method
        return "The finest clothing you could wear."
    
