from operator import itemgetter

class Vendor:
    
    def __init__(self, inventory = []):
        # Make a copy of what's passed in so changes to this instance's 
        # inventory don't affect other vendor's inventories (or other uses of the list being passed in)
        self.inventory = list(inventory)
        
        # Alternatively could have written default as inventory = none,
        # and used 
        # self.inventory = inventory or []
        # This siloes sparate vendor's inventories, 
        # but still doesnot protect against an accidental changing of an underlying list 

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
    
    def swap_items(self, other, my_item, their_item):
        if my_item not in self.inventory or their_item not in other.inventory:
            return False
        else:
            self.inventory.remove(my_item)
            self.inventory.append(their_item)
            other.inventory.remove(their_item)
            other.inventory.append(my_item)
            return True
    
    def swap_first_item(self, other):
        if not self.inventory or not other.inventory:
            return False
        else:
            # Original way I did it:
            # my_first = self.inventory[0]
            # their_first = other.inventory[0]
            # return self.swap_items(other, my_first, their_first)
            
            # Alternative with O(1) time instead of O(n)
            self.inventory[0], other.inventory[0] = other.inventory[0], self.inventory[0]
            return True
        
    def get_best_by_category(self, category):
        category_matches = [(item, item.condition) for item in self.inventory if item.category == category]
        if not category_matches:
            return None
        else:
            # Using itemgetter: This returns a callable to be used on an iterable object, and returns 
            # the specified value from the iterable.             
            # Also note that the 'key' parameter of max allows us to specify a function whose return values 
            # will be used for the comparison
            best = max(category_matches, key = itemgetter(1))[0]
            return best 

    def swap_best_by_category(self, other, my_priority, their_priority):
        my_item = self.get_best_by_category(their_priority) 
        their_item = other.get_best_by_category(my_priority)
        
        if not my_item or not their_item:
            return False
        else:
            return self.swap_items(other, my_item, their_item)
        
    def get_newest_by_category(self, category):
        category_matches = [(item, item.age) for item in self.inventory if item.category == category]
        if not category_matches:
            return None
        else:
            # Using itemgetter: This returns a callable to be used on an iterable object, and returns 
            # the specified value from the iterable.             
            # Also note that the 'key' parameter of min allows us to specify a function whose return values 
            # will be used for the comparison
            newest = min(category_matches, key = itemgetter(1))[0]
            return newest 

    def swap_newest_by_category(self, other, my_priority, their_priority):
        my_item = self.get_newest_by_category(their_priority) 
        their_item = other.get_newest_by_category(my_priority)
        
        if not my_item or not their_item:
            return False
        else:
            return self.swap_items(other, my_item, their_item)
    
 