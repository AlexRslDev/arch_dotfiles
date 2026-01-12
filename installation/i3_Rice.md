# i3 Rice

### Install Audio

```
sudo pacman -S --needed pipewire-pulse pavucontrol alsa-utils
```

### Bluetooth

```
sudo pacman -S --needed bluez bluez-utils blueman
sudo systemctl enable --now bluetooth
```

### Install Yay

```
sudo pacman -S --needed base-devel git

git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si

cd
rm -rf yay
```

### Install i3

```
sudo pacman -S i3-wm i3blocks i3status xss-lock xorg-xset xclip rofi feh picom kitty dunst network-manager-applet

yay -S i3lock-color
yay -S caffeine-ng
```

### Install ly

```
yay -S ly

systemctl enable ly@tty2.service
systemctl disable getty@tty2.service
```

**NOTE:** Config file: /etc/ly/config.ini

### Essential Dependencies

```
sudo pacman -S --needed gcc make cmake curl wget gwenview neovim 
```

**NOTE:** Ensure that you make "chmod +x .config/i3/scripts/lock.sh"
