class Item:
    def __init__(self, category = '', condition = 0):
        self.category = category
        self.condition = condition

    def __str__(self):
        return "Hello World!"

    def condition_description(self):
        condition_descriptions = {
            0: "still has tags",
            1: "mint",
            2: "good",
            3: "some signs of wear",
            4: "as is",
            5: "may actually be garbage"
        }
        return condition_descriptions[self.condition]