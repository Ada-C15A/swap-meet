from swap_meet.item import Item
class Vendor:
    def __init__(self, inventory = []):
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

    # Instances of Vendor have an instance method named swap_items
    # It takes 3 arguments:
    # an instance of another Vendor, representing the friend that the vendor is swapping with
    # an instance of an Item (my_item), representing the item this Vendor instance plans to give
    # an instance of an Item (their_item), representing the item the friend Vendor plans to give
    def swap_items(self, vendor,  my_item, their_item):
        if my_item in self.inventory and their_item in vendor.inventory:
            # It removes the my_item from this Vendor's inventory,
            self.remove(my_item)
            # and adds it to the friend's inventory
            self.add(their_item)
            # It removes the their_item from the other Vendor's inventory,
            vendor.remove(their_item)
            # and adds it to this Vendor's inventory 
            vendor.add(my_item)
            # it returns True 
            return True
        # If this Vendor's inventory doesn't contain my_item or the friend's inventory doesn't contain their_item, the method returns False
        return False