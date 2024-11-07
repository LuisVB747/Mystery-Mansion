from project import (ProcessCommand, room_descriptions, GhostEncounterGardenRoom,
                     GhostEncounterLibraryRoom, GhostEncounterDinningRoom, BossFight, BallRoomGhost, NapstaFight)

def Main():
    current_room = 'Grand Hall'
    inventory = []
    ghost_encountered_dining_room = False
    ghost_encountered_library_room = False
    ghost_encountered_garden_room = False
    ghost_encountered_ballroom = False
    napstablook_encountered = False
    boss_fight = False
    hiding = False

    print(room_descriptions[current_room])

    while True:
        command = input("> ")
        current_room, hiding = ProcessCommand(command, current_room, inventory, hiding, boss_fight)
        if current_room == 'Dining Room' and not ghost_encountered_dining_room:
            GhostEncounterDinningRoom(current_room)
            ghost_encountered_dining_room = True
        if current_room == 'Library' and not ghost_encountered_library_room:
            hiding = GhostEncounterLibraryRoom(current_room,hiding)
            ghost_encountered_library_room = True
        if current_room == 'Garden' and not ghost_encountered_garden_room:
            GhostEncounterGardenRoom(inventory)
            ghost_encountered_garden_room = True
        if current_room == 'Boss Room' and not boss_fight:
            BossFight(current_room, inventory, hiding)
            boss_fight = True
        if current_room == "Ballroom" and not ghost_encountered_ballroom:
            BallRoomGhost(current_room, inventory)
            ghost_encountered_ballroom = True
        if current_room == "NapstaRoom" and not napstablook_encountered:
            NapstaFight(current_room)
            napstablook_encountered = True
print("Welcome to the Haunted Manor Mystery!")
Main()