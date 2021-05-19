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
        return [item for item in self.inventory if item.category ==  category]
    
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
        if not self.inventory or not vendor.inventory:
            return False
        else:
            my_first = self.inventory.pop(0)
            their_first = vendor.inventory.pop(0)
            self.inventory.append(their_first)
            vendor.inventory.append(my_first)
            return True
        