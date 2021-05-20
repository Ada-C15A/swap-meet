class Item:
    def __init__(self, category="", condition=0, age=0):
        self.category = category if category else ""
        self.condition = condition
        self.age = age

    def __str__(self):
        return 'Hello World!'

    def condition_description(self):
        condition_desc = ["Just close your eyes & think happy thoughts", "Ehh.. Could be worse... Maybe?", "It'll do...", "You get what you pay for", "Almost perfect", "Like new!"]
        return condition_desc[self.condition]
