from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory 

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self,item):
        if len(self.inventory) > 0:
            for thing in self.inventory:
                if thing == item:
                    self.inventory.remove(item)
                    return item
        return False

    def get_by_category(self,category):
        category_list = []
        for thing in self.inventory:
            if thing.category == category:
                category_list.append(thing)
        return category_list

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.remove(my_item)
            friend.remove(their_item)
            friend.add(my_item)
            self.add(their_item)
            return True
        else:
            return False

    def swap_first_item(self, friend):
        if len(self.inventory) == 0 or len(friend.inventory) == 0:
            return False
        else:
            my_item = self.inventory.pop(0)
            friend.add(my_item)
            their_item = friend.inventory.pop(0)
            self.add(their_item)
            return True

    def get_best_by_category(self, category):
        highest_item = None
        for item in self.inventory:
            if item.category == category:
                if not highest_item:
                    highest_item = item
                else:
                    if highest_item.condition < item.condition:
                        highest_item = item
        return highest_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)
        if my_best and their_best:
            self.swap_items(other,my_best,their_best)
            return True
        else:
            return False