import os
import re
import socket
import subprocess
from libqtile.config import Drag, Key, Screen, Group, Drag, Click, Rule
from libqtile.command import lazy
from libqtile import layout, bar, widget, hook
from libqtile.widget import Spacer
import arcobattery
import mycolors
from constants import *
colors = mycolors.colorsList()
color = mycolors.colorsDict()

# mod4 or mod = super key
mod = "mod4"
mod1 = "alt"
mod2 = "control"
home = os.path.expanduser('~')
LOGOUT_MANAGER = home + '/.config/qtile/scripts/power.sh'


@lazy.function
def window_to_prev_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i - 1].name)


@lazy.function
def window_to_next_group(qtile):
    if qtile.currentWindow is not None:
        i = qtile.groups.index(qtile.currentGroup)
        qtile.currentWindow.togroup(qtile.groups[i + 1].name)


#####################################################################################################################################################################
############################# Key Bindings Start ####################################################################################################################
#####################################################################################################################################################################
keys = [

    # FUNCTION KEYS
    Key([], "F12", lazy.spawn('xfce4-terminal --drop-down')),
    
    # SUPER + FUNCTION KEYS  (Launch Applications)
    Key([mod], "e", lazy.spawn(MY_FILE_MANAGER)),
    Key([mod], "c", lazy.spawn(MY_CODE_EDITOR)),
    Key([mod], "b", lazy.spawn(MY_BROWSER)),
    Key([mod], "m", lazy.spawn(MY_MUSIC_PLAYER)),
    Key([mod], "v", lazy.spawn('pavucontrol')),
    Key([mod], "Escape", lazy.spawn('xkill')),
    Key([mod], "Return", lazy.spawn(MY_TERMINAL)),
    Key([mod], "s", lazy.spawn('rofi -show run')),
    Key([mod], "f", lazy.window.toggle_fullscreen()),

    # SUPER + CONTROL KEYS
    Key([mod, "control"], "r", lazy.restart()),
    Key([mod, "control"], "q", lazy.shutdown()),
    Key([mod, "control"], "x", lazy.spawn(LOGOUT_MANAGER)),
    Key([mod, "control"], "F4", lazy.spawn("systemctl poweroff")),
    Key([mod, "control"], "F5", lazy.spawn("systemctl reboot")),

    # SUPER + SHIFT KEYS
    Key([mod, "shift"], "d", lazy.spawn(
        "dmenu_run -i -nb '#191919' -nf '#fea63c' -sb '#fea63c' -sf '#191919' -fn 'NotoMonoRegular:bold:pixelsize=14'")),
    Key([mod, "shift"], "c", lazy.window.kill()),

    # CONTROL + SHIFT KEYS
    Key([mod2, "shift"], "Escape", lazy.spawn('xfce4-taskmanager')),

    # MULTIMEDIA KEYS
    # SCREENSHOTS
    Key([], "Print", lazy.spawn("flameshot full -p " + home + "/Pictures")),
    Key([mod], "Print", lazy.spawn("flameshot gui")),
    # INCREASE/DECREASE BRIGHTNESS
    # Key([], "XF86MonBrightnessUp", lazy.spawn("blight set +10%")),
    # Key([], "XF86MonBrightnessDown", lazy.spawn("blight set -10%")),
    # INCREASE/DECREASE/MUTE VOLUME
    Key([], "XF86AudioMute", lazy.spawn("amixer -q set Master toggle")),
    Key([], "XF86AudioLowerVolume", lazy.spawn("amixer -q set Master 5%-")),
    Key([], "XF86AudioRaiseVolume", lazy.spawn("amixer -q set Master 5%+")),
    # Play Pause Audio
    Key([], "XF86AudioPlay", lazy.spawn("playerctl play-pause")),
    Key([], "XF86AudioNext", lazy.spawn("playerctl next")),
    Key([], "XF86AudioPrev", lazy.spawn("playerctl previous")),
    Key([], "XF86AudioStop", lazy.spawn("playerctl stop")),

    # QTILE LAYOUT KEYS
    Key([mod], "n", lazy.layout.normalize()),
    Key([mod], "space", lazy.next_layout()),

    # CHANGE FOCUS
    Key([mod], "Up", lazy.layout.up()),
    Key([mod], "Down", lazy.layout.down()),
    Key([mod], "Left", lazy.layout.left()),
    Key([mod], "Right", lazy.layout.right()),
    Key([mod], "k", lazy.layout.up()),
    Key([mod], "j", lazy.layout.down()),
    Key([mod], "h", lazy.layout.left()),
    Key([mod], "l", lazy.layout.right()),


    # RESIZE UP, DOWN, LEFT, RIGHT
    Key([mod, "control"], "l",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "Right",
        lazy.layout.grow_right(),
        lazy.layout.grow(),
        lazy.layout.increase_ratio(),
        lazy.layout.delete(),
        ),
    Key([mod, "control"], "h",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "Left",
        lazy.layout.grow_left(),
        lazy.layout.shrink(),
        lazy.layout.decrease_ratio(),
        lazy.layout.add(),
        ),
    Key([mod, "control"], "k",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "Up",
        lazy.layout.grow_up(),
        lazy.layout.grow(),
        lazy.layout.decrease_nmaster(),
        ),
    Key([mod, "control"], "j",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),
    Key([mod, "control"], "Down",
        lazy.layout.grow_down(),
        lazy.layout.shrink(),
        lazy.layout.increase_nmaster(),
        ),


    # FLIP LAYOUT FOR MONADTALL/MONADWIDE
    Key([mod, "shift"], "f", lazy.layout.flip()),

    # FLIP LAYOUT FOR BSP
    Key([mod, "mod1"], "k", lazy.layout.flip_up()),
    Key([mod, "mod1"], "j", lazy.layout.flip_down()),
    Key([mod, "mod1"], "l", lazy.layout.flip_right()),
    Key([mod, "mod1"], "h", lazy.layout.flip_left()),

    # MOVE WINDOWS UP OR DOWN BSP LAYOUT
    Key([mod, "shift"], "k", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "j", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "h", lazy.layout.shuffle_left()),
    Key([mod, "shift"], "l", lazy.layout.shuffle_right()),

    # MOVE WINDOWS UP OR DOWN MONADTALL/MONADWIDE LAYOUT
    Key([mod, "shift"], "Up", lazy.layout.shuffle_up()),
    Key([mod, "shift"], "Down", lazy.layout.shuffle_down()),
    Key([mod, "shift"], "Left", lazy.layout.swap_left()),
    Key([mod, "shift"], "Right", lazy.layout.swap_right()),

    # TOGGLE FLOATING LAYOUT
    Key([mod, "shift"], "space", lazy.window.toggle_floating()), ]
