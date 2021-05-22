from swap_meet.item import Item

class Vendor():
    def __init__(self, inventory=[]): # if the vendor has a list use it, if not, use the default empty list
        # if not inventory: # take optional inventory by checking if the inventory is valid, (has a list of things)
        #     # self.inventory = [] # create list
        # else: 
        self.inventory = inventory
        self.item = Item()

    def add(self, item):
        self.inventory.append(item)
        return item
    
    def remove(self, item):
        if item in self.inventory: 
            self.inventory.remove(item) #list of items that have a category
            return item
        else:
            return False
    
    def get_by_category(self, category):
        return_list = []
        for item in self.inventory:
            if item.category == category:
                return_list.append(item)
        return return_list
        # It takes one argument: a string, representing a category
        # method returns a list of Items in the inventory with that category

    def swap_items(self, other_vendor, my_item, other_item):
        # iterate through the inventory list and look for my_item
        if my_item not in self.inventory or other_item not in other_vendor.inventory: # is my item in the inventory list?
            return False

        self.remove(my_item)
        self.add(other_item)
        other_vendor.remove(other_item)
        other_vendor.add(my_item)
        return True

    def swap_first_item(self, other_vendor):
        self.inventory 
        other_vendor.inventory

        if len(self.inventory) == 0 or len(other_vendor.inventory) == 0:
            return False
    
        my_item = self.inventory[0] 
        other_item = other_vendor.inventory[0]
        
        self.swap_items(other_vendor, my_item, other_item)
        return True
        
    def get_best_by_category(self, category):
        category_list = self.get_by_category(category)

        if len(category_list) > 1:
            highest_condition_item = category_list[0]
            for item in category_list:
                if item.condition > highest_condition_item.condition:
                    highest_condition_item = item
            return highest_condition_item
        else:
            return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority)
        their_item = other.get_best_by_category(my_priority)

        return self.swap_items(other, my_item, their_item)

        
