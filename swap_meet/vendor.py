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
            if item.category == category:
                matched_categories.append(item)
        return matched_categories
    
    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        else:
            my_item_to_switch = self.remove(my_item)
            their_item_to_switch = other_vendor.remove(their_item)
            self.add(their_item_to_switch)
            other_vendor.add(my_item_to_switch)
            return True
    
    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        else:
            my_first_item = self.inventory[0]
            their_first_item = other_vendor.inventory[0]
            my_removed_item = self.remove(my_first_item)
            thier_removed_item = other_vendor.remove(their_first_item)
            self.add(thier_removed_item)
            other_vendor.add(my_removed_item)
            return True