#####################################################################################################################################################################
############################# Key Bindings End ######################################################################################################################
#####################################################################################################################################################################


#####################################################################################################################################################################
############################# Groups (Workspaces) Start #############################################################################################################
#####################################################################################################################################################################
groups = []

# FOR QWERTY KEYBOARDS
group_names = ["1", "2", "3", "4", "5", "6"]

#group_labels = ["1 ", "2 ", "3 ", "4 ", "5 ", "6 ", "7 ", "8 ", "9 ", "0",]
group_labels = ["", "", "", "", "", ""]
#group_labels = ["Web", "Code", "Terminal", "Filemanagers", "Meld", "Video", "Vb", "Files", "Mail", "Music",]

group_layouts = ["monadtall", "monadtall",
                 "monadtall", "monadtall", "monadtall", "monadtall"]

for i in range(len(group_names)):
    groups.append(
        Group(
            name=group_names[i],
            layout=group_layouts[i].lower(),
            label=group_labels[i],
        ))

for i in groups:
    keys.extend([
        # CHANGE WORKSPACES
        Key([mod], i.name, lazy.group[i.name].toscreen(toggle=False)),
        Key([mod], "Tab", lazy.screen.next_group()),
        Key(["mod1"], "Tab", lazy.screen.next_group()),
        Key(["mod1", "shift"], "Tab", lazy.screen.prev_group()),

        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND STAY ON WORKSPACE
        #Key([mod, "shift"], i.name, lazy.window.togroup(i.name)),
        # MOVE WINDOW TO SELECTED WORKSPACE 1-10 AND FOLLOW MOVED WINDOW TO WORKSPACE
        Key([mod, "shift"], i.name, lazy.window.togroup(
            i.name), lazy.group[i.name].toscreen(toggle=False)),
    ])

# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
# BEGIN


