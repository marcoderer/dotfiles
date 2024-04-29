#  ╭──────────────────────────╮  #
#  │   ____ ___ _ _    ____   │  #
#  │   |  |  |  | |    |___   │  #
#  │   |_\|  |  | |___ |___   │  #
#  │                          │  #
#  ╰──────────────────────────╯  #
#   ==== DIRECTORY PATHS =====   #

from os import path
import json

qtile_path = path.join(path.expanduser('~'), ".config", "qtile")
cfg_file = path.join(qtile_path, "config.json")

# Directories from config.json
with open(cfg_file, "r") as f:
    cfg = json.load(f)

icons_dir = cfg["path"]["icons"]
wallp_dir = cfg["path"]["wallpapers"]
scrots_dir = cfg["path"]["screenshots"]
themes_dir = cfg["path"]["themes"]
scrot_form = cfg["scrot_file_format"]
# Theme cfg_file
theme_file = path.join(themes_dir,f"{cfg["theme"]}.json")

# Timestamped screenshot file
scrot = path.join(scrots_dir, f"{scrot_form}.png")

# Wallpaper
wallpaper = path.join(wallp_dir,cfg["wallpaper"])
