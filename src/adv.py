from room import Room
from player import Player

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


# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']

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
    print(player)
    choice = True
    while choice == True:
        user_input = input('Which way will you go? [n] [s] [w] [e] or [q] to quit ')
        user_commands = ['n', 's', 'e', 'w']
        if user_input == 'q':
            choice = False
            game = False
        elif user_input in user_commands:
            player.move(player.current_room, user_input)
        # elif user_input == 'n':
        #     player.move(player.current_room, 'n')
        # elif user_input == 's':
        #     player.move(player.current_room, 's')
        # elif user_input == 'w':
        #     player.move(player.current_room, 'w')
        # elif user_input == 'e':
        #     player.move(player.current_room, 'e')
        else:
            print('Please select a valid option')