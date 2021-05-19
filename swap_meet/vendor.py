from operator import attrgetter
class Vendor:
    def __init__(self, inventory = []):
        self.inventory = inventory

    def add(self,item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        else:  return False
    
    def get_by_category(self,category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.remove(my_item)
            self.add(their_item)
            vendor.remove(their_item)
            vendor.add(my_item)
            return True
        else: return False
    
    def swap_first_item(self, vendor):
        if len(self.inventory) > 0 and len(vendor.inventory) > 0:
            my_item = self.inventory[0]
            their_item = vendor.inventory[0]
            self.swap_items(vendor, my_item, their_item)
            return True
        else: return False

    def get_best_by_category(self, category):
        items = [item for item in self.inventory if item.category == category]
        if len(items) > 0:
            best_item = items[0]
            for item in items:
                if item.condition > best_item.condition:
                    best_item = item
            return best_item
        else: return None
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if my_best and their_best:
            self.swap_items(other, my_best, their_best)
            return True
        else: return False

    def get_newest_by_category(self,category=None):
        if category == None:
            items = self.inventory
        else:
            items = [item for item in self.inventory if item.category == category]
        if len(items) > 0:
            newest = None
            for item in items:
                if not newest or item.age < newest.age:
                    newest = item
            return newest
        else: return None

    def swap_newest_by_category(self, other, my_priority=None, their_priority=None):
        if len(self.inventory) > 0 and len(other.inventory) > 0:
            my_newest = self.get_newest_by_category(their_priority)
            their_newest = other.get_newest_by_category(my_priority)
            if my_newest and their_newest:
                self.swap_items(other, my_newest, their_newest)
                return True
            else: return False
        else: return False
