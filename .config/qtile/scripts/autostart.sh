#!/bin/bash

function run {
  if ! pgrep $1 ;
  then
    $@&
  fi
}

# ## Launch Variety ###
run variety &

## Change wallpaper and get accent colors  ###
# $HOME/.config/qtile/scripts/set-pywal.sh -u &
wal -R 

### Launch Power Manager ###
run xfce4-power-manager &

### Launch Xfce settings daemon ###
run xfsettingsd &

### Launch network manager ###
run nm-applet &

### Launch Lightdm locker service ###
run light-locker &

### Launch bluetooth manager tray icon ###
# blueman-tray &

### Launch compositor picom ###
picom &

### Launch authentication agent ###
/usr/lib/polkit-gnome/polkit-gnome-authentication-agent-1 &

### Launch pulse audio ###
start-pulseaudio-x11 &
