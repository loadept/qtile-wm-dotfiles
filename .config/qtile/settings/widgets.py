"""
QTHEME CONFIGURATION
Module for defining widget configurations in Qtile.
"""

from libqtile import widget
from libqtile.widget.base import _Widget


widget_defaults = dict(
    font="UbuntuMono Nerd Font",
    fontsize=16,
    padding=3,
)
extension_defaults = widget_defaults.copy()

def arch_logo (config) -> list[_Widget]:
    return [
        widget.TextBox(
            text='   ',
            foreground=config["arch_logo"]["foreground"],
            background=config['bar'],
            fontsize=22,
        ),
        widget.Sep(
            foreground=["#f1ffff", "#f1ffff"],
            background=config['bar']
        ),
        widget.Spacer(
            length=20,
            background=config['bar'],
        ),
    ]

def groupbox (config) -> list[_Widget]:
    return [
        widget.GroupBox(
            foreground=["#f1ffff", "#f1ffff"],
            background=config['bar'],
            font='UbuntuMono Nerd Font',
            fontsize=20,
            margin_y=3,
            margin_x=0,
            padding_y=8,
            padding_x=5,
            borderwidth=1,
            active=["#f1ffff", "#f1ffff"],
            inactive=["#525050", "#525050"],
            rounded=False,
            highlight_method='block',
            this_current_screen_border=config['current_window']['this_current_screen_border'],
            this_screen_border=["#5c5c5c", "#5c5c5c"],
            other_current_screen_border=config['bar'],
            other_screen_border=config['bar'],
        ),
        widget.WindowName(
            foreground=config['window_name']['foreground'],
            background=config['bar'],
        ),
        widget.Sep(
            background=config['bar'],
            foreground=config['bar'],
        ),
    ]

def checkupdates (config) -> list[_Widget]:
    return [
        widget.TextBox(
            text="󱈙 ",
            padding=-10.5,
            fontsize=37,
            foreground=config['bar'],
            background=config['widget_update']['arrow']['background'],
        ),
        widget.TextBox(
            text=" ",
            foreground=config['widget_update']['icon']['foreground'],
            background=config['widget_update']['arrow']['background'],
        ),
        widget.CheckUpdates(
            foreground=config['widget_update']['checkupdates']['foreground'],
            background=config['widget_update']['arrow']['background'],

            display_format='{updates}',
            colour_have_updates=config['widget_update']['checkupdates']['foreground'],
            custom_command='checkupdates',
            update_interval=1900,
        ),
    ]

def memory_state (config) -> list[_Widget]:
    return [
        widget.TextBox(
            text="󱈙 ",
            padding=-12,
            fontsize=37,
            foreground=config['widget_update']['arrow']['background'],
            background=config['widget_memory']['arrow']['background'],
        ),
        widget.TextBox(
            text='󰍛 ',
            foreground=config['widget_memory']['icon']['foreground'],
            background=config['widget_memory']['arrow']['background'],
        ),
        widget.Memory(
            format="{MemUsed:.0f}{mm} / {MemTotal:.0f}{mm}",
            foreground=config['widget_memory']['memory']['foreground'],
            background=config['widget_memory']['arrow']['background'],
        ),
        widget.Sep(
            foreground=config['widget_memory']['arrow']['background'],
            background=config['widget_memory']['arrow']['background'],
        ),
    ]

def current_layout (config) -> list[_Widget]:
    return [
        widget.TextBox(
            text="󱈙 ",
            padding=-12,
            fontsize=37,
            foreground=config['widget_memory']['arrow']['background'],
            background=config['widget_layout']['arrow']['background'],
        ),
        widget.CurrentLayout(
            mode='icon',
            scale = 0.6,
            background=config['widget_layout']['arrow']['background'],
        ),
        widget.CurrentLayout(
            foreground=config['widget_layout']['layout']['foreground'],
            background=config['widget_layout']['arrow']['background'],
        ),
    ]

def time_date (config) -> list[_Widget]:
    return [
        widget.TextBox(
            text="󱈙 ",
            padding=-12,
            fontsize=37,
            foreground=config['widget_layout']['arrow']['background'],
            background=config['widget_clock']['arrow']['background'],
        ),
        widget.TextBox(
            text='󰃰 ',
            foreground=config['widget_clock']['icon']['foreground'],
            background=config['widget_clock']['arrow']['background'],
        ),
        widget.Clock(
            format="%d/%m/%Y ",
            foreground=config['widget_clock']['clock']['foreground'],
            background=config['widget_clock']['arrow']['background'],
        ),
        widget.Sep(
            foreground=config['widget_clock']['sep']['foreground'],
            background=config['widget_clock']['arrow']['background'],
        ),
        widget.Clock(
            format=" %I:%M %p",
            foreground=config['widget_clock']['clock']['foreground'],
            background=config['widget_clock']['arrow']['background'],
        ),
        widget.Sep(
            foreground=config['widget_clock']['arrow']['background'],
            background=config['widget_clock']['arrow']['background'],
        ),
    ]

def system_tray (config) -> list[_Widget]:
    return [
        widget.TextBox(
            text="󱈙 ",
            padding=-11,
            fontsize=37,
            foreground=config['widget_clock']['arrow']['background'],
            background=config['bar'],
        ),
        widget.Systray(
            background=config['bar'],
        ),
    ]

def main_widgets (config: dict) -> list[_Widget]:
    return (
        arch_logo(config) +
        groupbox(config) +
        checkupdates(config) +
        memory_state(config) +
        current_layout(config) +
        time_date(config) +
        system_tray(config)
    )

def secondary_widgets (config: dict) -> list[_Widget]:
    return (
        arch_logo(config) +
        groupbox(config)[::-1]
    )
