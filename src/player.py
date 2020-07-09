# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def __str__(self):
        return f'{self.name} is in {self.current_room}'

    def move(self, current_room, direction):
        self.current_room = current_room
        move = f"{direction}_to"
        if hasattr(current_room, move):
            location = getattr(current_room, move)
            self.current_room = location
            print('You are now in', location)
        else:
            print('You cannot go that way.')