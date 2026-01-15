# Rice

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
sudo pacman -S --needed i3-wm i3blocks i3status xss-lock xorg-xset maim xclip xcolor rofi feh picom kitty dunst network-manager-applet xorg-xrandr xdg-desktop-portal xdg-desktop-portal-gtk cmatrix

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
sudo pacman -S --needed gcc make cmake curl wget gwenview neovim qt5ct qt6ct
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
sudo pacman -S --needed gnome-themes-extra xdg-desktop-portal xdg-desktop-portal-gtk

yay -S gtk-engine-murrine gtk-engines

sudo pacman -S lxappearance
```

Copy this dirs into your ".config":

```
cp -r .config/gtk-4.0/ .config/gtk-3.0/ .config/xdg-desktop-portal/ ~/.config

cp .xprofile ~/
```

Copy the themes into dotfiles to the themes local dirs:

```
mkdir ~/.local/share/themes

cp -r .local/share/themes/* ~/.local/share/themes/
```

**Note:** You can create "~/.themes/" and ~/.icons/ also and copy the themes and icons there to ensure that the config files find them.

**How to Theming**

Automatic Way

You can open lxappearance and set your theme, icons, cursor and then apply it.

Manual Way

Open ".config/gtk-3.0/settings.ini", ".config/gtk-4.0/settings.ini", ".xprofile" and change the theme name for the new one, and the same thing for icons or cursor.

**Note:** If after change the theme you can see it, restart your pc.

How to know if dark mode is working?

```
dbus-send --print-reply --dest=org.freedesktop.portal.Desktop /org/freedesktop/portal/desktop org.freedesktop.portal.Settings.Read string:'org.freedesktop.appearance' string:'color-scheme'
```

if it returns "uint32 1" it's dark theme on.
