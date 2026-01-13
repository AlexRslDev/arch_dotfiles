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
sudo pacman -S --needed i3-wm i3blocks i3status xss-lock xorg-xset maim xclip rofi feh picom kitty dunst network-manager-applet xorg-xrandr xdg-desktop-portal xdg-desktop-portal-gtk

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

### Cursor and Icons

Move "./.local/share/icons/" to "~/.local/share/icons/"

```
mkdir ~/.local/share/icons

cp -r .local/share/icons/* ~/.local/share/icons/
```

After that, set them into lxappearance.

### Themes

```
sudo pacman -S gnome-themes-extra

yay -S gtk-engine-murrine gtk-engines

sudo pacman -S lxappearance
```

Into "~/.config/xdg-desktop-portal/settings.ini" paste:

```
[Settings]
color-scheme=1
```

Copy the themes into dotfiles "./.local/share/themes/" to "~/.local/share/themes/".

```
mkdir ~/.local/share/themes

cp -r .local/share/themes/* ~/.local/share/themes/
```

Open lxappearance and set a "-dark" theme.

Force to ensure to apply it for GTK3 and GTK4. Into "~/.config/gtk-3.0/settings.ini" and "~/.config/gtk-4.0/settings.ini":

```
[Settings]
gtk-application-prefer-dark-theme=1
gtk-theme-name=Adwaita-dark
```

For Qt Apps

```
sudo pacman -S qt5ct qt6ct
```
