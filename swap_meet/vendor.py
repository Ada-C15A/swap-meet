from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory = None):
        self.inventory = inventory or []

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
            return item
        return False

    def get_by_category(self, category):
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and \
            their_item in vendor.inventory:
            self.remove(my_item)
            self.add(their_item)
            vendor.remove(their_item)
            vendor.add(my_item)
            return True
        return False
    
    def swap_first_item(self, vendor):
        if len(self.inventory) > 0 and len(vendor.inventory) > 0:
            return self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
        else:
            return False
    
    def get_best_by_category(self, category):
        item_options = [item for item in self.inventory if item.category == category]
        if item_options:
            best_item = item_options[0]
            for item in item_options:
                if item.condition > best_item.condition:
                    best_item = item
            return best_item
        return None
    
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if my_best and their_best:
            return self.swap_items(other, my_best, their_best)
        return False