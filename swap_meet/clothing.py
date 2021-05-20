from swap_meet.item import Item
class Clothing(Item):
    def __init__(self, condition=0):
        Item.__init__(self, "Clothing", condition)

    def __str__(self):
        return "The finest clothing you could wear."
