import json
import plistlib
import os
import re


# Function to remove comments from a JSON string
def clean_json(json_str):
    # Remove specific line with "$schema"
    json_str = re.sub(r'"\$schema":.*', "", json_str)
    # Remove // comments
    json_str = re.sub(r"//.*", "", json_str)
    # Remove /* */ comments
    json_str = re.sub(r"/\*[\s\S]*?\*/", "", json_str)
    return json_str


# Define the global settings
global_settings = {
    # ref: https://www.sublimetext.com/docs/color_schemes_tmtheme.html#global_settings
    "settings": {
        "background": "#191919",
        "foreground": "#b3b3b3",
        "caret": "#eaeaea",
        "lineHighlight": "#222222",  # bg for the current line
        "misspelling": "#b07878",  # color to use for the underline drawn under misspelled words
        "accent": "#dad5c8",  # color made available for use by the theme
        "selection": "#303030",  # bg of selected text
        "inactiveSelection": "#242424",  # not currently focused selection
        "gutterForeground": "#474747",  # line number
        "findHighlight": "#474747",  # bg color for match result
        "guide": "#242424",  # indent guide line
        "activeGuide": "#5d5d5d",  # indent guide line for current caret location
        "stackGuide": "#353535",  # parent indent guide line for current caret location
        "bracketsOptions": "foreground",  # next/ previous brackets style
        "bracketsForeground": "#353535",  # next/ previous brackets color
        "bracketContentsOptions": "underline foreground",  # surround bracket style
        "bracketContentsForeground": "#5d5d5d",  # surround bracket color
        "tagsOptions": "underline foreground",  # surround tags style
        "tagsForeground": "#5d5d5d",  # surround tags color
    }
}

# Create the root dictionary for .tmTheme
theme_plist = {  # the file structure of the .tmTheme
    "name": "Color Fatigue",
    "semanticClass": "theme.dark.color-fatigue",
    "colorSpaceName": "sRGB",
    "settings": [global_settings],  # the convert settings will be appended in here
}

# Get the directory of the current script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Construct the path to the vscode_theme.json file in the parent directory
parent_dir = os.path.dirname(script_dir)
json_file_path = os.path.join(parent_dir, "color-fatigue-dark.json")
output_file_path = os.path.join(script_dir, "color-fatigue.tmTheme")

# Load the JSON theme file and process it
with open(json_file_path, "r") as f:
    json_str = f.read()
    json_str_no_comments = clean_json(json_str)
    theme_json = json.loads(json_str_no_comments)

# Convert token colors to .tmTheme settings
for token in theme_json["tokenColors"]:
    scope = token["scope"]
    if isinstance(scope, list):  # if "scope" contain an array of strings
        # join the strings in the list into a single comma-separated string
        scope = ", ".join(scope)
    settings = {"scope": scope, "settings": token["settings"]}
    if "name" in token:  # add name field if exist
        settings["name"] = token["name"]
    theme_plist["settings"].append(settings)

# Save the .tmTheme file
with open(output_file_path, "wb") as f:
    plistlib.dump(theme_plist, f)
