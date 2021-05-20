from .item import Item

class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory if inventory else []

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
            if item.category ==  category:
                category_items.append(item)
        return category_items

    def swap_items(self, vendor, my_item, their_item):
        self.vendor = vendor
        self.my_item = my_item
        self.their_item = their_item

        if my_item in self.inventory and their_item in vendor.inventory:
            vendor.add(my_item)
            self.add(their_item)
            self.remove(my_item)
            vendor.remove(their_item)
            return True
        return False

    def swap_first_item(self, vendor):
        if len(self.inventory) > 0 and len(vendor.inventory) > 0:
            self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
            return True
        return False

    def get_best_by_category(self, category):
        best = None

        for item in self.get_by_category(category):
            if best == None:
                best = item
            elif item.condition > best.condition:
                best = item
        return best

        # ****Other option, not sure which one is best
        # list_items = self.get_by_category(category)

        # if len(list_items) > 0:
        #     best = list_items[0]
        #     for item in list_items:
        #         if item.condition > best.condition:
        #             best = item
        #     return best
        # return None

    def swap_best_by_category(self, other, their_priority, my_priority):
        their_item = self.get_best_by_category(their_priority)
        my_item = other.get_best_by_category(my_priority)

        if self.swap_items(other, their_item, my_item):
            return True
        return False


########################SWAP BY NEWEST########################
    def find_newest_item(self):
        newest = None
        if len(self.inventory) > 0:
            for item in self.inventory:
                if newest == None:
                    newest = item
                elif item.age > newest.age:
                    newest = item
        return newest

    def swap_by_newest(self, vendor):
        my_newest = self.find_newest_item()
        vendors_newest = vendor.find_newest_item()

        if my_newest and vendors_newest:
            return self.swap_items(vendor, my_newest, vendors_newest)
        return False