# What is this?
- **hyprwallpaper** is a simple terminal application written for linux distributions with the hyprland environment set up along with hyprpaper as the wallpaper manager.
- This simple program written in python allows the user the quickly switch between different wallpapers without having to go into their config file to change it.

# How do i use it?
## Dependencies
- one of the dependencies of this program is [mpvpaper](https://github.com/GhostNaN/mpvpaper) if you would like to be able to have video wallpapers
- another dependency is [hyprpaper](https://wiki.hyprland.org/Hypr-Ecosystem/hyprpaper/)

## Installation
- download the program with pip - [pypi project site](https://pypi.org/project/hyprwallpaper/)
```
pip install hyprwallpaper
```
- make sure your config files are located in /home/*your username*/.config/hypr/
```
python3 -m hyprwallpaper
```
- just follow the simple prompts given in the program
- if you have a GUI file manager like Dolphin, you can just drag and drop the picture you want as your wallpaper into the terminal, which will write out the entire path of the image automatically (*on most terminals, at least*)
- after you are done you can log out and back in to see yrou changes. *logging out is usually down with Ctrl+m in hyprland*

# features
- Can modify your hyprpaper.conf and hyprland.conf files to change your image wallpaper or video wallpaper
- ensures wallpaper program runs in the background

# message
- this is a small beginner project I made for myself to make switching between my wallpapers faster. I am aware that it is very elementary and can use a lot more improvements, which I hope to add in the future as I become better at programming
- any suggestions are welcome :) I will try my best to address them
