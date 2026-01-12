# i3 Rice

### Essential Dependencies

```
sudo pacman -S --needed pipewire-pulse pavucontrol alsa-utils gcc make cmake git curl wget gwenview neovim xorg-xset xclip rofi feh picom kitty dunst network-manager-applet

yay -S caffeine-ng
```

### Bluetooth

```
sudo pacman -S --needed bluez bluez-utils blueman
sudo systemctl enable --now bluetooth
```

### i3lock

```
sudo pacman -Rs i3lock
yay -S i3lock-color
```

### Install ly

**NOTE:** Ensure that you make "chmod +x .config/i3/scripts/lock.sh"
