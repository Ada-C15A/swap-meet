class Item:
    def __init__(self, category="", condition=0, age=None ):
        self.category = category
        self.condition = condition
        self.age = age

    def __str__(self, return_message="Hello World!"):
        return return_message

    def condition_description(self):
        condition_description = {
            0: "Buy at your own risk",
            1: "ok",
            2: "more ok",
            3: "kind of ok",
            4: "Better",
            5: "Best",
        }
        return condition_description[self.condition]
