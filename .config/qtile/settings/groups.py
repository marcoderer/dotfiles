#  ╭──────────────────────────╮  #
#  │   ____ ___ _ _    ____   │  #
#  │   |  |  |  | |    |___   │  #
#  │   |_\|  |  | |___ |___   │  #
#  │                          │  #
#  ╰──────────────────────────╯  #
#   ====== GROUP CONFIG ======   #

from libqtile.config import Key, Group
from libqtile.command import lazy
from .keys import mod, keys

groups = []
group_names = ["1", "2", "3", "4", "5", "6", "7", "8", "9",]

# group labels turn into icons with Awesome Font
# see:https://fontawesome.com/search?o=r&m=free&s=solid&f=classic
group_labels = ["HOME", "globe", "code", "folder-open", "envelope", "terminal", "cubes", "comments", "music",]

group_layouts = ["monadtall", "monadtall", "tile", "tile", "monadtall", "monadtall", "monadtall", "monadtall", "monadtall"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))
 
for i in groups:
    keys.extend(
        [
            # mod + group number = switch to group
            Key(
                [mod],
                i.name,
                lazy.group[i.name].toscreen(),
                desc="Switch to group {}".format(i.name),
            ),
            # mod + shift + group number = switch to & move focused window to group
            Key(
                [mod, "shift"],
                i.name,
                lazy.window.togroup(i.name, switch_group=True),
                desc="Switch to & move focused window to group {}".format(i.name),
            ),
            # Or, use below if you prefer not to switch to that group.
            # mod + ctrl + group number = move focused window to group
            Key([mod, "control"], i.name, lazy.window.togroup(i.name),
                desc="move focused window to group {}".format(i.name)),
        ]
    )
