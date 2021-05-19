class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item in self.inventory:
            self.inventory.remove(item)
        else:
            return False
        return item

    def get_by_category(self, category):
        items_in_category = []
        for thing in self.inventory:
            if thing.category == category:
                items_in_category.append(thing)
        return items_in_category

    def swap_items(self, vendor, item_to_give, item_to_receive):
        if item_to_give in self.inventory and item_to_receive in vendor.inventory:
            self.inventory.remove(item_to_give)
            self.inventory.append(item_to_receive)
            vendor.inventory.remove(item_to_receive)
            vendor.inventory.append(item_to_give)
            return True
        else:
            return False

    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False
        [self.inventory[0], vendor.inventory[0]] = [
            vendor.inventory[0],
            self.inventory[0],
        ]
        return True
