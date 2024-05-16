#    ,ad8888ba,             88  88
#   d8"'    `"8b     ,d     ""  88
#  d8'        `8b    88         88
#  88          88  MM88MMM  88  88   ,adPPYba,
#  88          88    88     88  88  a8P_____88
#  Y8,    "88,,8P    88     88  88  8PP"""""""
#   Y8a.    Y88P     88,    88  88  "8b,   ,aa
#    `"Y8888Y"Y8a    "Y888  88  88   `"Ybbd8"'
#
######### ===== CONFIGURATION ====== ############

import subprocess
import re
import os
from libqtile import bar, layout, widget, hook, qtile
from libqtile.config import Click, Drag, Group, Key, Match, Screen, KeyChord
from libqtile.lazy import lazy
from libqtile.log_utils import logger
from libqtile.utils import send_notification
from qtile_extras import widget
from qtile_extras.widget.decorations import RectDecoration

mod = "mod4"
scrot = "home/marco/Pictures/Screenshots/%Y-%m-%d-%H%M%S.png"
terminal = "kitty"
file_browser = "thunar"
browser = "firefox"
calculator = "qalculate"
home = os.path.expanduser("~")
scripts = home + "/.config/qtile/scripts/"


def show_keybindings(keys):
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

        key_help += "{:<40} {}".format(mods, k.desc + "\n")

    return key_help


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

