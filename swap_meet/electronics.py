from swap_meet.item import Item

class Electronics(Item):
    def __init__(self, condition=None):
        if condition == None:
            super().__init__(category="Electronics")
        else:
            super().__init__(condition = condition, category = "Electronics")
    
        
        
    def __str__(self):
        return "A gadget full of buttons and secrets."

    def condition_description(self, condition=0):
        return super().condition_description()