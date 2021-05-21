from swap_meet.item import Item

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

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
        cateogry_list = []
        for item in self.inventory:
            if item.category == category :
                cateogry_list.append(item)                
        return cateogry_list

    def swap_items(self, friend, item_give, item_get):
        if item_give in self.inventory and item_get in friend.inventory:
            friend.inventory.append(item_give)
            self.inventory.remove(item_give)
            self.inventory.append(item_get)
            friend.inventory.remove(item_get)
            return True
        else:
            return False

    def swap_first_item(self, friend):
        if self.inventory and friend.inventory:
            self.swap_items(friend, self.inventory[0], friend.inventory[0])
            return True
        else:
            return False

    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        if not category_list:
            return None
        
        best_item = category_list[0]
        for item in category_list:
            if item.condition > best_item.condition:
                best_item = item
        return best_item
        
    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)
        if my_best_item and their_best_item:
            self.swap_items(other, my_best_item, their_best_item)
            return True
        else:
            return False