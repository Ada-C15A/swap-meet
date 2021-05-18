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
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item in self.inventory and their_item in other_vendor.inventory:
            self.inventory.remove(my_item)
            other_vendor.inventory.remove(their_item)
            self.inventory.append(their_item)
            other_vendor.inventory.append(my_item)
            return True
        else:
            return False