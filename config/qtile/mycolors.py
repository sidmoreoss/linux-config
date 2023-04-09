import json
import os
home = os.path.expanduser('~')
with open(home + '/.cache/wal/colors.json') as f:
    wal = json.load(f)

def colorsList():
    return [["#2F343F", "#2F343F"],  # color 0
            ["#2F343F", "#2F343F"],  # color 1
            ["#c0c5ce", "#c0c5ce"],  # color 2
            ["#fba922", "#fba922"],  # color 3
            ["#3384d0", "#3384d0"],  # color 4
            ["#f3f4f5", "#f3f4f5"],  # color 5
            ["#cd1f3f", "#cd1f3f"],  # color 6
            ["#62FF00", "#62FF00"],  # color 7
            ["#0d4bd1", "#0d4bd1"],  # color 8
            ["#a9a9a9", "#a9a9a9"]]  # color 9

### Python-pywal ### sudo pacman -S python-pywal
## Background change ##
textColor = wal["special"]["background"]
clockColor = wal["special"]["foreground"]
barBackground =wal["special"]["background"]
leftColor1 = wal["colors"]["color1"]
leftColor2 = wal["colors"]["color2"]
rightColor1 = wal["colors"]["color3"]
rightColor2 = wal["colors"]["color4"]
def colorsDict():
    return {
            ### Bar Background ###
            "barBackground" : barBackground,

            ### Sep colors ###
            "sepForeground" : "#1a000a",
            "sepBackground" : barBackground,

            ### Group colors ###
            "groupBackground" : leftColor1,
            "groupForeground" : textColor,
            "currentGroup" : leftColor1,
            "groupActive" : leftColor2,

            ### Layout colors ###
            "layoutBackground" : leftColor2,
            "layoutForeground" : textColor,

            ### Window Name colors ###
            "windowBackground" : barBackground,
            "windowForeground" : clockColor,

            ### Clock colors ###
            "clockForeground" : clockColor,
            "clockBackground" : barBackground,
            
            ### Music colors ###
            "musicForeground" : rightColor1,
            "musicBackground" : rightColor1,
            
            ### CPU colors ###
            "cpuBackground" : rightColor2,
            "cpuForeground" : textColor,

            ### Memory colors ###
            "memoryBackground" : rightColor1,
            "memoryForeground" : textColor,

            ### HDD colors ###
            "hddBackground" : rightColor2,
            "hddForeground" : textColor,

            ### Volume colors ###
            "volBackground" : rightColor1,
            "volForeground" : textColor,

            ### Updates colors ###
            "updateBackground" : rightColor2,
            "updateForeground" :textColor,
            "updatesAvailable" : "#cc0000",

            ### Wallpaper colors ###
            "walBackground" : rightColor1,
            "walForeground" :textColor,
            
            ### Tray colors ###
            "trayForeground" : textColor,
            "trayBackground" : rightColor2,

            ### Exit Menu ###
            "exitForeground" : textColor,
            "exitBackground" : rightColor1,

            # COLORS FOR THE WINDOWS
            "border_focus" : wal["colors"]["color2"],
            "border_normal" : wal["colors"]["color1"],

            }


