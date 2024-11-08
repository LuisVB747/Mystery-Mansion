from project import (ProcessCommand, room_descriptions, GhostEncounterGardenRoom,
                     GhostEncounterLibraryRoom, GhostEncounterDinningRoom, BossFight, BallRoomGhost, NapstaFight)
import pygame

pygame.mixer.init()

def play_music(file_path):
    pygame.mixer.music.stop()
    pygame.mixer.music.load(file_path)
    pygame.mixer.music.play(-1)

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

    play_music("Undertale OST - Waterfall Extended.mp3")
    background_music_playing = True

    while True:
        command = input("> ")
        previous_room = current_room
        current_room, hiding = ProcessCommand(command, current_room, inventory, hiding, boss_fight)

        if current_room != previous_room:
            if current_room == 'NapstaRoom':
                play_music("Ghost Fight (#10) - Undertale Music Extended.mp3")
                background_music_playing = False
            elif current_room == 'Boss Room':
                play_music("再臨_片翼の天使 Advent_ One-Winged Angel.mp3")
                background_music_playing = False
            elif current_room == "Kefka's Lair":
                play_music("Final Fantasy VI 6 Terra's Theme SNES Version.mp3")
                background_music_playing = False
            else:
                if not background_music_playing:
                    play_music("Undertale OST - Waterfall Extended.mp3")
                    background_music_playing = True

        if current_room == 'Dining Room' and not ghost_encountered_dining_room:
            GhostEncounterDinningRoom(current_room)
            ghost_encountered_dining_room = True
        if current_room == 'Library' and not ghost_encountered_library_room:
            hiding = GhostEncounterLibraryRoom(current_room, hiding)
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
