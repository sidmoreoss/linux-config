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
- Copy **[i3]** to $HOME/.config/ and **restart i3** using the command 
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

### Plugins

Dillinger is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md][PlDb] |
| GitHub | [plugins/github/README.md][PlGh] |
| Google Drive | [plugins/googledrive/README.md][PlGd] |
| OneDrive | [plugins/onedrive/README.md][PlOd] |
| Medium | [plugins/medium/README.md][PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md][PlGa] |


### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantaneously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 8080, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version} .
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 8080 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

#### Kubernetes + Google Cloud

See [KUBERNETES.md](https://github.com/joemccann/dillinger/blob/master/KUBERNETES.md)


### Todos

 - Write MORE Tests
 - Add Night Mode

License
----

MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


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
