import os
import core


os.system('color')
prefix="\033["
reset=f"{prefix}0m"
red="31m"

# arr=["Mehroz", "12"]
str=f"My name is {prefix}{red}Mehroz{reset}. I am in class 12"
str.replace("Mehroz", f"")
print(str)

# str = "A man was found unconscious at the shore of an island far far away from the world."
# core.load_settings()
# core.output_narration(str)