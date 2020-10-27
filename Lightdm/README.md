To change lightdm themes to Litarvan (Arch recommended):

1) Ensure that 'lightdm-webkit2-greeter lightdm-webkit-theme-litarvan' are installed
    sudo pacman -S lightdm-webkit2-greeter lightdm-webkit-theme-litarvan

2) Edit '/etc/lightdm/lightdm.conf' and set 'greeter-session=lightdm-webkit2-greeter'

3) Edit '/etc/lightdm/lightdm-webkit2-greeter.conf' and set 'theme' or 'webkit-theme' to 'litarvan'

4) Relax!


Ref: https://github.com/Litarvan/lightdm-webkit-theme-litarvan