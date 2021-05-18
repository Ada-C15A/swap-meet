from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition=0, age=1):
        Item.__init__(self, condition, age, "Electronics")

    def __str__(self):
        return("A gadget full of buttons and secrets.")