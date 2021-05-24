class Vendor:
    def __init__(self, inventory=None):

        if inventory == None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item):
        if item not in self.inventory:
            return False
        if item in self.inventory:
            self.inventory.remove(item)
            return item

    def get_by_category(self, category):
        category_list = []
        for item in self.inventory:
            if category == item.category:
                category_list.append(item)

        return category_list

    def swap_items(self, someonelse, my_item, someonelse_item):
        if my_item in self.inventory and someonelse_item in someonelse.inventory:
            self.remove(my_item)
            someonelse.add(my_item)
            someonelse.remove(someonelse_item)
            self.add(someonelse_item)
            return True
        else:
            return False

    def swap_first_item(self, someonelse):

        if len(self.inventory) == 0 or len(someonelse.inventory) == 0:
            return False
        else:
            self.swap_items(
                someonelse, self.inventory[0], someonelse.inventory[0])
            return True

    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)
        if not category_list:
            return None
        top_condition = -1
        top_item = None
        for item in category_list:
            if item.condition > top_condition:
                top_condition = item.condition
                top_item = item
        return top_item

    def swap_best_by_category(self, other, my_priority, their_priority):
        item_for_someonelse = self.get_best_by_category(their_priority)
        item_for_myself = other.get_best_by_category(my_priority)
        if item_for_someonelse and item_for_myself:
            self.swap_items(other, item_for_someonelse, item_for_myself)
            return True
        else:
            return False
