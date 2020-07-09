from room import Room
from player import Player
from item import Item

# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}

loot = {
    "gold": Item("Gold Coin", "Shiny and valuable"),
    "ruby": Item("Cut Ruby", "This should be worth something"),
    "dagger": Item("Rusty Dagger", "Could be useful if I encounter enemies"),
    "car keys": Item("Missing Car Keys", "Ah, there they are! Knew I left them somewhere...")
}


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

# Item spawn
room["outside"].spawn_item('gold')
room["foyer"].spawn_item("gold")
room["overlook"].spawn_item("ruby")
room["narrow"].spawn_item("dagger")
room["treasure"].spawn_item("car keys")

#
# Main
#

# Make a new player object that is currently in the 'outside' room.

# Write a loop that:
#
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
#
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

game = True
while game == True:
    player1 = input("Welcome player, what is your name? ")
    player = Player(player1, room['outside'])
    print(f"Welcome, {player1}. You have stumbled into this RPG and must now find the treasure. You are currently in {player.current_room}.")
    choice = True
    while choice == True:
        nav_commands = ['n', 's', 'e', 'w']
        user_input = input('What will you do? [n] [s] [w] [e] to move, [i] or [inventory] \n to view inventory [search] to search, or [q] to quit ')
        if user_input == 'q':
            choice = False
            game = False
        elif user_input in nav_commands:
            player.move(player.current_room, user_input)
        elif user_input == "search":
            print(player.current_room.inventory)
            print(type(player.current_room.inventory))
            if len(player.current_room.inventory) > 0:
                item = player.current_room.inventory.pop(0)
                print(f"There is {item} in {player.current_room}. What will you do?")
                interaction = input(f"[take {item}] or [leave {item}]? ")
                if interaction == f"take {item}":
                    player.take(item)
                    print(loot[item])
                    # loot[Item].on_take(item)
                else:
                    player.current_room.receive_item(item)
        elif user_input == "i" or "inventory":
            print(player.inventory)
        else:
            print('Please select a valid option')