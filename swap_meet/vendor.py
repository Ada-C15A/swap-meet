class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item): 
        if item not in self.inventory:
            return False
        self.inventory = [
            thing for thing in self.inventory if thing != item
            ]
        return item

    def get_by_category(self, category):
        category_items = [
            item for item in self.inventory if item.category == category
        ]
        return category_items

    def swap_items(self, other_vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in other_vendor.inventory:
            return False
        other_vendor.remove(their_item)
        self.remove(my_item)
        other_vendor.add(my_item)
        self.add(their_item)
        return self.inventory

    def swap_first_item(self, other_vendor):
        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
        my_item = self.inventory[0]
        their_item = other_vendor.inventory[0]
        return self.swap_items(other_vendor, my_item, their_item)
        
    def get_best_by_category(self, category):
        category_items = self.get_by_category(category)
        if len(category_items) == 0:
            return None
        best_condition = 0
        for item in category_items:
            if item.condition > best_condition:
                best_condition = item.condition
                best_item = item
        return best_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        their_best = other.get_best_by_category(my_priority)
        my_best = self.get_best_by_category(their_priority)
        return self.swap_items(other, my_best, their_best)
