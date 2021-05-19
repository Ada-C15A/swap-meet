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