@hook.subscribe.client_new
def assign_app_group(client):
    d = {}
    # Browsers
    d["1"] = ["Navigator", "Firefox", "Vivaldi-stable", "Vivaldi-snapshot", "Chromium", "Google-chrome", "Brave", "Brave-browser",
              "navigator", "firefox", "vivaldi-stable", "vivaldi-snapshot", "chromium", "google-chrome", "brave", "brave-browser", ]

    # Code Editors
    d["2"] = ["Atom", "Subl3", "Geany", "Brackets", "Code-oss", "Code", "TelegramDesktop", "Discord",
              "atom", "subl3", "geany", "brackets", "code-oss", "code", "telegramDesktop", "discord", ]

    # Terminals
    d["3"] = ["Terminator", "Termite", "Alacritty", "urxvt", "Xterm", "Konsole",
              "terminator", "termite", "alacritty", "urxvt", "xterm", "konsole"]

    # File Managers
    d["4"] = ["Thunar", "Nemo", "Caja", "Nautilus", "org.gnome.Nautilus", "Pcmanfm", "Pcmanfm-qt",
              "thunar", "nemo", "caja", "nautilus", "org.gnome.nautilus", "pcmanfm", "pcmanfm-qt", ]

    # Video Players
    d["5"] = ["Vlc", "vlc", "Mpv", "mpv", "smplayer", "smplayer", "qbittorrent"]

    # Audio Players
    d["6"] = ["spotify", "Spotify",  "Pragha", "Clementine", "Deadbeef", "Audacious",
                "pragha", "clementine", "deadbeef", "audacious"]

    wm_class = client.window.get_wm_class()[0]

    for i in range(len(d)):
        if wm_class in list(d.values())[i]:
            group = list(d.keys())[i]
            client.togroup(group)
            # Set toggle=False for not changing group if current group is same
            client.group.cmd_toscreen(toggle=False)
# END
# ASSIGN APPLICATIONS TO A SPECIFIC GROUPNAME
#####################################################################################################################################################################
############################# Groups (Workspaces) End ###############################################################################################################
#####################################################################################################################################################################


#####################################################################################################################################################################
############################# Layouts Start #########################################################################################################################
#####################################################################################################################################################################
layout_theme = {"margin": 5,
                "border_width": 1,
                "border_focus": color["border_focus"],
                "border_normal": color["border_normal"]
                }


layouts = [
    layout.MonadTall(margin=4, border_width=1,
                     border_focus=color["border_focus"], border_normal=color["border_normal"]),
    layout.MonadWide(margin=4, border_width=1,
                     border_focus=color["border_focus"], border_normal=color["border_normal"]),
    layout.Matrix(**layout_theme),
    layout.Bsp(**layout_theme),
    layout.Floating(**layout_theme),
    layout.RatioTile(**layout_theme),
    layout.Max(**layout_theme)
]
#####################################################################################################################################################################
############################# Layouts End ###########################################################################################################################
#####################################################################################################################################################################


#####################################################################################################################################################################
############################# Bar Start #############################################################################################################################
#####################################################################################################################################################################
widget_defaults = dict(font=MY_TEXT_FONT,
                       fontsize=MY_FONT_SIZE,
                       padding=5,
                       background=color['barBackground'])

prompt = "{0}@{1}: ".format(os.environ["USER"], socket.gethostname())

