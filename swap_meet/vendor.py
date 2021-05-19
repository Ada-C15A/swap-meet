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
    