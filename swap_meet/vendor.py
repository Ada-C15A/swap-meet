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
        category_items = []
        for item in self.inventory:
            if item.category == category:
                category_items.append(item)
        return category_items

    def swap_items(self, vendor, my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            self.inventory.remove(my_item) #takes my item
            self.inventory.append(their_item) #adds it to theirs
            vendor.inventory.remove(their_item) #removes theirs
            vendor.inventory.append(my_item) #adds it to mine
            return True 
        else:
            return False
    
    def swap_first_item(self, vendor):
        if len(self.inventory) > 0 and len(vendor.inventory) > 0:
            my_item = self.inventory[0]
            their_item = vendor.inventory[0]
            self.swap_items(vendor, my_item, their_item)
            return True
        else:
            return False

    def get_best_by_category(self, category):
        category_matches = []

        for item in self.inventory:
            if item.category == category:
                category_matches.append(item)

        if len(category_matches) > 0:
            highest_ranked_item = category_matches[0]
            for item in category_matches:
                if item.condition > highest_ranked_item.condition:
                    highest_ranked_item = item
            return highest_ranked_item
            
        return None

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_best_item = self.get_best_by_category(their_priority)
        their_best_item = other.get_best_by_category(my_priority)

        if my_best_item and their_best_item:
            self.swap_items(other, my_best_item, their_best_item)
            return True
        else:
            return False