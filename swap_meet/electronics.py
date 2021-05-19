from swap_meet.item import Item


class Electronics(Item):
    def __init__(self, category="Electronics", condition=0):
        super().__init__(category, condition)

    def __str__(self):
        return super().__str__("A gadget full of buttons and secrets.")

    def condition_description(self):
        return super().condition_description()
