# Hello, Introduction to Programming Students! Welcome to PA2!
# Your task is to implement the necessary functions in this file.
from io import IOBase
from PIL import Image
import pygame
import threading
import cv2
pygame.mixer.init()
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
    'Grand Hall': {'n': 'Attic', 's': 'Library', 'e': 'Dining Room', 'w': None},
    'Library': {'n': 'Grand Hall', 's': None, 'e': None, 'w': 'Ballroom'},
    'Dining Room': {'n': 'Kitchen', 's': None, 'e': 'Garden', 'w': 'Grand Hall'},
    'Garden': {'n': None, 's': 'Mirror Room', 'e': 'Secret Room', 'w': 'Dining Room'},
    'Secret Room': {'n': None, 's': None, 'e': None, 'w': 'Garden'},
    'Attic': {'n': None, 's': 'Grand Hall', 'e': None, 'w': None},
    'Kitchen': {'n': 'Boss Room', 's': 'Dining Room', 'e': 'Cellar', 'w': None},
    'Cellar': {'n': None, 's': None, 'e': None, 'w': 'Kitchen'},
    'Ballroom': {'n': None, 's': None, 'e': 'Library', 'w': None},
    'Mirror Room': {'n': 'Garden', 's': None, 'e': None, 'w': None},
    'Boss Room': {'n': None, 's': 'Kitchen', 'e': None, 'w': None}
    # TODO TASK 4 EXPAND THE HOUSE
}

room_descriptions = {
    'Grand Hall': "You stand in the majestic Grand Hall.",
    'Library': "You are surrounded by towering ancient books in the Library.",
    'Dining Room': "The dusty Dining Room feels eerily quiet.",
    'Garden': "You find yourself in an overgrown Garden.",
    'Secret Room': "A mysterious Secret Room with a glowing artifact lies ahead.",
    'Attic': "A dark Attic, full of dresses and old clothes.",
    'Kitchen': "You found an abandoned kitchen, theres an old knife laying in the floor.",
    'Cellar': "It looks like the Cellar was used as a brewing room.",
    'Ballroom': "You enter a beautiful ballroom",
    'Mirror Room': "A wonderful place, beautiful for those who don't hate looking at themselves",
    'Boss Room': 'You step into a dark, foreboding chamber with ominous symbols carved into the walls. The air feels heavy.'
}

room_objects = {
    'Library': {'item': 'ancient_book of secrets', 'in_inventory': False},
    'Dining Room': {'item': 'mysterious hidden key', 'in_inventory': False},
    'Secret Room': {'item': 'glowing artifact', 'in_inventory': False},
    'Attic': {'item': 'Dusty Shawl', 'in_inventory': False},
    'Kitchen': {'item': 'Knife', 'in_inventory': False},
    'Cellar': {'item': 'Bubbling Drink', 'in_inventory': False },
    'Ballroom': {'item': 'Spectral Key', 'in_inventory': False},
    'Mirror Room': {'item': 'Broken piece of mirror', 'in_inventory': False},
    # TODO TASK 6 MYSTICAL ARTIFACTS
}


def show_screamer_image(image_path):
    img = cv2.imread(image_path)
    if img is not None:

        cv2.namedWindow('Screamer!', cv2.WINDOW_NORMAL)
        cv2.setWindowProperty('Screamer!', cv2.WND_PROP_FULLSCREEN, cv2.WINDOW_FULLSCREEN)

        cv2.imshow('Screamer!', img)
        cv2.setWindowProperty('Screamer!', cv2.WND_PROP_TOPMOST, 1)


        cv2.waitKey(3000)
        cv2.destroyAllWindows()

        print('''What was THAT! The thing just dissapeared into the nearby door.
        *Spectre side quest started*''')
    else:
        print("Error loading image.")


def play_scream_sound():
    pygame.mixer.music.load(sound_path)
    pygame.mixer.music.play()