keys = [
    Key(key[0], key[1], *key[2:])
    for key in [
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
        ([mod, "control"], "equal", lazy.shutdown()),
        # Spawn command using a prompt widget
        # ([mod], "r", lazy.spawncmd()),
        # Browser
        ([mod], "b", lazy.spawn(browser)),
        # Calculator
        ([mod], "c", lazy.spawn(calculator)),
        # File Explorer
        ([mod], "e", lazy.spawn(file_browser)),
        # Terminal
        ([mod], "t", lazy.spawn(terminal)),
        # Nightlight (dependencies: x11-xserver-utils (debian) )
        (
            [mod, "shift"],
            "n",
            lazy.spawn(f"xgamma -rgamma {n["r"]} -ggamma {n["g"]} -bgamma {n["b"]}"),
        ),
        # Daylight (dependencies: x11-xserver-utils (debian) )
        (
            [mod, "shift"],
            "d",
            lazy.spawn(f"xgamma -rgamma {d["r"]} -ggamma {d["g"]} -bgamma {d["b"]}"),
        ),
    ]
]
keys.extend(
    [  # TODO:check: Key([], "Print", lazy.spawn("scrot /home/piyush/Pictures/Screenshot-%d-%m-%Y_%H:%M:%S_$wx$h.png -e 'xclip -selection clipboard -t image/png -i $f'"), desc="Print screen and copy to clipboard"),
        # Screenshots
        KeyChord(
            [mod],
            "s",
            [
                # dependencies: scrot, flameshot
                Key(key[0], key[1], *key[2:])
                for key in [
                    # Screenshot by selection or rectangle
                    ([], "s", lazy.spawn(f"scrot -s {scrot}")),
                    # Screenshot with highlighted area
                    ([], "h", lazy.spawn(f"scrot -shole {scrot}")),
                    # Screenshot with blurred area
                    ([], "b", lazy.spawn(f"scrot -sblur,30 {scrot}")),
                    # Screenshot with Flameshot
                    ([], "f", lazy.spawn("flameshot")),
                ]
            ],
            name="Screenshot mode",
        ),
        # Rofi
        KeyChord(
            [mod],
            "r",
            [
                Key(key[0], key[1], *key[2:])
                for key in [
                    ([], "a", lazy.spawn([scripts + "rofi_run"])),
                    (
                        [],
                        "w",
                        lazy.spawn(
                            "rofi -show window \
                    -theme /home/marco/.config/rofi/script_menu_1.rasi"
                        ),
                    ),
                    (
                        ["shift"],
                        "k",
                        lazy.spawn(
                            "rofi -show keys \
                    -theme /home/marco/.config/rofi/script_menu_1.rasi"
                        ),
                    ),
                    ([], "c", lazy.spawn([scripts + "rofi_clip"])),
                    (
                        [],
                        "b",
                        lazy.spawn(
                            "rofi-bluetooth | rofi -dmenu  \
                    -theme /home/marco/.config/rofi/script_menu_1.rasi"
                        ),
                    ),
                    ([], "r", lazy.spawncmd()),
                    (
                        [],
                        "p",
                        lazy.spawn([scripts + "rofi-power"]),  # "rofi -show drun"
                    ),
                ]
            ],
            name="Rofi select",
        ),
        # Volume
        KeyChord(
            [mod],
            "v",
            [
                # dependencies: pulseaudio-utils
                Key(key[0], key[1], *key[2:])
                for key in [
                    ([], "j", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ -5%")),
                    ([], "k", lazy.spawn("pactl set-sink-volume @DEFAULT_SINK@ +5%")),
                    ([], "m", lazy.spawn("pactl set-sink-mute @DEFAULT_SINK@ toggle")),
                ]
            ],
            mode=True,
            name="Adjust Volume",
        ),
    ]
)


keys.extend(
    [
        Key(
            [mod],
            "q",
            lazy.spawn(
                "sh -c 'echo \""
                + show_keybindings(keys)
                + '" | rofi -dmenu -i -theme /home/marco/.config/rofi/script_menu_1.rasi -p "󰌌" -mesg "Keyboard shortcuts"\''
            ),
        ),
    ]
)
# To bind groups to 'number' keys on an azerty Keyboard
g_bindings = [
    "ampersand",
    "eacute",
    "quotedbl",
    "apostrophe",
    "parenleft",
    "section",
    "egrave",
    "exclam",
    "ccedilla",
]

# group labels turn into icons with Awesome Font
# see:https://fontawesome.com/search?o=r&m=free&s=solid&f=classic
groups = [
    Group("1", label="HOME", layout="monadtall"),
    Group(
        # starting firefox with autostart.sh because of non resolved error when spawned
        "2",
        matches=[Match(wm_class=re.compile(r"^(firefox)$"))],
        label="globe",
        layout="monadtall",
    ),
    Group(
        "3",
        spawn="kitty -e nvim",
        label="code",
        layout="monadtall",
    ),
    Group(
        "4",
        # matches=[Match(wm_class=re.compile(r"^(kitty)$"))],
        spawn="kitty",
        label="terminal",
        layout="monadtall",
    ),
    Group(
        "5",
        matches=[Match(wm_class=re.compile(r"^(thunar)$"))],
        spawn="thunar",
        label="folder-open",
        layout="monadtall",
    ),
    Group(
        "6",
        matches=[Match(wm_class=re.compile(r"^(Virtualbox Manager)$"))],
        label="cubes",
        layout="monadtall",
    ),
    Group(
        "7",
        matches=[Match(wm_class=re.compile(r"^(whatsapp-for-linux)$"))],
        spawn="whatsapp-for-linux",
        label="comments",
        layout="monadtall",
    ),
    Group(
        "8",
        matches=[Match(wm_class=re.compile(r"^(thunderbird)$"))],
        spawn="thunderbird",
        label="envelope",
        layout="monadtall",
    ),
    Group(
        "9",
        matches=[Match(wm_class=re.compile(r"^(spotify)$"))],
        spawn="spotify",
        label="music",
        layout="monadtall",
    ),
]

for i, group in enumerate(groups):
    keys.extend(
        [
            # switch to group
            Key([mod], g_bindings[i], lazy.group[group.name].toscreen()),
            # switch to & move focused window to group
            Key(
                [mod, "shift"],
                g_bindings[i],
                lazy.window.togroup(group.name, switch_group=True),
            ),
        ]
    )


layout_theme = {
    "border_width": 2,
    "margin": 6,
    "border_focus": "#89b4fa",
    "border_normal": "#45475a",
    "grow_amount": 5,
}

layouts = [
    layout.MonadTall(**layout_theme),
    layout.Columns(**layout_theme),
    layout.Max(**layout_theme),
    # Try more layouts by unleashing below layouts.
    # layout.Stack(num_stacks=2),
    # layout.Bsp(),
    # layout.Matrix(),
    # layout.MonadWide(),
    # layout.RatioTile(),
    # layout.Tile(),
    # layout.TreeTab(),
    # layout.VerticalTile(),
    # layout.Zoomy(),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="qalculate"),
        Match(title="branchdialog"),  # gitk
        Match(wm_class="confirmreset"),  # gitk
        Match(wm_class="dialog"),  # dialog boxes
        Match(wm_class="download"),  # downloads
        Match(wm_class="error"),  # error msgs
        Match(wm_class="file_progress"),  # file progress boxes
        Match(wm_class="kdenlive"),  # kdenlive
        Match(wm_class="makebranch"),  # gitk
        Match(wm_class="maketag"),  # gitk
        Match(wm_class="notification"),  # notifications
        Match(wm_class="pinentry-gtk-2"),  # GPG key password entry
        Match(wm_class="ssh-askpass"),  # ssh-askpass
        Match(wm_class="toolbar"),  # toolbars
    ],
    # border_focus=#003fff
)

