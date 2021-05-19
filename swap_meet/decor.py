from swap_meet.item import Item

class Decor(Item):
    def __init__(self, condition=0, age=1):
        Item.__init__(self, condition, age, "Decor")

    def __str__(self):
        return("Something to decorate your space.")