def trigger_screamer(image_path, sound_path):
    image_thread = threading.Thread(target=show_screamer_image, args=(image_path,))
    sound_thread = threading.Thread(target=play_scream_sound, args=(sound_path,))

    image_thread.start()
    sound_thread.start()

    image_thread.join()
    sound_thread.join()

def play_scream_sound():
    pygame.mixer.init()
    pygame.mixer.music.load("Grito de mujer aterrada  Efecto de sonido-[AudioTrimmer.com].mp3")
    pygame.mixer.music.play()

image_path = "original-7F3D4BEB-9CF1-4763-B637-B6919E1285CC.jpeg"
sound_path = "Grito de mujer aterrada  Efecto de sonido-[AudioTrimmer.com].mp3"

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
def OpenFrontDoor(inventory, current_room, boss_fight):
    required_items = {
        'ancient_book of secrets',
        'mysterious hidden key',
        'glowing artifact',
        'Dusty Shawl',
        'Bubbling Drink'
    }

    if current_room == "Grand Hall" and required_items.issubset(inventory) and not boss_fight:
        print('''Congrats, you have opened the front door and finally escaped the house
        You kept walking till you arrive at your house, but before you open the door, you feel that something is watching you''')
        play_scream_sound()
        print("The End?")
        exit()
    elif current_room == "Grand Hall" and required_items.issubset(inventory) and boss_fight:
        print('''Congrats, after a long journey, and a tiresome fight, you have opened the front door and finally escaped the house''')
        exit()
    else:
        print("You can't open the front door yet. Make sure you're in the Grand Hall and have 5 items.")


# TODO: Implement `OpenSecretRoom`. This function opens the secret room
#       if the player is in the Garden and possesses the "mysterious hidden key".
def OpenSecretRoom(current_room, inventory):
    if current_room == "Garden" and "mysterious hidden key" in inventory:
        print("You have unlocked the secret room")
        return "Secret Room"
    else:
        print("You can't open the Secret Room yet.")
        return current_room


def OpenBossRoom(current_room, inventory):
    if current_room != "Kitchen":
        print("You can't open this Room yet. But you hear some scary screams inside it.")
        return current_room

    if "Spectral Key" not in inventory:
        print("You can't open this Room yet. But you hear some scary screams inside it.")
        return current_room

    if "Broken piece of mirror" not in inventory:
        print("I can unlock it, but I don't think I'm prepared enough.")
        return current_room

    print("You open the door, ready for the fight that is waiting for you.")
    return "Boss Room"


# TODO: Implement `Get`. This function allows the player to pick up an item
#       in the current room, if it hasn't been picked up yet. Add the item
#       to the player's inventory and mark it as collected.
def Get(current_room, inventory):
    if current_room in room_objects:
        item_info = room_objects[current_room]
        if not item_info['in_inventory']:
            inventory.append(item_info["item"])
            item_info['in_inventory'] = True
            print(f"You have picked up: {item_info['item']}")

            if current_room == 'Kitchen' and item_info["item"] == 'Knife':
                trigger_screamer("original-7F3D4BEB-9CF1-4763-B637-B6919E1285CC.jpeg",
                                 "Grito de mujer aterrada  Efecto de sonido-[AudioTrimmer.com].mp3")

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
def ProcessCommand(command, current_room, inventory, hiding, boss_fight):
    if hiding and command in ['n', 's', 'e', 'w']:
        print("You can't move while hiding. You must stop hiding first.")
        return current_room, hiding

    if command == "o":
        if current_room == "Grand Hall":
            OpenFrontDoor(inventory, current_room, boss_fight)
        elif current_room == "Kitchen":
            current_room = OpenBossRoom(current_room, inventory)
        elif current_room == "Garden":
            current_room = OpenSecretRoom(current_room, inventory)
        else:
            print("There's nothing to open here.")
        return current_room, hiding

    if command in ['n', 's', 'e', 'w']:
        if current_room == "Kitchen" and command == 'n':
            current_room = OpenBossRoom(current_room, inventory)
        else:
            current_room = Move(current_room, command)
        # Trigger specific ghost interactions after moving
        if current_room == 'Dining Room':
            GhostEncounterDinningRoom(current_room)
        elif current_room == 'Library':
            hiding = GhostEncounterLibraryRoom(current_room, hiding)
        elif current_room == 'Garden':
            GhostEncounterGardenRoom(inventory)
        elif current_room == 'Ballroom':
            BallRoomGhost(current_room, inventory)
        elif current_room == 'Boss Room':
            BossFight(current_room, inventory, hiding)
        return current_room, hiding

    elif command == 'm':
        Manual()
    elif command == 'q':
        Quit()
    elif command == 'g':
        current_room = Get(current_room, inventory)
    elif command == 'i':
        ShowInventory(inventory)
    elif command == 'r':
        Read(inventory)
    elif command == 'h':
        hiding = ToggleHide(hiding)
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
def GhostEncounterLibraryRoom(current_room, hiding):
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
#asap
# TODO: Implement `GhostEncounterGardenRoom`. This function makes
#       the player lose an item from their inventory. Remember to update
#       the `room_objects` `in_inventory` to false
def GhostEncounterGardenRoom(inventory):
    print("Remove me and add your code here")

