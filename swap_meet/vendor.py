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
       
    def get_best_by_category(self,item_category):
        matched_category_list = self.get_by_category(item_category)

        if len(matched_category_list) > 1:
            best_item = matched_category_list[0]
            for item in matched_category_list:
                if item.condition > best_item.condition:
                    best_item = item
            return best_item
        elif len(matched_category_list) == 0:
            return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = other.get_best_by_category(my_priority)
        their_item = self.get_best_by_category(their_priority)
        return self.swap_items(other, their_item, my_item)