widget_defaults = dict(
    font="Jetbrains mono NF",
    fontsize=12,
    padding=3,
)
extension_defaults = widget_defaults.copy()

primary_widgets = [
    widget.CurrentLayoutIcon(
        padding=4, scale=0.7, foreground="#cdd6f4", background="#1e1e2e"
    ),
    widget.OpenWeather(
        background="#1e1e2e",
        cityid=2803138,
        font="Jetbrains Mono Nerd Font Bold",
        fontsize=12,
        format="{main_temp}° {icon}",
        padding=8,
    ),
    widget.Prompt(
        font="Jetbrains Mono Nerd Font Bold",
        fontsize=12,
        background="#1e1e2e",
        foreground="#cdd6f4",
    ),
    widget.Spacer(background="#1e1e2e"),
    widget.GroupBox(
        font="Font Awesome 6 Free Solid",
        fontsize=14,
        margin_y=2,
        margin_x=16,
        padding_y=2,
        padding_x=3,
        borderwidth=0,
        disable_drag=True,
        active="#6c7086",
        inactive="#313244",
        rounded=False,
        highlight_method="text",
        this_current_screen_border="#cdd6f4",
        foreground="#45475a",
        background="#1e1e2e",
    ),
    widget.Spacer(background="#1e1e2e"),
    widget.Chord(
        font="Jetbrains Mono Nerd Font Bold",
        fontsize=12,
        background="#a6e3a1",
        foreground="#1e1e2e",
    ),
    widget.CurrentScreen(
        background="#1e1e2e",
        active_color="#00ff00",
        active_text="",
        inactive_color="#ff0000",
        inactive_text="",
        padding=6,
    ),
    widget.Sep(linewidth=1, padding=5, foreground="#45475a", background="#1e1e2e"),
    widget.CPU(
        background="#1e1e2e",
        foreground="#181825",
        font="Jetbrains Mono Nerd Font Bold",
        fontsize=12,
        decorations=[
            RectDecoration(colour="#f38ba8", padding_y=3, radius=2, filled=True),
        ],
    ),
    widget.Sep(linewidth=1, padding=5, foreground="4c566a", background="#1e1e2e"),
    widget.Memory(
        measure_mem="G",
        foreground="#181825",
        background="#1e1e2e",
        font="Jetbrains Mono Nerd Font Bold",
        fontsize=12,
        format="RAM{MemUsed: .0f}{mm}/{MemTotal: .0f}{mm}",
        decorations=[
            RectDecoration(colour="#fab387", padding_y=3, radius=2, filled=True),
        ],
    ),
    widget.Sep(linewidth=1, padding=5, foreground="#45475a", background="#1e1e2e"),
    widget.Clock(
        foreground="#181825",
        background="#1e1e2e",
        font="Jetbrains Mono Nerd Font Bold",
        fontsize=12,
        format="%d %B %y",
        decorations=[
            RectDecoration(colour="#a6e3a1", padding_y=3, radius=2, filled=True),
        ],
    ),
    widget.Sep(linewidth=1, padding=5, foreground="4c566a", background="#1e1e2e"),
    widget.Clock(
        foreground="#181825",
        background="#1e1e2e",
        font="Jetbrains Mono Nerd Font Bold",
        fontsize=12,
        format="%H:%M:%S",
        decorations=[
            RectDecoration(colour="#89b4fa", padding_y=3, radius=2, filled=True),
        ],
    ),
    widget.Sep(linewidth=1, padding=5, foreground="#45475a", background="#1e1e2e"),
    widget.Systray(
        background="#1e1e2e",
        icon_size=20,
        padding=5,
    ),
    widget.Sep(linewidth=1, padding=5, foreground="#45475a", background="#1e1e2e"),
    widget.TextBox(
        foreground="#708ed8",
        background="#1e1e2e",
        text="⏻",
        font="Font Awesome 6 Free Solid",
        fontsize=17,
        padding=10,
        mouse_callbacks={"Button1": lazy.spawn([scripts + "powermenu"])},
    ),
]
secondary_widgets = [
    widget.CurrentLayoutIcon(
        padding=4, scale=0.7, foreground="#cdd6f4", background="#1e1e2e"
    ),
    widget.Spacer(background="#1e1e2e"),
    widget.GroupBox(
        font="Font Awesome 6 Free Solid",
        fontsize=14,
        margin_y=2,
        margin_x=16,
        padding_y=2,
        padding_x=3,
        borderwidth=0,
        disable_drag=True,
        active="#6c7086",
        inactive="#313244",
        rounded=False,
        highlight_method="text",
        this_current_screen_border="#cdd6f4",
        foreground="#45475a",
        background="#1e1e2e",
    ),
    widget.Spacer(background="#1e1e2e"),
    widget.CurrentScreen(
        background="#1e1e2e",
        active_color="#00ff00",
        active_text="",
        inactive_color="#ff0000",
        inactive_text="",
        padding=6,
    ),
    widget.Sep(linewidth=1, padding=5, foreground="#45475a", background="#1e1e2e"),
    widget.Clock(
        foreground="#181825",
        background="#1e1e2e",
        font="Jetbrains Mono Nerd Font Bold",
        fontsize=12,
        format="%d %B %y",
        decorations=[
            RectDecoration(colour="#a6e3a1", padding_y=3, radius=2, filled=True),
        ],
    ),
    widget.Sep(linewidth=1, padding=5, foreground="4c566a", background="#1e1e2e"),
    widget.Clock(
        foreground="#181825",
        background="#1e1e2e",
        font="Jetbrains Mono Nerd Font Bold",
        fontsize=12,
        format="%H:%M:%S",
        decorations=[
            RectDecoration(colour="#89b4fa", padding_y=3, radius=2, filled=True),
        ],
    ),
    widget.Sep(linewidth=1, padding=5, foreground="#45475a", background="#1e1e2e"),
]


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


