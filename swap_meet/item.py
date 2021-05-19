class Item:
    DEFAULT_ITEM_AGE = 3
    # Note about my using 2 different patterns for making the child classes (Clothing, Decor, Electronics) use the 
    # parent class' default values for condition and age. In production code, I'd use the same pattern for all of these cases 
    # to make the code more consistent and readbale. Here, I'm using 2 different patterns for my own laerning/practice and 
    # to have both as examples to look back on.  
    
    def __init__(self, category = '', condition = 0, age = DEFAULT_ITEM_AGE):
        self.category = category
        self.condition = condition
        self.age = age   

    def __str__(self):
        return "Hello World!"
    
    def condition_description(self):
         descriptions = ["Uh, ya sure you want this?",
                "Remember, all swaps final",
                "Still works",
                "Eh, good enough!",
                "Good enough for company",
                "P-r-i-m-o!"                
         ]
         return descriptions[self.condition]
    
    def age_descriptions(self):
        descriptions = ['0-1 year', '2-5 years', '5-10 years', 'older than 10 years']
        return descriptions[self.age]
     