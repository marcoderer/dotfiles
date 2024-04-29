#  ╭──────────────────────────╮  #
#  │   ____ ___ _ _    ____   │  #
#  │   |  |  |  | |    |___   │  #
#  │   |_\|  |  | |___ |___   │  #
#  │                          │  #
#  ╰──────────────────────────╯  #
#   ======= KEYBINDINGS ======   #

from libqtile.config import Key, KeyChord
from libqtile.command import lazy
from .paths import scrot

mod = "mod4"


terminal = "kitty"
file_browser = "thunar"
browser = "firefox"

# gamma values to use as nightlight (n) and daylight (d)
n = {
    "r": "0.95", 
    "g": "0.85",
    "b": "0.90", 
}
d = {
    "r": "0.95", 
    "g": "0.95",
    "b": "0.95", 
}

keys = [Key(key[0], key[1], *key[2:]) for key in [

    # Switch between windows in current stack pane
    ([mod], "j", lazy.layout.down()),
    ([mod], "k", lazy.layout.up()),
    ([mod], "h", lazy.layout.left()),
    ([mod], "l", lazy.layout.right()),
    ([mod], "space", lazy.layout.next()),

    # Change window sizes (MonadTall)
    ([mod, "shift"], "l", lazy.layout.grow()),
    ([mod, "shift"], "h", lazy.layout.shrink()),

    # Reset layout
    ([mod], "n", lazy.layout.normalize()),

    # Toggle floating
    ([mod, "shift"], "f", lazy.window.toggle_floating()),

    # Toggle fullscreen
    ([mod], "f", lazy.window.toggle_fullscreen()),

    # Move windows up or down in current stack
    ([mod, "shift"], "j", lazy.layout.shuffle_down()),
    ([mod, "shift"], "k", lazy.layout.shuffle_up()),

    # Toggle between different layouts
    ([mod], "Tab", lazy.next_layout()),
    ([mod, "shift"], "Tab", lazy.prev_layout()),

    # Kill window
    ([mod], "w", lazy.window.kill()),

    # Switch focus of monitors
    ([mod], "semicolon", lazy.next_screen()),
    ([mod], "comma", lazy.prev_screen()),

    # Restart Qtile
    ([mod, "control"], "r", lazy.restart()),

    # Quit Qtile
    ([mod, "control"], "q", lazy.shutdown()),

    # Spawn command using a prompt widget
    ([mod], "r", lazy.spawncmd()),

    # Show applications menu
    ([mod], "m", lazy.spawn("rofi -show drun")),

    # Window Nav
    ([mod, "shift"], "m", lazy.spawn("rofi -show")),

    # Browser
    ([mod], "b", lazy.spawn(browser)),

    # File Explorer
    ([mod], "e", lazy.spawn(file_browser)),

    # Terminal
    ([mod], "t", lazy.spawn(terminal)),

    # Nightlight (dependencies: x11-xserver-utils (debian) )
    ([mod, "shift"], "n", lazy.spawn(
        f"xgamma -rgamma {n["r"]} -ggamma {n["g"]} -bgamma {n["b"]}"
    )),

    # Daylight (dependencies: x11-xserver-utils (debian) )
    ([mod, "shift"], "d", lazy.spawn(
        f"xgamma -rgamma {d["r"]} -ggamma {d["g"]} -bgamma {d["b"]}"
    )),
]]
keys.extend(
    [ # check: Key([], "Print", lazy.spawn("scrot /home/piyush/Pictures/Screenshot-%d-%m-%Y_%H:%M:%S_$wx$h.png -e 'xclip -selection clipboard -t image/png -i $f'"), desc="Print screen and copy to clipboard"),
        # Screenshots
        KeyChord([mod], "s", [
            # dependencies: scrot, flameshot
            Key(key[0], key[1], *key[2:]) for key in [
                # Screenshot by selection or rectangle
                ([], "s", lazy.spawn(f"scrot -s {scrot}")),
                # Screenshot with highlighted area
                ([], "h", lazy.spawn(f"scrot -shole {scrot}")),
                # Screenshot with blurred area
                ([], "b", lazy.spawn(f"scrot -sblur,30 {scrot}")),
                # Screenshot with Flameshot
                ([], "f", lazy.spawn("flameshot")),
            ]],
            name = 'Screenshot mode'
        ),
        # Volume
        KeyChord([mod], "v", [
            # dependencies: pulseaudio-utils
            Key(key[0], key[1], *key[2:]) for key in [
                ([], "j", lazy.spawn(
                    "pactl set-sink-volume @DEFAULT_SINK@ -5%"
                )),
                ([], "k", lazy.spawn(
                    "pactl set-sink-volume @DEFAULT_SINK@ +5%"
                )),
                ([], "m", lazy.spawn(
                    "pactl set-sink-mute @DEFAULT_SINK@ toggle"
                )),
            ]],
            mode = True,
            name = 'Adjust Volume'
        ),
    ]
)
