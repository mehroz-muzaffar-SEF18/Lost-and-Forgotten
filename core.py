import json
from time import sleep
import re

global settings
settings={"Null":"Null"}
global entities
entities={"Null":"Null"}
global narrations
narrations={"Null":"Null"}
global visible_entities
visible_entities = []

def print_c(character, char_separator='', sync_print=True):
    print(character, end=char_separator, flush=sync_print)

def display_intro():
    prefix = "\033["
    end = f"{prefix}0m"
    red= f"{prefix}31m"#red
    yellow = f"{prefix}33m"#yellow
    cyan = f"{prefix}36m"#cyan
    green = f"{prefix}32m"#green
    output_narration("Some info before you play the game:\n")
    output_narration(f"1. There are four kinds of entities in this game: {yellow}places{end} shown in yellow, {cyan}interactables{end} shown in cyan, {green}usables{end} shown in green, {red}enemies{end} shown in red\n")
    output_narration(f"2. Syntax: COMMAND ENTITY_NAME\n")
    output_narration(f"3. Commands for {yellow}places{end} are \"walk_into\" and \"look_around\"\n")
    output_narration(f"4. Command for {cyan}interactables{end} is \"interact\"\n")
    output_narration(f"5. Command for {green}usables{end} is \"use\"\n")
    output_narration(f"6. There are no commands for {red}enemies{end}\n")

def load_json_data_from_file(path):
    json_data_file = open(path)
    json_data=json.load(json_data_file)
    json_data_file.close()
    return json_data

def is_json_data_empty(data):
    if "Null" in data.keys():
        return True
    return False

def load_settings():
    global settings
    settings = load_json_data_from_file("settings.json")

def load_entities():
    global entities
    entities = load_json_data_from_file("entities.json")

def load_narrations():
    global narrations
    narrations = load_json_data_from_file("narrations.json")

def update_settings():
    settings_file = open('settings.json', 'w')
    settings_file.write(json.dumps(settings, indent=4))
    settings_file.close()

def color_all_entities_in_narration(narration_text:str):
    global visible_entities
    entities_array=[]
    for category in entities.keys():
        entities_array+=entities[category]
    for entity in entities_array:
        narration_text = re.sub(entity, color_entity_text(entity), narration_text, flags=re.IGNORECASE)
        if narration_text.find(entity) != -1:
            visible_entities.append(entity)
    return narration_text

def output_narration(narration_text):
    speed_map = {
        'Low': 25,
        'Medium': 50,
        'High': 75,
        'Very High': 200
    }
    text_speed=50
    if "text_speed" in settings.keys():
        text_speed=speed_map[settings["text_speed"]]
    character_interval=1/text_speed
    narration_text = color_all_entities_in_narration(narration_text)
    for ch in narration_text:
        sleep(character_interval)
        print_c(ch)

def color_entity_text(item_name):
    prefix = "\033["
    reset = f"{prefix}0m"
    color_category_map={
        "enemies": "31m",#red
        "places": "33m",#yellow
        "interactables": "36m",#cyan
        "usables": "32m"#green
    }
    for category in entities.keys():
        if item_name in entities[category]:
            color_prefix = f"{prefix}{color_category_map[category]}"
            return color_prefix+item_name+reset
    return item_name

def entity_type(entity_name):
    for category in entities.keys():
        if entity_name in entities[category]:
            return category
    return "None"