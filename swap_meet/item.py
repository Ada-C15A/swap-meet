class Item:
    def __init__(self, condition=0, age=1, category=""):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self):
        return("Hello World!")

    def condition_description(self):
        decriptions = ["Are you sure?", "Iffy", "Maybe", "Solid", "Good", "Mint"]
        return decriptions[self.condition]

    def age_description(self):
        decriptions = ["New", "Loved", "Retro", "Antique", "Ancient"]
        return decriptions[self.condition]