widgets_list = [
    ### Groups ###
    widget.GroupBox(
        font=ICON_FONT,
        fontsize=ICON_SIZE,
        padding = 10,
        borderwidth=0,
        disable_drag=True,
        active=color['groupActive'],
        inactive=color['groupForeground'],
        rounded=False,
        highlight_method="text",
        this_current_screen_border=color['currentGroup'],
        foreground=color['groupForeground'],
        background=color['groupBackground']
    ),
    widget.TextBox(
        font = ICON_FONT,
        fontsize = 40,
        text = "",
        padding = 0,
        foreground=color['groupBackground'],
        background = color['layoutBackground']
    ),

    ### Layouts ###
    widget.CurrentLayout(
        foreground=color['layoutForeground'],
        background=color['layoutBackground'],
    ),
    widget.TextBox(
        font = ICON_FONT,
        fontsize = 40,
        text = "",
        padding = 0,
        foreground=color['layoutBackground'],
    ),

    
    ### Window Name ###
    widget.WindowName(
        foreground=color['windowForeground'],
        background=color['windowBackground'],
        padding = 10
    ),

    ### Clock ###
    widget.Clock(
        foreground=color['clockForeground'],
        background=color['clockBackground'],
        format="%a, %b %d [ %I:%M %P ]",
        mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(
            MY_BROWSER + ' https://calendar.google.com/calendar')}
    ),
    widget.Spacer(
        length=bar.STRETCH,
    ),

    ### CPU ###
    widget.TextBox(font=ICON_FONT,fontsize=40,text="",padding=0,foreground=color['cpuBackground']),
    widget.TextBox(
        font=ICON_FONT,
        fontsize=ICON_SIZE,
        foreground=color['cpuForeground'],
        background=color['cpuBackground'],
        text="",
        mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(
            MY_TERMINAL + " -e htop")},
    ),
    widget.CPU(
        foreground=color['cpuForeground'],
        background=color['cpuBackground'],
        format='{load_percent}%',
        mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(
            MY_TERMINAL + " -e htop")},
    ),
    widget.Sep(linewidth=0,padding=SEP_PADDING,background=color['cpuBackground']),
    
    ### Memory ###
    widget.TextBox(font=ICON_FONT,fontsize=40,text="",padding=0,foreground=color['memoryBackground'],background=color['cpuBackground']),
    widget.TextBox(
        font=ICON_FONT,
        fontsize=ICON_SIZE,
        foreground=color["memoryForeground"],
        background=color["memoryBackground"],
        text="",
        mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(
            MY_TERMINAL + " -e htop")},
    ),
    widget.Memory(
        foreground=color["memoryForeground"],
        background=color["memoryBackground"],
        format='{MemUsed} / {MemTotal}',
        update_interval=1,
        mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(
            MY_TERMINAL + " -e htop")},
    ),
    widget.Sep(linewidth=0,padding=SEP_PADDING,background=color["memoryBackground"]),

    ### HDD ###
    widget.TextBox(font=ICON_FONT,fontsize=40,text="",padding=0,foreground=color['hddBackground'],background=color['memoryBackground']),
    widget.TextBox(
        font=ICON_FONT,
        fontsize=ICON_SIZE,
        foreground=color["hddForeground"],
        background=color["hddBackground"],
        text="",
        mouse_callbacks={
            'Button1': lambda qtile: qtile.cmd_spawn(MY_FILE_MANAGER)}
    ),
    widget.DF(
        foreground=color["hddForeground"],
        background=color["hddBackground"],
        format='{uf}{m} Free',
        visible_on_warn=False,
        mouse_callbacks={
            'Button1': lambda qtile: qtile.cmd_spawn(MY_FILE_MANAGER)}
    ),
    widget.Sep(linewidth=0,padding=SEP_PADDING,background=color["hddBackground"]),

    ### Volume ###
    widget.TextBox(font=ICON_FONT,fontsize=40,text="",padding=0,foreground=color['volBackground'],background=color['hddBackground']),
    widget.TextBox(
        font=ICON_FONT,
        fontsize=ICON_SIZE,
        foreground=color["volForeground"],
        background=color["volBackground"],
        text="",
        mouse_callbacks={
            'Button1': lambda qtile: qtile.cmd_spawn("pavucontrol")}
    ),
    widget.Volume(
        foreground=color["volForeground"],
        background=color["volBackground"],
    ),
    widget.Sep(linewidth=0,padding=SEP_PADDING,background=color["volBackground"]),
    
    ### Updates ###
    widget.TextBox(font=ICON_FONT,fontsize=40,text="",padding=0,foreground=color['updateBackground'],background=color['volBackground']),
    widget.TextBox(
        font=ICON_FONT,
        fontsize=ICON_SIZE,
        foreground=color["updateForeground"],
        background=color["updateBackground"],
        text="",
        mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(
            MY_TERMINAL + " -e yay -Syu"),
            'Button3': lambda qtile: qtile.cmd_spawn("set-pywal qtile -u")
            }
    ),
    widget.CheckUpdates(
        update_interval = 1800,
        foreground=color["updateForeground"],
        background=color["updateBackground"],
        no_update_string = 'All Good!',
        colour_have_updates=color["updatesAvailable"],
        colour_no_updates=color["updateForeground"],
        distro='Arch',
        display_format='{updates}',
        mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(
            MY_TERMINAL + " -e yay -Syu"),
            'Button3': lambda qtile: qtile.cmd_spawn("set-pywal qtile -u")
            }
    ),
    widget.Sep(linewidth=0,padding=SEP_PADDING,background=color["updateBackground"]),

    ### Wallpaper ###
    widget.TextBox(font=ICON_FONT,fontsize=40,text="",padding=0,foreground=color['walBackground'],background=color['updateBackground']),
    widget.TextBox(
        font=ICON_FONT,
        fontsize=ICON_SIZE,
        foreground=color["walForeground"],
        background=color["walBackground"],
        text="",
        mouse_callbacks={
            'Button1': lambda qtile: qtile.cmd_spawn("set-pywal qtile -n"),
            'Button3': lambda qtile: qtile.cmd_spawn("set-pywal qtile -p"),
            'Button2': lambda qtile: qtile.cmd_spawn("set-pywal qtile -u"),
            }
    ),
    widget.Sep(linewidth=0,padding=SEP_PADDING,background=color["walBackground"]),

    ### Sys Tray ###
    widget.TextBox(font=ICON_FONT,fontsize=40,text="",padding=0,foreground=color['trayBackground'],background=color['walBackground']),
    widget.Systray(
        background=color['trayBackground'],
        icon_size=ICON_SIZE,
        padding = SEP_PADDING,
    ),
    widget.Sep(linewidth=0,padding=SEP_PADDING,background=color['trayBackground']),

    ### Quick Exit ###
    widget.TextBox(font=ICON_FONT,fontsize=40,text="",padding=0,foreground=color['exitBackground'],background=color['trayBackground']),
    widget.TextBox(
        font=ICON_FONT,
        text="",
        foreground=color["exitForeground"],
        background=color["exitBackground"],
        padding=10,
        fontsize=ICON_SIZE,
        mouse_callbacks={'Button1': lambda qtile: qtile.cmd_spawn(LOGOUT_MANAGER)}
    ),
]

