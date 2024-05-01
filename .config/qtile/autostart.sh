#!/usr/bin/env bash

### AUTOSTART PROGRAMS ###
picom --experimental-backends -b &
sleep 1
nitrogen --restore &
firefox
kitty
thunderbird
thunar
whatsapp-for-linux
