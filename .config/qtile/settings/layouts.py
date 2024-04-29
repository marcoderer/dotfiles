#  ╭──────────────────────────╮  #
#  │   ____ ___ _ _    ____   │  #
#  │   |  |  |  | |    |___   │  #
#  │   |_\|  |  | |___ |___   │  #
#  │                          │  #
#  ╰──────────────────────────╯  #
#   ===== LAYOUTS CONFIG =====   #

from libqtile import layout
from libqtile.config import Match
from .theme import color

# Layouts and layout rules


layout_theme = {
    "border_width": 2,
    "margin": 4,
    "border_focus": "003fff",
    "border_normal": "3b4252",
    "font": "FiraCode Nerd Font",
    "grow_amount": 2,
}

layouts = [
    layout.Columns(
        **layout_theme,
        border_on_single=True,
        num_columns=2,
        border_focus_stack="#003fff",
        border_normal_stack="#3b4252",
        split=False,
        wrap_focus_columns=True,
        wrap_focus_rows=True,
        wrap_focus_stacks=True,
    ),
    layout.Bsp(**layout_theme, fair=False, border_on_single=True),
    layout.Matrix(**layout_theme),
    layout.MonadTall(**layout_theme),
    layout.MonadWide(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Tile(**layout_theme),
]

floating_layout = layout.Floating(
    float_rules=[
        *layout.Floating.default_float_rules,
        Match(wm_class="confirmreset"),
        Match(wm_class="makebranch"),
        Match(wm_class="maketag"),
        Match(wm_class="ssh-askpass"),
        Match(title="branchdialog"),
        Match(title="pinentry"),
    ],
    # border_focus=#003fff
)