screens = [Screen(top=bar.Bar(widgets=widgets_list, size=PANEL_SIZE, opacity=1)),
            # Screen(top=bar.Bar(widgets=widgets_list, size=PANEL_SIZE, opacity=1))  ## For two monitors
                ]
#####################################################################################################################################################################
############################# Bar End ###############################################################################################################################
#####################################################################################################################################################################

# MOUSE CONFIGURATION
mouse = [
    Drag([mod], "Button1", lazy.window.set_position_floating(),
        start=lazy.window.get_position()),
    Drag([mod], "Button3", lazy.window.set_size_floating(),
        start=lazy.window.get_size()),
    Click([mod], "Button2", lazy.window.bring_to_front())
]

dgroups_key_binder = None
dgroups_app_rules = []

main = None

@hook.subscribe.startup_once
def start_once():
    home = os.path.expanduser('~')
    subprocess.call([home + '/.config/qtile/scripts/autostart.sh'])

@hook.subscribe.client_new
def set_floating(window):
    if (window.window.get_wm_transient_for()
            or window.window.get_wm_type() in floating_types):
        window.floating = True


floating_types = ["notification", "toolbar", "splash", "dialog"]


follow_mouse_focus = True
bring_front_click = False
cursor_warp = False
floating_layout = layout.Floating(float_rules=[
    {'wmclass': 'Arcolinux-welcome-app.py'},
    {'wmclass': 'Arcolinux-tweak-tool.py'},
    {'wmclass': 'confirm'},
    {'wmclass': 'dialog'},
    {'wmclass': 'download'},
    {'wmclass': 'error'},
    {'wmclass': 'file_progress'},
    {'wmclass': 'notification'},
    {'wmclass': 'splash'},
    {'wmclass': 'toolbar'},
    {'wmclass': 'confirmreset'},
    {'wmclass': 'makebranch'},
    {'wmclass': 'maketag'},
    {'wmclass': 'Arandr'},
    {'wmclass': 'feh'},
    {'wmclass': 'Galculator'},
    {'wmclass': LOGOUT_MANAGER},
    {'wmclass': 'xfce4-terminal'},
    {'wmclass': 'pavucontrol'},
    {'wname': 'branchdialog'},
    {'wname': 'Open File'},
    {'wname': 'Custom Actions'},
    {'wname': 'Create Action'},
    {'wname': 'pinentry'},
    {'wmclass': 'ssh-askpass'},
    {'wmclass': 'shotwell'},

],  fullscreen_border_width=0, border_width=0)
auto_fullscreen = True

focus_on_window_activation = 'focus'  # "focus" # or smart

wmname = "LG3D"
