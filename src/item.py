class Item:
    def __init__(self, name, *description):
        self.name = name
        self.description = description
        print('description', self.description)

    def on_take(self, name):
        print(f"You have picked up {self.name}")

    def on_drop(self, name):
        print(f"You have dropped {self.name}")

    def __str__(self, name, description):
        return f"{self.name}, {self.description}"