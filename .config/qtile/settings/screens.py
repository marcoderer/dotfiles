#  ╭──────────────────────────╮  #
#  │   ____ ___ _ _    ____   │  #
#  │   |  |  |  | |    |___   │  #
#  │   |_\|  |  | |___ |___   │  #
#  │                          │  #
#  ╰──────────────────────────╯  #
#   ==== MONITORS CONFIG =====   #

from libqtile.config import Screen
from libqtile import bar
from .widgets import primary_widgets, secondary_widgets
from .paths import wallpaper
from .theme import color
from utils.qutils import count_monitors


def status_bar(widgets):
    return bar.Bar(
        widgets, 
        20,
        margin=[0, 0, 4, 0],
        border_width=4,
        border_color=color.alert)
    
screen_defaults= {
        "wallpaper": wallpaper,
        "wallpaper_mode": "fill",
        "bottom": bar.Gap(4),
        "left": bar.Gap(4),
        "right": bar.Gap(4),
}

screens = [
    Screen(
        **screen_defaults,
        top=status_bar(primary_widgets),
    ),
]

monitors = count_monitors()
if monitors > 1:
    for _ in range(1, monitors):
        screens.append(
            Screen(
                **screen_defaults,
                top=status_bar(secondary_widgets)
            )
        )
