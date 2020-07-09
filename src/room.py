# Implement a class to hold room information. This should have name and
# description attributes.
import random

class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.inventory = []

    def __str__(self):
        return f'{self.name} \n *** \n {self.description}'

    def spawn_item(self, item):
        spawn = random.randrange(4)
        if spawn == 3:
            self.inventory.append(item)
            print(self.inventory)
        else:
            pass

    def receive_item(self, item):
        print('item', item)
        print('inventory', self.inventory)
        self.inventory.append(item)
