from swap_meet.item import Item

class Vendor:
    
    def __init__(self, inventory=[], items=[]):
        self.inventory = inventory
        self.items = items 
        
    def add(self, item_to_add):
        self.inventory.append(item_to_add)
        return item_to_add
    
    def remove(self, item_to_remove):
        if item_to_remove in  self.inventory:
            self.inventory.remove(item_to_remove)
            return item_to_remove
        else:
            return False
        
    def get_by_category(self, category):
        item_list = []
        for item in self.inventory:
            if item.category == category:
                item_list.append(item)
        return item_list
    