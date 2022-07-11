import os
from tkinter import E
import core
from core import *

os.system('color')

load_settings()
load_narrations()
load_entities()

game_end=False
place_in_view = ""
entered_place = "island"
items_interact_count = {
    "window": 0,
    "door": 0,
    "mirror": 0,
    "drawer": 0,
    "picture": 0,
    "telephone": 0,
    "bed": 0,
    "letters": 0,
    "basement door": 0,
    "first aid kit": 0,
    "four cards": 0,
}
inventory = []

display_intro()
os.system("pause")

print()
output_narration(core.narrations["beginning"])
looked_at_mirror = False
one_time_mirror = True
looked_at_picture = False
one_time_picture = True

while not game_end:
    print_c("\n\nWhat would you like to do?\n\n")
    input_words = input("Enter Command: ").split(" ", 1)
    print()
    command = input_words[0]
    is_single_word = False
    if len(input_words)>=2:
        entity = input_words[1].lower()
    else:
        is_single_word = True
    if command in core.narrations.keys():
        if is_single_word:
            output_narration(core.narrations[command])
            game_end = True
        elif entity in core.narrations[command].keys():
            if entity in visible_entities:
                if entity_type(entity) == "places":
                    if command == "look_around":
                        if entity == entered_place:
                            output_narration(core.narrations[command][entity][0])
                        else:
                            output_narration(core.narrations[command]["error"][0]%entity)
                    elif command == "walk_into":
                        if entity == entered_place:
                            output_narration(core.narrations[command]["error"][0]%entity)
                        else:
                            if entered_place == "house":
                                output_narration(core.narrations[command]["error"][1]%entity)
                            else:
                                if entity=="house":
                                    if items_interact_count["door"]>0:
                                        output_narration(core.narrations[command][entity][0])
                                        entered_place = entity
                                        items_interact_count["door"]=2
                                    else:
                                        output_narration(core.narrations["invalid_timing"])
                                else:
                                    output_narration(core.narrations[command][entity][0])
                                    entered_place = entity
                elif entity_type(entity)=="usables":
                    output_narration(core.narrations[command][entity][0])
                    if entity=="keys":
                        game_end=True
                else:
                    max_interacts = len(core.narrations[command][entity])-1
                    if entity == "mirror":
                        if looked_at_picture and one_time_mirror:
                            items_interact_count[entity]=1
                            looked_at_mirror=True
                            one_time_mirror=False
                        elif looked_at_mirror:
                            items_interact_count[entity]=2
                        else:
                            items_interact_count[entity]=0
                            looked_at_mirror=True
                    elif entity == "picture":
                        if looked_at_mirror and one_time_picture:
                            items_interact_count[entity]=1
                            looked_at_picture=True
                            one_time_picture=False
                        elif looked_at_picture:
                            items_interact_count[entity]=2
                        else:
                            items_interact_count[entity]=0
                            looked_at_picture=True
                    output_narration(core.narrations[command][entity][items_interact_count[entity]])
                    if entity =="door":
                        if entered_place=="house":
                            items_interact_count[entity]+=1
                        else:
                            items_interact_count[entity]=1
                    elif entity != "mirror" and entity !="picture":
                        items_interact_count[entity]+=1
                    items_interact_count[entity] = min(items_interact_count[entity], max_interacts)
            else:
                output_narration(core.narrations["invalid_timing"])
        else:
            e_type = entity_type(entity)
            if e_type =="None":
                output_narration(core.narrations["invalid_object"][1]%entity)
            else:
                output_narration(core.narrations["invalid_object"][0]%(command,e_type[:len(e_type)-1]))
    else:
        output_narration(core.narrations["invalid_command"])