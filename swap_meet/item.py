
class Item():
    def __init__(self, category="", condition=0):
        self.category = category
        self.condition = condition
    
    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
        item_descriptions = [ "Mint", "Excellent", "Good", "Fair", "Poor:", "Trash"]
        item_descriptions = item_descriptions[::-1]
        return item_descriptions[self.condition]
