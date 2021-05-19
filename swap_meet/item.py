class Item:
   
    def __init__(self, category = '', condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
         descriptions = {0 :"Uh, ya sure you want this?",
                1 : "Remember, all swaps final",
                2 : "Still works",
                3 : "Eh, good enough!",
                4 : "Good enough for company",
                5 : "P-r-i-m-o!"                
                }
         return descriptions[self.condition]