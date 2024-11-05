# Hello, Introduction to Programming Students! Welcome to PA2!
# Your task is to implement the necessary functions in this file.
from io import IOBase

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
    if command in ['n', 's', 'e', 'w']:
        next_room = rooms[current_room].get(command)

        if next_room is not None:
            current_room = next_room
            print(room_descriptions[current_room])
        else:
            print('You cant go that way.')
    else:
        print("Invalid command. Use 'n', 's', 'e', or 'w'")

    return current_room
    #done


# TODO: Implement `OpenFrontDoor`. This function checks if the player
#       wins the game. If the player is in the 'Grand Hall' and has 5 items
#       in the inventory, print a victory message and call `exit()`.
def OpenFrontDoor(inventory, current_room):
    if current_room == "Grand Hall" and len(inventory) > 5:
        print("Congrats, you have opened the front door and finally escaped the house")
        exit()
    else:
        print("You can't open the front door yet. Make sure you're in the Grand Hall and have 5 items.")
    #done


# TODO: Implement `OpenSecretRoom`. This function opens the secret room
#       if the player is in the Garden and possesses the "mysterious hidden key".
def OpenSecretRoom(current_room, inventory):
    if current_room == "Garden" and "mysterious hidden key" in inventory:
        print("You have unlocked the secret room")
        return "Secret Room"
    else:
        print("You can't open the Secret Room yet.")
        return current_room
    #done

# TODO: Implement `Get`. This function allows the player to pick up an item
#       in the current room, if it hasn't been picked up yet. Add the item
#       to the player's inventory and mark it as collected.
def Get(current_room, inventory):
    if current_room in room_objects:
        item_inf = room_objects[current_room]
        if not item_inf['in_inventory']:
            inventory.append(item_inf["item"])
            item_inf['in_inventory'] = True
            print(f"You have picked up: {item_inf['item']}")
        else:
            print("You've already picked up this item.")

    else:
        print("There are no items here")

    return current_room

# TODO: Implement `ShowInventory`. This function displays all items in the
#       player's inventory.
def ShowInventory(inventory):
    if inventory:
        print('You currently have:')
        for item in inventory:
            print(f'-{item}')
    else:
        print("You have nothing in your inventory")
    #done

# TODO: Implement `Read`. This function allows the player to read the
#       "ancient_book of secrets" if it's in the inventory.
def Read(inventory):
    if 'ancient_book of secrets' in inventory:
        print('''Where the star shower you'll see
        The secrets from you I wont keep.
        ''')
    else:
        print("You don't have anything to read")
    #done

# TODO: Implement `ToggleHide`. This function toggles the player's hiding
#       state, printing the appropriate message.
def ToggleHide(hiding):
    if hiding:
        print("You're in trouble now")
        return False


    else:
        print("You're now one with the shadows")
        return True


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
    elif command in ['n', 's', 'e', 'w']:
        current_room = Move(current_room, command)
    elif command == 'q':
        Quit()
    elif command == 'o':
        OpenFrontDoor(inventory, current_room)
    elif command == 'g':
        current_room = Get(current_room, inventory)
    elif command == 'i':
        ShowInventory(inventory)
    elif command == 'r':
        Read(inventory)
    elif command == 'h':
        hiding = ToggleHide(hiding)
    elif current_room == "Garden" and command == 'g':
        current_room = OpenSecretRoom(current_room, inventory)
    else:
        print("Invalid command.")

    return current_room, hiding

# TASK 3 GHOST INTERACTIONS -------------------------------------------+
# TODO: Implement `GhostEncounterDinningRoom`. This function presents
#       the player with a riddle and checks if they solve it correctly.
def GhostEncounterDinningRoom(current_room):
    if current_room == 'Dining Room':
        print('''You have encounter the ghost! The ghost presents you a riddle:
        "In the shadows, I lurk at night,
        with my haunting, presence, I bring fright.
        Count the bones of the dead, you'll see,
        What number am I, as eerie as can be?"''')
        answer = input('What will you respond?')
        if answer != '206':
            print("You're wrong. The ghost has decided to kill you because of your ignorance")
            Quit()
        else:
            print("You're correct. The ghost has decided to let you go.")

# TASK 5 MORE GHOSTS -------------------------------------------+
# TODO: Implement `GhostEncounterLibraryRoom`. This function tells
#       the player to hide. If they fail to hide, they lose the game.
def GhostEncounterLibraryRoom(current_room):
    if current_room == 'Library':
        print('''Oh no! There's a ghost, you must hide!''')
        action = input("")

        if action == 'h':
            hiding = ToggleHide(hiding)
            print('The ghost has vanished.')
        else:
            print('You failed to hide. The ghost has killed you.')
            Quit()

    return hiding

# TODO: Implement `GhostEncounterGardenRoom`. This function makes
#       the player lose an item from their inventory. Remember to update
#       the `room_objects` `in_inventory` to false
def GhostEncounterGardenRoom(inventory):
    print("Remove me and add your code here")
