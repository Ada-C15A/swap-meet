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
        
