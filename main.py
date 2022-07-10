import os
import core
from core import *


os.system('color')
# prefix="\033["
# reset=f"{prefix}0m"
# red="31m"

# # arr=["Mehroz", "12"]
# str=f"My name is {prefix}{red}Mehroz{reset}. I am in class 12"
# str.replace("Mehroz", f"")

load_settings()
load_narrations()
load_entities()

game_end=False

output_narration(core.narrations["begining"])

while not game_end:
    print_c("What would you like to do?\n")
    input_words = input("Enter Command: ").split()

    command = input_words[0]
    is_single_word = False
    if len(input_words)>=2:
        entity = input_words[1].capitalize()
    else:
        is_single_word = True
    if command in core.narrations.keys():
        if is_single_word:
            output_narration(core.narrations[command])
        elif entity in core.narrations[command].keys():
            output_narration(core.narrations[command][entity])
        else:
            output_narration(core.narrations["invalid_object"])
    else:
        output_narration(core.narrations["invalid_command"])
    print()


# str = "A man was found unconscious at the shore of an island far far away from the world."
# core.load_settings()
# core.output_narration(str)