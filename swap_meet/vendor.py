class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False

        self.inventory.remove(item)
        return item

    def get_by_category(self, category):
        category_items = []

        for item in self.inventory:
            if item.category ==  category:
                category_items.append(item)
        return category_items

    def swap_items(self, vendor, my_item, their_item):
        if my_item not in self.inventory or their_item not in vendor.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            vendor.inventory.remove(their_item)
            vendor.inventory.append(my_item)
            return True 
    
    def swap_first_item(self, vendor):
        if len(self.inventory) == 0 or len(vendor.inventory) == 0:
            return False
        else:
            self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
            return True
    
    def get_best_by_category(self, category_str):
        highest_so_far = None

        for item in self.inventory:
            if item.category == category_str:
                if highest_so_far:
                    if item.condition > highest_so_far.condition:
                        highest_so_far = item
                else:
                    highest_so_far = item
        return highest_so_far
