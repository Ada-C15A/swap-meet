from swap_meet.item import Item

class Clothing(Item):
    def __init__(self, condition=0):
        super().__init__(category="Clothing",condition=0)
      
    def __str__(self):
        return "The finest clothing you could wear."
    
    def condition_description(self):
        print(super().condition_description())
        return super().condition_description()