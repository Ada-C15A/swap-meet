class Vendor:
    def __init__(self,inventory=[]):
        self.inventory=inventory 
       
    def add(self,item):
        self.inventory.append(item)
        return self.inventory[len(self.inventory)-1]

    def remove(self,item):
        for i in self.inventory:
            if i == item:
                self.inventory.remove(item)
                return item
        return False
    
    def get_by_category(self,accessory):
        print(self.inventory)
        matching_list=[]
        for i in self.inventory:
            print("jj",i)
            if i.category == accessory:
                matching_list.append(i)
        print("see",matching_list)
        return matching_list

    def swap_items(self, friend, my_item, their_item):
        if my_item in self.inventory and their_item in friend.inventory:
            self.inventory.append(their_item)
            self.inventory.remove(my_item)
            friend.inventory.append(my_item)
            friend.inventory.remove(their_item)
            return True
        
        return False
    def swap_first_item(self,friend):
        if self.inventory and friend.inventory:
            self.inventory.append(friend.inventory[0])
            friend.inventory.remove(friend.inventory[0])
            friend.inventory.append(self.inventory[0])
            self.inventory.remove(self.inventory[0])
           
            return True
        return False
    