# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room
        self.inventory = []

    def __str__(self):
        return f'{self.name} is in {self.current_room}'

    def move(self, current_room, direction):
        move = f"{direction}_to"
        if hasattr(current_room, move):
            location = getattr(current_room, move)
            self.current_room = location
            print('You are now in', location)
        else:
            print('You cannot go that way.')

    def take(self, item):
        self.inventory.append(item)
        print(f"You now have {self.inventory}")

    def drop(self, item):
        self.inventory.remove(item)
        print(f"You now have {self.inventory}")