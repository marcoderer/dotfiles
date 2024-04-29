#  ╭──────────────────────────╮  #
#  │   ____ ___ _ _    ____   │  #
#  │   |  |  |  | |    |___   │  #
#  │   |_\|  |  | |___ |___   │  #
#  │                          │  #
#  ╰──────────────────────────╯  #
#   ======== WIDGETS =========   #

from libqtile import widget, bar
import psutil
from libqtile import qtile
from .theme import color
from .paths import icons_dir
from qtile_extras import widget
from qtile_extras.widget.decorations import BorderDecoration 
from utils.qutils import open_powermenu

def base(fg="fg", bg="bg"): 
    return {
        "foreground": color[fg],
        "background": color[bg],
    }

def separator(size_percent=50, padding=10):
    return widget.Sep(
        **base(fg="bgmuted"), 
        linewidth=0, 
        padding=padding,
        size_percent=size_percent
    )

def icon(
        text="?", 
        fg="extrablue", 
        bg="bg", 
        fontsize=17, 
        padding=10, 
        mouse_callbacks=None):
    return widget.TextBox(
        **base(fg, bg),
        text=text,
        font="Font Awesome 6 Free Solid",
        fontsize=fontsize,
        padding=padding
    )

def wicon(text="?", fg="fg", bg="extradark"): 
    return widget.TextBox(
        **base(fg, bg),
        text=text,
        font="Font Awesome 6 Free Solid"
    )

def bubble(open=False,fg="extradark", bg="bg"):
    text = ""
    if not open:
        text = ""
    return widget.TextBox(
        **base(fg, bg),
        text=text, 
        fontsize=17,
        padding=0
    )

def workspaces(): 
    return widget.GroupBox(
        **base(bg="extradark"),
        font="Font Awesome 6 Free Solid",
        fontsize=12,
        margin_y=5,
        margin_x=0,
        padding_y=4,
        padding_x=4,
        borderwidth=2,
        this_current_screen_border=color.bg,
        this_screen_border=color.ansi5,
        other_current_screen_border=color.extradark,
        other_screen_border=color.extradark,
        urgent_border=color.alert,
        active=color.ansi7,
        inactive=color.extragrey,
        rounded=True,
        highlight_method="block",
        urgent_alert_method="block",
        disable_drag=True,
        highlight_color=color.bgmuted,
        block_highlight_text_color=color.ansi4,
    )

primary_widgets = [
    icon(text=""),
    bubble(open=True),
    workspaces(),
    bubble(),
    separator(padding=18, size_percent=40),
    bubble(open=True),
    widget.CurrentLayoutIcon(
            **base(fg="bgmuted", bg="extradark"),
            custom_icon_paths=[icons_dir],
            padding=6,
            scale=0.40,
    ),
    bubble(),
    separator(),
    widget.Spacer(**base()),
    wicon(text=" ", fg="extracyan", bg="bg"),
    widget.WindowName(
        **base(fg="extracyan"),
        width=bar.CALCULATED,
        empty_group_string="Desktop",
        max_chars=130,
    ),
    widget.Spacer(**base()),
    separator(padding=18, size_percent=40),
    bubble(open=True),
    wicon(text=" ", fg="ansi4", bg="extradark"),
    widget.Volume(
        **base(fg="ansi4", bg="extradark"),
        font="Font Awesome 6 Free Solid",
        emoji=True,
    ),
    bubble(),
    separator(),
    bubble(open=True),
    wicon(text=" ", fg="ansi5", bg="extradark"),
    widget.Net(
        **base(fg="ansi5", bg="extradark"),
        interface="enp86s0",
        format="{down} ↓↑ {up}",
        prefix="k",
        padding=5,
    ),
    bubble(),
    separator(),
    bubble(open=True),
    wicon(text=" ", fg="ansi3", bg="extradark"),
    widget.Clock(
        **base(fg="ansi3", bg="extradark"),
        format="%a, %b %d",
    ),
    bubble(),
    separator(),
    bubble(open=True),
    wicon(text=" ", fg="ansi3", bg="extradark"),
    widget.Clock(
        **base(fg="ansi3", bg="extradark"),
        format="%I:%M %p",
    ),
    bubble(),
    widget.Systray(
        **base(),
        icon_size=14,
        padding=7,
    ),
    icon(text="⏻"), #, mouse_callbacks={"Button1": open_powermenu()}),
]

secondary_widgets = [
    icon(text=""),
    bubble(open=True),
    workspaces(),
    bubble(),
    separator(padding=18, size_percent=40),
    bubble(open=True),
    widget.CurrentLayoutIcon(
            **base(fg="bgmuted", bg="extradark"),
            custom_icon_paths=[icons_dir],
            padding=6,
            scale=0.40,
    ),
    bubble(),
    separator(),
    widget.Spacer(**base()),
    wicon(text=" ", fg="extracyan"),
    widget.WindowName(
        **base(fg="extracyan"),
        width=bar.CALCULATED,
        empty_group_string="Desktop",
        max_chars=130,
    ),
    separator(),
    widget.Spacer(**base()),
    separator(padding=18, size_percent=40),
]

widget_defaults = dict(
    font="Ubuntu Bold",
    fontsize=12,
    padding=3,
    decorations=[
        BorderDecoration(
            colour=color.alert,
            border_width=[0, 0, 0, 0],
        ),
    ]
)
extension_defaults = widget_defaults.copy()
