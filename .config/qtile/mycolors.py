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

### Alternate Colors ###
# COLORS FOR THE BAR AND WINDOWS
# textColor = "#ffffff"
# barBackground = "#0d0d0d"
# leftColor1 = "#f28cae"
# leftColor2 = "#98a0e7"
# rightColor1 = "#e52165"
# rightColor2 = "#0d1137"
# def colorsDict():
#     return {
#             ### Bar Background ###
#             "barBackground" : barBackground,

#             ### Sep colors ###
#             "sepForeground" : "#1a000a",
#             "sepBackground" : barBackground,

#             ### Group colors ###
#             "groupBackground" : leftColor1,
#             "groupForeground" : textColor,
#             "currentGroup" : "#2e0513",
#             "groupActive" : "#eb477e",

#             ### Layout colors ###
#             "layoutBackground" : leftColor2,
#             "layoutForeground" : textColor,

#             ### Window Name colors ###
#             "windowBackground" : barBackground,
#             "windowForeground" : textColor,

#             ### Clock colors ###
#             "clockForeground" : textColor,
#             "clockBackground" : barBackground,
            
#             ### CPU colors ###
#             "cpuBackground" : rightColor2,
#             "cpuForeground" : textColor,

#             ### Memory colors ###
#             "memoryBackground" : rightColor1,
#             "memoryForeground" : textColor,

#             ### HDD colors ###
#             "hddBackground" : rightColor2,
#             "hddForeground" : textColor,

#             ### Volume colors ###
#             "volBackground" : rightColor1,
#             "volForeground" : textColor,

#             ### Updates colors ###
#             "updateBackground" : rightColor2,
#             "updateForeground" :textColor,
#             "updatesAvailable" : "#cc0000",
            

#             ### Tray colors ###
#             "trayForeground" : textColor,
#             "trayBackground" : rightColor1,

#             ### Exit Menu ###
#             "exitForeground" : textColor,
#             "exitBackground" : rightColor2,

#             # COLORS FOR THE WINDOWS
#             "border_focus" : "#ff0066",
#             "border_normal" : "#ffe6f0",

#             }

# # print(colorsList(), colorsDict())


# ### Shade Style ###
# textColor = "#000000"
# # colorShades = ['#fff1ef', '#ffe2df', '#ffd4d0', '#ffc5c0', '#ffb7b0', '#ffa9a0', '#ff9a90', '#ff8c81', '#ff7d71', '#ff6f61']
# # colorShades = ['#ffb7b0', '#ffc5c0', '#ffd4d0', '#ffc5c0', '#ffb7b0', '#ffa9a0', '#ff9a90', '#ff8c81', '#ff7d71', '#ff6f61']
# colorShades =['9aaac5', 'aebbd1', 'c2ccdc', 'aebbd1', '9aaac5', '8599b9', '7188ae', '5d77a2', '486697', '34558b']
# # colorShades = ['#ffd0cc', '#ffb9b3', '#ffa299', '#ff8a80', '#ff7366', '#ff6f61', '#ff5b4d', '#ff4433', '#ff2d1a', '#ff1500', '#e61300']
# barBackground = colorShades[2]
# # colorShades.reverse()
# def colorsDict():
#     return {
#             ### Bar Background ###
#             "barBackground" : barBackground,

#             ### Sep colors ###
#             "sepForeground" : "#1a000a",
#             "sepBackground" : barBackground,

#             ### Group colors ###
#             "groupBackground" : colorShades[0],
#             "groupForeground" : textColor,
#             "currentGroup" : "#ffffff",
#             "groupActive" : "#eb477e",

#             ### Layout colors ###
#             "layoutBackground" : colorShades[1],
#             "layoutForeground" : textColor,

#             ### Window Name colors ###
#             "windowBackground" : barBackground,
#             "windowForeground" : textColor,

#             ### Clock colors ###
#             "clockForeground" : textColor,
#             "clockBackground" : barBackground,
            
