"""
QTHEME CONFIGURATION
Module for defining screen configurations in Qtile.
"""

from libqtile import bar
from libqtile.config import Screen
from .widgets import main_widgets, secondary_widgets
from .theme import json_theme, config
import subprocess


screens = [
    Screen(**{
        json_theme.get('position'): bar.Bar(main_widgets(config), 21, opacity=0.99)
    }),
]

command = subprocess.run(
    'xrandr | grep -w "connected" | cut -d " " -f 2 | wc -l',
    shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
)

if command.returncode != 0:
    monitors = 1
else:
    monitors = int(command.stdout.decode('UTF-8'))

for i in range(1, monitors):
    screens.append(
        Screen(**{
            json_theme.get('position'): bar.Bar(secondary_widgets(config), 21, opacity=0.99)
        }),
    )
