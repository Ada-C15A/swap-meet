from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory
        self.item = Item()

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:
            return False

    def get_by_category(self, category):
        matched_categories = []
        for item in self.inventory:
            if str(item.category) == category:
                matched_categories.append(item)
        return matched_categories
