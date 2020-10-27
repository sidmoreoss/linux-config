# My Linux Config

## Drivers
>Alsa
  - For Realtek ALC3246 sound chipset alsa needs modprobe configuration.
  - Run the script [install realtek] to pass modprobe parameters to Alsa driver or copy the **realtek_alc3246.conf** file to **/etc/modprobe.d/**.
  - For auto muting channels use/install PulseAudio.
  - To install PulseAudio run the script [install pulse].
>Nvidia
  - Follow the steps on [Intel-Nvidia Hybrid] for Manjaro.
  - Arch and Arch based distros have similar Nvidia driver installation process.
 >Screen Tearing with picom
- Sometimes you may notice screen tearing with picom.
- Try *vsync = True* in picom [config] file.
- If the problem persists copy the file [20-intel.conf] to /etc/X11/xorg.conf.d/ folder.
- For more information refer:  https://www.maketecheasier.com/get-rid-screen-tearing-linux/
> Handle Screen Brightness

Run the following commands to handle brightness keys using xfce4-power-manager.
```sh
$ sudo pacman --needed -S xfce4-power-manager xfce4-settings xfconf
$ xfconf-query -c xfce4-power-manager -p /xfce4-power-manager/handle-brightness-keys --create -t bool -s true
```

## Configuration
To install dependencies and favorite **apps** and **fonts** run the script [Install Favorites].
## Bash 
- Copy the contents of [Bash] to home directory ($HOME).
### Qtile
Qtile is a tiling window manager for linux written in Python.
```s
$ sudo pacman --needed -S qtile
```
Python-pywal is a tool to pick colorschemes from wallpapers, it has already been installed by [Install Favorites] script.
- Requires [Install Favorites] to be run to install all dependencies.
- Copy **[qtile]** to $HOME/.config/ and **restart qtile** using the command 
```sh
$ qtile-cmd -o cmd -f restart.
```

### i3
i3 is a tiling window manager for linux written in C.
```s
$ sudo pacman --needed -S i3 polybar
```
- Copy **[i3]** to $HOME/.config/ 
- Now configure polybar using the steps given below and **restart i3** using the command
``` sh
$ i3-msg restart.
```

### Dunst *(Light-weight notification daemon)*
```sh
$ sudo pacman --needed -S dunst
```
- **Qtile** handles dunst configuration **automatically** if installed by above method.
- For **i3**, **copy** [dunst] to $HOME/.config/

### Polybar
- **Qtile** doesn't require polybar.
- **i3**: Copy [polybar] to $HOME/.config/

### Configuring GTK themes
Use *xfce4-appearance-settings* to apply **color schemes** and **fonts**.
Visit *https://www.gnome-look.org/browse/cat/* for more themes.

### Configuring Qt themes
Install Kvantum and qt5ct to configure qt applications.
```sh
sudo pacman --needed -S kvantum-qt5 qt5ct
```
Visit *https://store.kde.org/browse/cat/123/order/latest/* for more themes.

### Lightdm
##### Installation:
```sh
$ sudo pacman --needed -S lightdm light-locker
$ sudo systemctl enable lightdm.service
```
##### Configuration:
Follow the steps in *https://wiki.archlinux.org/index.php/LightDM#Webkit2_greeter*


   [Intel-Nvidia Hybrid]: <https://archived.forum.manjaro.org/t/guide-install-and-configure-optimus-manager-for-hybrid-gpu-setups-intel-nvidia/92196>
   [install realtek]: <https://github.com/SiddharthMMore/linux-config/blob/master/Drivers/Alsa/install_realtek_alc3246>
   [install pulse]: <https://github.com/SiddharthMMore/linux-config/blob/master/Drivers/Alsa/install_pulse>
   [20-intel.conf]: <https://github.com/SiddharthMMore/linux-config/blob/master/Drivers/Intel%20Display%20Driver/20-intel.conf>
   [config]: <https://github.com/SiddharthMMore/linux-config/blob/master/.config/qtile/scripts/picom.conf>
   [Install Favorites]: <https://github.com/SiddharthMMore/linux-config/blob/master/Scripts/install_favorite_apps>
   [Bash]: <https://github.com/SiddharthMMore/linux-config/tree/master/Bash>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