def status_bar(widgets):
    return bar.Bar(widgets, 28, margin=[3, 3, 0, 3], opacity=0.75)


screens = [
    Screen(
        top=status_bar(primary_widgets),
    ),
]

monitors = count_monitors()
if monitors > 1:
    for _ in range(1, monitors):
        screens.append(Screen(top=status_bar(secondary_widgets)))


# Drag floating layouts.
mouse = [
    Drag(
        [mod],
        "Button1",
        lazy.window.set_position_floating(),
        start=lazy.window.get_position(),
    ),
    Drag(
        [mod], "Button3", lazy.window.set_size_floating(), start=lazy.window.get_size()
    ),
    Click([mod], "Button2", lazy.window.bring_to_front()),
]

dgroups_key_binder = None
dgroups_app_rules = []  # type: list
follow_mouse_focus = True
bring_front_click = False
floats_kept_above = True
cursor_warp = False
auto_fullscreen = True
focus_on_window_activation = "smart"
reconfigure_screens = True

# If things like steam games want to auto-minimize themselves when losing
# focus, should we respect this or not?
auto_minimize = True

# When using the Wayland backend, this can be used to configure input devices.
wl_input_rules = None


@hook.subscribe.startup_once
def start_once():
    subprocess.Popen([home + "/.config/qtile/autostart.sh"])


@hook.subscribe.startup_complete
def run_every_startup():
    qtile.groups_map["2"].toscreen(0)
    qtile.groups_map["3"].toscreen(1)


# @hook.subscribe.client_new
# def new_client(client):
#     if client.name == "kitty":
#         send_notification("client name", f"{client.name}")
#         client.enable_fullscreen
#         client.enable_fullscreen
#

# @hook.subscribe.group_window_add
# def group_window_add(group, window):
#     if group.name == "3":
#         if window.name == "kitty":
#             window.enable_fullscreen()
#             send_notification("qtile", "fullscreen enabled")


# XXX: Gasp! We're lying here. In fact, nobody really uses or cares about this
# string besides java UI toolkits; you can see several discussions on the
# mailing lists, GitHub issues, and other WM documentation that suggest setting
# this string if your java app doesn't work correctly. We may as well just lie
# and say that we're a working one by default.
#
# We choose LG3D to maximize irony: it is a 3D non-reparenting WM written in
# java that happens to be on java's whitelist.
wmname = "LG3D"
