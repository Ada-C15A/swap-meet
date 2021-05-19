from swap_meet.item import Item

class Decor(Item):
    def __init__(self, category="Decor"):
        self.category = category

    def __str__(self):
        return "Something to decorate your space."
