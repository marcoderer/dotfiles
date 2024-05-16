#!/usr/bin/env bash

### AUTOSTART PROGRAMS ###
picom --experimental-backends -b &
nitrogen --restore &
greenclip daemon &
sleep 1
firefox &
