class Item:

    def __init__(self, category="", condition=""):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        item_conditions = ["noooowayyyy", "ugghhh", "umm...", "eh?", "ooohhh", "ahhhh!"]
        return item_conditions[self.condition]