def BallRoomGhost(current_room, inventory):
    if current_room == 'Ballroom' and 'Knife' in inventory:
        print('''A friendly ghost greets you, it looks like he wants to give you something
        Hello there! *said the friendly ghost* You seem scared, 
        I guess you already met the owner of the house, She's really scary, but dont worry, I have something for you.
        He offers you something, will you GET it?''')
        action = input('')

        if action == 'g':
            Get(current_room, inventory)
            print('''This is a Spectral Key, it will help you unlock the door north of the kitchen.
            Only do it if you're prepared for a fight. And before you go, that "Thing" does not like its apperance
            so have that in mind *He winks and dissapears*''')
    else:
        print("Nothing special happens here.")

def BossFight(current_room, inventory, hiding):
    if current_room == 'Boss Room':
        print("The Banshee roars as you step into the room. Its eyes blaze with fury.")
        print("Suddenly, it charges at you! You need to hide quickly!")

        action = input("")
        if action == 'h':
            hiding = ToggleHide(hiding)
            if hiding:
                print("You press yourself against the wall, holding your breath. The Banshee stumbles around, unable to find you.")
        else:
            print("You fail to hide in time, and the Banshee finds you. You have been killed.")
            Quit()

        print('''The creature begins to search for you. You look at the broken piece of mirror in your inventory, and remembered what the ghost told you.
        Will you surprise the Banshee with the mirror? (Press u to use the mirror)''')
        action = input("")
        if action == "u":
            print('''You hold up the broken piece of mirror, catching the Banshee's gaze. It freezes, staring at its reflection with terror.)
            She lets out a guttural scream and reels back, weakened and vulnerable.''')
        else:
            print('''You hesitate, and the creature recovers from its confusion. You have lost your chance.
            You have been killed''')
            Quit()

        print("You need to hide again before it recovers!")
        action = input("What will you do? (h = hide) ")
        if action == 'h':
            hiding = ToggleHide(hiding)
            if hiding:
                print("You slip back into the shadows, avoiding its flailing limbs.")
            else:
                print("You are too slow, and the creature catches sight of you. You have been Killed.")
                Quit()

        print("The creature is disoriented and vulnerable. Now is your chance to finish it!")
        action = input("What will you do? (k = use the knife) ")
        if action == 'k':
            print('''With a burst of courage, you lunge forward and strike with the knife. The creature lets out a final, guttural wail and collapses.")
            You stand victorious, the nightmare is over.''')
        else:
            print("You hesitate, and the creature recovers its strength. You have been killed.")
            Quit()
