#!/bin/sh

cp -u dunstrc $HOME/.config/wal/templates/

# Symlink dunst config
ln -sf ~/.cache/wal/dunstrc ~/.config/dunst/dunstrc

# Restart dunst with the new color scheme
pkill dunst
dunst &