#             ### CPU colors ###
#             "cpuBackground" : colorShades[3],
#             "cpuForeground" : textColor,

#             ### Memory colors ###
#             "memoryBackground" : colorShades[4],
#             "memoryForeground" : textColor,

#             ### HDD colors ###
#             "hddBackground" : colorShades[5],
#             "hddForeground" : textColor,

#             ### Volume colors ###
#             "volBackground" : colorShades[6],
#             "volForeground" : textColor,

#             ### Updates colors ###
#             "updateBackground" : colorShades[7],
#             "updateForeground" :textColor,
#             "updatesAvailable" : "#cc0000",
            

#             ### Tray colors ###
#             "trayForeground" : textColor,
#             "trayBackground" : colorShades[8],

#             ### Exit Menu ###
#             "exitForeground" : textColor,
#             "exitBackground" : colorShades[9],

#             # COLORS FOR THE WINDOWS
#             "border_focus" : colorShades[9],
#             "border_normal" : colorShades[0],

#             }




### Python-pywal ### sudo pacman -S python-pywal
## Background change ##
textColor = wal["special"]["background"]
clockColor = wal["special"]["foreground"]
barBackground =wal["special"]["background"]

leftColor1 = wal["colors"]["color3"]
leftColor2 = wal["colors"]["color4"]
rightColor1 = wal["colors"]["color5"]
rightColor2 = wal["colors"]["color6"]
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
            "currentGroup" : "#cc0000",
            "groupActive" : "#aaa0ff",

            ### Layout colors ###
            "layoutBackground" : leftColor2,
            "layoutForeground" : textColor,

            ### Window Name colors ###
            "windowBackground" : barBackground,
            "windowForeground" : clockColor,

            ### Clock colors ###
            "clockForeground" : clockColor,
            "clockBackground" : barBackground,
            
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


# ## Text change ##
# textColor = wal["special"]["background"]
# clockColor = wal["special"]["foreground"]
# barBackground =wal["special"]["background"]

# leftColor1 = wal["colors"]["color3"]
# leftColor2 = wal["colors"]["color4"]
# rightColor1 = wal["colors"]["color5"]
# rightColor2 = wal["colors"]["color6"]
# def colorsDict():
#     return {
#             ### Bar Background ###
#             "barBackground" : barBackground,

#             ### Sep colors ###
#             "sepForeground" : "#1a000a",
#             "sepBackground" : barBackground,

#             ### Group colors ###
#             "groupBackground" : barBackground,
#             "groupForeground" : leftColor1,
#             "currentGroup" : "#cc0000",
#             "groupActive" : "#aaa0ff",

#             ### Layout colors ###
#             "layoutBackground" : barBackground,
#             "layoutForeground" : leftColor2,

#             ### Window Name colors ###
#             "windowBackground" : barBackground,
#             "windowForeground" : clockColor,

#             ### Clock colors ###
#             "clockForeground" : clockColor,
#             "clockBackground" : barBackground,
            
#             ### CPU colors ###
#             "cpuBackground" : barBackground,
#             "cpuForeground" : rightColor2,

#             ### Memory colors ###
#             "memoryBackground" : barBackground,
#             "memoryForeground" : rightColor1,

#             ### HDD colors ###
#             "hddBackground" : barBackground,
#             "hddForeground" : rightColor2,

#             ### Volume colors ###
#             "volBackground" : barBackground,
#             "volForeground" : rightColor1,

#             ### Updates colors ###
#             "updateBackground" : barBackground,
#             "updateForeground" : rightColor2,
#             "updatesAvailable" : "#cc0000",
            

#             ### Tray colors ###
#             "trayForeground" : rightColor1,
#             "trayBackground" : barBackground,

#             ### Exit Menu ###
#             "exitForeground" : rightColor2,
#             "exitBackground" : barBackground,

#             # COLORS FOR THE WINDOWS
#             "border_focus" : wal["colors"]["color2"],
#             "border_normal" : wal["colors"]["color1"],

#             }
