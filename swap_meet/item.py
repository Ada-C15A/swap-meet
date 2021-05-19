

class Item:
   
    def __init__(self, category, condition):
        self.category = category
        self.condition = condition 
        
    def __str__(self):
        return 'Hello World!'

    def condition_description(self, condition):
        if condition >= 0:
            print ("You must need this really bad.")
        elif condition >= 1:
            print ("It really redefines mediocre.")
        elif condition >= 2:
            print ("The very definition of meh.")
        elif condition >= 3:
            print("Its not great but not bad either!")
        elif condition >= 4:
            print("Its nearly perfect! Great choice!")
        elif condition >= 5:
            print("Absolutely perfect! Just like you!")
        else:
            print("We can't even rate this one!")
