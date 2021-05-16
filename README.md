# My Linux Config

## Install KDE config and favorite applications
{{distro}} is the current distro you are using

Supported distros are **arch, fedora, ubuntu**

```s
$ cd ~/.cache
$ clone git git@github.com:sidmoreoss/linux-config.git
$ cd linux-config
$ chmod -R +xr *
$ ./Scripts/kde/{{distro}}/{{distro}}-setup
```

## To only install favorite applications run
{{package manager}} is the package manager for your distro

Supported package managers are **pacman, apt, dnf**

```s
$ cd ~/.cache
$ clone git git@github.com:sidmoreoss/linux-config.git
$ cd linux-config
$ chmod -R +xr *
$ ./Scripts/common/install_favorites {{package manager}} {{desktop env}}
```

## To install ZSH with Oh-My-Zsh and plugins
```s
$ cd ~/.cache
$ clone git git@github.com:sidmoreoss/linux-config.git
$ cd linux-config
$ chmod -R +xr *
$ ./Scripts/common/install_zsh
```

## Python-pywal (get colors from image)
Python-pywal is a tool to pick colorschemes from wallpapers, it should be installed by [Install Favorites] script, if not do the following.

```s
$ pip3 install pywal
```


### Configuring Qt themes and effects
Install Kvantum to configure qt applications(should be installed automatically by [Install Favorites]).

```sh
$ sudo pacman --needed -S kvantum-qt5 qt5ct
```

Visit [KDE Store] for more themes.

[KDE Store]: https://store.kde.org/
[Install Favorites]: https://github.com/sidmoreoss/linux-config/blob/stable/Scripts/common/install_favorites