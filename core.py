import json
from time import sleep

global settings
settings={"Null":"Null"}

def print_c(character, char_separator='', sync_print=True):
    print(character, end=char_separator, flush=sync_print)

def load_settings():
    settings_file = open('settings.json')
    global settings
    settings = json.load(settings_file)
    settings_file.close()

def update_settings():
    settings_file = open('settings.json', 'w')
    settings_file.write(json.dumps(settings, indent=4))
    settings_file.close()

def output_narration(narration_text):
    speed_map = {
    'Low': 25,
    'Medium': 50,
    'High': 75
    }
    text_speed=50
    if "text_speed" in settings.keys():
        text_speed=speed_map[settings["text_speed"]]
    character_interval=1/text_speed
    for ch in narration_text:
        sleep(character_interval)
        print_c(ch)
