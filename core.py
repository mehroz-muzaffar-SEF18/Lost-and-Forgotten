import json
import string
from time import sleep

from numpy import true_divide
import re

global settings
settings={"Null":"Null"}
global entities
entities={"Null":"Null"}
global narrations
narrations={"Null":"Null"}

def print_c(character, char_separator='', sync_print=True):
    print(character, end=char_separator, flush=sync_print)

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
    entities_array=[]
    for category in entities.keys():
        entities_array+=entities[category]
    for entity in entities_array:
        narration_text = re.sub(entity, color_entity_text(entity), narration_text, flags=re.IGNORECASE)
        # narration_text=narration_text.replace(entity, color_entity_text(entity))
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
        "pickables": "32m"#green
    }
    for category in entities.keys():
        if item_name in entities[category]:
            color_prefix = f"{prefix}{color_category_map[category]}"
            return color_prefix+item_name+reset
    return item_name

