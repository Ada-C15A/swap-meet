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
        
    def swap_first_item(self, other_vendor): 
        if len(self.inventory ) > 0 and len(other_vendor.inventory) > 0:
            item_1 = self.inventory[0]
            self.inventory.remove(self.inventory[0])
            self.inventory.append(other_vendor.inventory[0])
            other_vendor.remove(other_vendor.inventory[0])
            other_vendor.inventory.append(item_1)
            return True
        else:
            return False
            
    def get_best_by_category(self, category):
        highest = 0.0
        best = None
        for item in self.inventory:
            if item.condition > highest and item.category == str(category):
                best = item
                highest = item.condition
        return best

    def swap_best_by_category(self, other, my_priority, their_priority):
        if not self.inventory or not other.inventory:
            return False
        if not my_priority or not their_priority:
            return False
        
        my_p = other.get_best_by_category(my_priority)
        their_p = self.get_best_by_category(their_priority)

        if (my_p in other.inventory )and (their_p in self.inventory):
            self.swap_items(other, their_p, my_p)
            return True
        else:
            return False


        # if my_priority == None or their_priority == None:
        #     return False
        # if (their_p in self.inventory) and (my_p in other.inventory):
        #     self.swap_items(other, their_p, my_p)
        #     return True
        # else: 
        #     return False
