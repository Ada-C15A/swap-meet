from swap_meet.item import Item

class Electronics(Item):
    def __init__(self):
        super().__init__(category="Electronics", condition=0)
        
    def __str__(self):
        return "A gadget full of buttons and secrets."

    def condition_description(self):
        return super().condition_description()