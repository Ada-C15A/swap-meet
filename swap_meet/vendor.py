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
        items_in_category = []
        for thing in self.inventory:
            if thing.category == category:
                items_in_category.append(thing)
        return items_in_category

    def swap_items(self, vendor, item_to_give, item_to_receive):
        if (
            not item_to_give in self.inventory
            or not item_to_receive in vendor.inventory
        ):
            return False

        self.inventory.remove(item_to_give)
        self.inventory.append(item_to_receive)
        vendor.inventory.remove(item_to_receive)
        vendor.inventory.append(item_to_give)
        return True

    def swap_first_item(self, vendor):
        if not self.inventory or not vendor.inventory:
            return False

        self.swap_items(vendor, self.inventory[0], vendor.inventory[0])
        # other option not using helper method --
        # [self.inventory[0], vendor.inventory[0]] = [
        #     vendor.inventory[0],
        #     self.inventory[0],
        # ]

        return True

    def get_best_by_category(self, item_category):
        applicable_items = self.get_by_category(item_category)

        if not applicable_items:
            return None

        highest_item = applicable_items[0]

        for current_item in applicable_items:
            if highest_item.condition < current_item.condition:
                highest_item = current_item

        return highest_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best = self.get_best_by_category(their_priority)
        their_best = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_best, their_best)

    # ************** OPTIONAL ENHANCEMENT **************
    def swap_by_newest(self, vendor):
        self_newest = self.get_newest_item(self.inventory)
        vendor_newest = self.get_newest_item(vendor.inventory)
        if not self_newest or not vendor_newest:
            return None
        return self.swap_items(vendor, self_newest, vendor_newest)

    @staticmethod
    def get_newest_item(inventory):
        if not inventory:
            return None

        newest_item = None

        for individual_item in inventory:
            if not newest_item:
                if individual_item.age:
                    newest_item = individual_item
            elif individual_item.age:
                if individual_item.age < newest_item.age:
                    newest_item = individual_item

        return newest_item
