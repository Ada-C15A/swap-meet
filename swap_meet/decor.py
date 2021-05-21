from swap_meet.item import Item

class Decor(Item):

    def __init__(self,condition=None):
        super().__init__("Decor", condition)
    
    def __str__(self):
        return "Something to decorate your space."
