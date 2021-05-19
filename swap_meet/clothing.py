from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition=0, age=1):
        Item.__init__(self, condition, age, "Clothing")

    def __str__(self):
        return("The finest clothing you could wear.")
