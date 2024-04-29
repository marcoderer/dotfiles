#  ╭──────────────────────────╮  #
#  │   ____ ___ _ _    ____   │  #
#  │   |  |  |  | |    |___   │  #
#  │   |_\|  |  | |___ |___   │  #
#  │                          │  #
#  ╰──────────────────────────╯  #
#   ======= QUTILITIES =======   #

import json
from os import path
from settings.paths import qtile_path, theme_file
import subprocess
from libqtile.log_utils import logger
from libqtile.lazy import lazy
from libqtile import qtile

class QTheme(dict):
    """dot notation access to theme elements"""
    def __init__(self, theme_data,*args, **kwargs): 
        super().__init__(*args, **kwargs)
        
        if isinstance(theme_data, dict):
            for k, v in theme_data.items():
                if isinstance(v, dict):
                    self[k] = QTheme(v)
                else:
                    self[k] = v
        else:
            raise Exception(
                f"Error in file qutils.py, class QTheme:\n"\
                f"Can't create a theme object from\n {theme_data}"
            )

    def __getattr__(self, attr):
        return self.get(attr)


def load_theme():
    if path.isfile(theme_file):
        with open(theme_file, "r") as f:
            theme = json.load(f)
            return QTheme(theme)
    else:
        raise Exception(f"'{theme_file}' does not exist.")

def count_monitors():
    connected_monitors = 1
    xrandr = "xrandr | grep -w 'connected' | cut -d ' ' -f 2 | wc -l"

    command = subprocess.run(
        xrandr,
        shell=True,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )

    if command.returncode != 0:
        error = command.stderr.decode("UTF-8")
        logger.error(f"Failed counting monitors using {xrandr}:\n{error}")
    else:
        connected_monitors = int(command.stdout.decode("UTF-8"))

    return connected_monitors

# Mouse_callback functions
def open_powermenu():
    qtile.cmd_spawn("power")


### UNUSED FUNCTIONS, MAY BECOME HANDY ONE DAY ###
### v   v   v   v   v   v   v   v   v   v   v  ###

# Notifier functions
def dunst():
    return subprocess.check_output(["./.config/qtile/dunst.sh"]).decode("utf-8").strip()


def toggle_dunst():
    qtile.cmd_spawn("./.config/qtile/dunst.sh --toggle")


def toggle_notif_center():
    qtile.cmd_spawn("./.config/qtile/dunst.sh --notif-center")


def open_launcher():
    qtile.cmd_spawn("rofi -show drun")

def kill_window():
    qtile.cmd_spawn("xdotool getwindowfocus windowkill")


def open_pavu():
    qtile.cmd_spawn("pavucontrol")




# Resize functions for bsp layout


def resize(qtile, direction):
    layout = qtile.current_layout
    child = layout.current
    parent = child.parent

    while parent:
        if child in parent.children:
            layout_all = False

            if (direction == "left" and parent.split_horizontal) or (
                direction == "up" and not parent.split_horizontal
            ):
                parent.split_ratio = max(5, parent.split_ratio - layout.grow_amount)
                layout_all = True
            elif (direction == "right" and parent.split_horizontal) or (
                direction == "down" and not parent.split_horizontal
            ):
                parent.split_ratio = min(95, parent.split_ratio + layout.grow_amount)
                layout_all = True

            if layout_all:
                layout.group.layout_all()
                break

        child = parent
        parent = child.parent


@lazy.function
def resize_left(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "left")
    elif current == "columns":
        layout.cmd_grow_left()


@lazy.function
def resize_right(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "right")
    elif current == "columns":
        layout.cmd_grow_right()


@lazy.function
def resize_up(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "up")
    elif current == "columns":
        layout.cmd_grow_up()


@lazy.function
def resize_down(qtile):
    current = qtile.current_layout.name
    layout = qtile.current_layout
    if current == "bsp":
        resize(qtile, "down")
    elif current == "columns":
        layout.cmd_grow_down()


def show_keys():
    key_help = ""
    for k in keys:
        mods = ""

        for m in k.modifiers:
            if m == "mod4":
                mods += "Super + "
            else:
                mods += m.capitalize() + " + "

        if len(k.key) > 1:
            mods += k.key.capitalize()
        else:
            mods += k.key

        key_help += "{:<30} {}".format(mods, k.desc + "\n")

    return key_help


# Padding
def padding(qtile, direction):
    if direction == "+":
        qtile.current_screen.left.size += 18
        qtile.current_screen.top.size += 9
        qtile.current_screen.right.size += 18
        qtile.current_screen.bottom.size += 9
        qtile.current_group.layout_all()
    elif direction == "-":
        qtile.current_screen.left.size -= 18
        qtile.current_screen.top.size -= 9
        qtile.current_screen.right.size -= 18
        qtile.current_screen.bottom.size -= 9
        qtile.current_group.layout_all()
    else:
        qtile.current_screen.left.size = 18
        qtile.current_screen.top.size = 77
        qtile.current_screen.right.size = 18
        qtile.current_screen.bottom.size = 18
        qtile.current_layout.margin = 9
        qtile.current_group.layout_all()


@lazy.function
def inc_pad(qtile):
    padding(qtile, "+")


@lazy.function
def dec_pad(qtile):
    padding(qtile, "-")


@lazy.function
def reset_pad(qtile):
    padding(qtile, "reset")


@lazy.function
def inc_margins(qtile):
    qtile.current_layout.margin += 9
    qtile.current_group.layout_all()


@lazy.function
def dec_margins(qtile):
    qtile.current_layout.margin -= 9
    qtile.current_group.layout_all()
