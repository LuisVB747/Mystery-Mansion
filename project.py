# Hello, Introduction to Programming Students! Welcome to PA2!
# Your task is to implement the necessary functions in this file.

# In this assignment, we will work with dictionaries. Dictionaries are a
# data structure used to store data in key-value pairs.
# For more information, visit:
# https://docs.python.org/3/tutorial/datastructures.html#dictionaries

# DICTIONARIES ------------------------------------------------+
# The main dictionaries you will be working with are `rooms`,
# `room_descriptions`, and `room_objects`:
#   - `rooms`: Contains the room name as the key, and the value is
#     another dictionary where the key is a direction (e.g., 'n' for north)
#     and the value is the adjacent room.
#     Example: rooms['Library'] -> {'n': 'Grand Hall'}
#   - `room_descriptions`: Contains the room name as the key and a
#     description of the room as the value.
#   - `room_objects`: Contains the room name as the key, and the value is
#     a dictionary. One key is `item`, which stores the name of the item
#     in the room, and another key is `in_inventory`, a boolean indicating
#     whether the item has been picked up.

rooms = {
    'Grand Hall': {'n': None, 's': 'Library', 'e': 'Dining Room', 'w': None},
    'Library': {'n': 'Grand Hall', 's': None, 'e': None, 'w': None},
    'Dining Room': {'n': None, 's': None, 'e': 'Garden', 'w': 'Grand Hall'},
    'Garden': {'n': None, 's': None, 'e': None, 'w': 'Dining Room'},
    'Secret Room': {'n': None, 's': None, 'e': None, 'w': 'Garden'},
    # TODO TASK 4 EXPAND THE HOUSE
}

room_descriptions = {
    'Grand Hall': "You stand in the majestic Grand Hall.",
    'Library': "You are surrounded by towering ancient books in the Library.",
    'Dining Room': "The dusty Dining Room feels eerily quiet.",
    'Garden': "You find yourself in an overgrown Garden.",
    'Secret Room': "A mysterious Secret Room with a glowing artifact lies ahead."
}

room_objects = {
    'Library': {'item': 'ancient_book of secrets', 'in_inventory': False},
    'Dining Room': {'item': 'mysterious hidden key', 'in_inventory': False},
    'Secret Room': {'item': 'glowing artifact', 'in_inventory': False},
    # TODO TASK 6 MYSTICAL ARTIFACTS
}


# TASK 1 COMMANDS FUNCTIONS -----------------------------------------------------+
# Your first task is to implement the functions for each command.
# Commands represent the input from the player.

# TODO: Implement `Move`. This function updates the player's current room
#       when a valid movement command ('n', 's', 'e', 'w') is given.
#       If the move is valid, update the `current_room` and print the
#       room's description (use `room_descriptions`). If invalid,
#       print "You can't go that way."
def Move(current_room, command):
    print("Remove me and add your code here")
    return current_room


# TODO: Implement `OpenFrontDoor`. This function checks if the player
#       wins the game. If the player is in the 'Grand Hall' and has 5 items
#       in the inventory, print a victory message and call `exit()`.
def OpenFrontDoor(inventory, current_room):
    print("Remove me and add your code here")


# TODO: Implement `OpenSecretRoom`. This function opens the secret room
#       if the player is in the Garden and possesses the "mysterious hidden key".
def OpenSecretRoom(current_room, inventory):
    print("Remove me and add your code here")

# TODO: Implement `Get`. This function allows the player to pick up an item
#       in the current room, if it hasn't been picked up yet. Add the item
#       to the player's inventory and mark it as collected.
def Get(current_room, inventory):
    print("Remove me and add your code here")

# TODO: Implement `ShowInventory`. This function displays all items in the
#       player's inventory.
def ShowInventory(inventory):
    print("Remove me and add your code here")


# TODO: Implement `Read`. This function allows the player to read the
#       "ancient_book of secrets" if it's in the inventory.
def Read(inventory):
    print("Remove me and add your code here")

# TODO: Implement `ToggleHide`. This function toggles the player's hiding
#       state, printing the appropriate message.
def ToggleHide(hiding):
    print("Remove me and add your code here")
    return False


# Available Commands -------------------------------------------+
# This function displays all possible player commands.
def Manual():
    print(
        "Available Commands:\n"
        "n = move north\n"
        "s = move south\n"
        "e = move east\n"
        "w = move west\n"
        "o = open an object (e.g. door)\n"
        "g = get an item in the room\n"
        "i = display inventory\n"
        "r = read an item (e.g., book)\n"
        "h = hide/unhide\n"
        "m = show commands\n"
        "q = quit the game\n"
    )


# Exit the game ------------------------------------------------+
def Quit():
    print("Thanks for playing!")
    exit()

# TASK 2 PROCESS COMMAND -----------------------------------------------------+
# TODO: Complete the `ProcessCommand` function. It should check
#       the player's command and call the respective function.
def ProcessCommand(command, current_room, inventory, hiding):
    if command == 'm':
        Manual()
    elif command == 'q':
        Quit()
    else:
        print("Invalid command.")

    return current_room, hiding

# TASK 3 GHOST INTERACTIONS -------------------------------------------+
# TODO: Implement `GhostEncounterDinningRoom`. This function presents
#       the player with a riddle and checks if they solve it correctly.
def GhostEncounterDinningRoom():
    print("Remove me and add your code here")

# TASK 5 MORE GHOSTS -------------------------------------------+
# TODO: Implement `GhostEncounterLibraryRoom`. This function tells
#       the player to hide. If they fail to hide, they lose the game.
def GhostEncounterLibraryRoom():
    print("Remove me and add your code here")
    return True

# TODO: Implement `GhostEncounterGardenRoom`. This function makes
#       the player lose an item from their inventory. Remember to update
#       the `room_objects` `in_inventory` to false
def GhostEncounterGardenRoom(inventory):
    print("Remove me and add your code here")
