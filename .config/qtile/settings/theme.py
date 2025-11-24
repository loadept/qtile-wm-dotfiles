"""
QTHEME CONFIGURATION
Module for managing theme settings in Qtile.
"""

import json
import os


def set_theme ():
    user_path = os.path.expanduser('~')
    theme_selector_path = os.path.join(user_path, '.config', 'qtile', 'themes', 'theme_selector.json')

    with open(theme_selector_path, 'r') as file:
        json_theme = json.load(file)
        theme_path = os.path.join(user_path, '.config', 'qtile', 'themes', json_theme['theme'] + '.json')
        
        with open(theme_path) as json_file:
            data = json.load(json_file)
    return json_theme, data

if __name__ == "settings.theme":
    json_theme, config = set_theme()
