class Vendor:
    def __init__(self, inventory=[]):
        self.inventory = inventory

    def add(self, item):
        self.inventory.append(item)
        return item

    def remove(self, item): 
        if item not in self.inventory:
            return False
        self.inventory = [
            thing for thing in self.inventory if thing != item
            ]
        return item

    def get_by_category(self, category):
        category_items = [
            item for item in self.inventory if item.category == category
        ]
        return category_items
