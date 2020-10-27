### For Realtek Alc 3246 just copy modprobe.conf to /etc/modprobe.d/ with pulseaudio installed
Note: Pulseaudio is only required to mute channels automatically and mixing

#### IN CASE OF WRONG ALSA CONFIG DO THE FOLLOWING ####

With Intel Corporation HD Audio Controller on laptop, you may need to add this line to modprobe or sound.conf:

'options snd-hda-intel model=model'

Where model is any one of the following:
dell-m6
dell-vostro
generic
laptop
laptop-hpsense
olpc-xo-1_5
dell-inspiron-7559
Note: It may be necessary to put this "options" line below (after) any "alias" lines about your card.
You can see all the available models in the kernel documentation. For example https://www.kernel.org/doc/html/latest/sound/hd-audio/models.html, but check that it is the correct version of that document for your kernel version.

A list of available models is also available here. To know your chip name type the following command (with * being corrected to match your files). Note that some chips could have been renamed and do not directly match the available ones in the file.

$ grep Codec /proc/asound/card*/codec*
Note that there is a high chance none of the input devices (all internal and external mics) will work if you choose to do this, so it is either your headphones or your mic. Please report to ALSA if you are affected by this bug.

And also, if you have problems getting beeps to work (pcspkr):
options snd-hda-intel model=$model enable=1 index=0

### Important ###
If you are using 'options snd-hda-intel model=dell-inspiron-7559'  you need pulseaudio to manage alsa mixer.

If you can't get to achieve the preferred sound quality try this.
options snd-hda-intel probe_mask=0x101 


If your hear high pitched or distorted sound, its always related to alsa because pulseaudio doesn't add distortion on its own
Follow the above steps to configure alsa correctly

If you have problems configuring with above methods try visiting and gathering information from below sites.

https://nint.us/181963
https://www.kernel.org/doc/html/latest/sound/hd-audio/notes.html#codec-probing-problem
https://bbs.archlinux.org/viewtopic.php?id=234965
https://bbs.archlinux.org/viewtopic.php?id=222322
https://wiki.archlinux.org/index.php/Kernel_module#Setting_module_options
https://wiki.archlinux.org/index.php/Advanced_Linux_Sound_Architecture/Troubleshooting
