### Install Arch Linux

+ Download arch linux iso.
+ Boot it into a pendrive.
+ Verify Internet conection

```
ping -c 5 google.com
```

(if it has not conection)

```
iwctl
device list
```

(if it's off)

```
device wlan0 set-property Powered on
station wlan0 get-networks
station wlan0 connect [wifi name]
exit

ping -c 5 googe.com
```

(optional) <- formatting disk.

```
lsblk
gdisk /dev/[your disk name]
x
z

lsblk  <- to check if it's clean.
```

+ archinstall

```
archinstall
```

**NOTE**: Install Hyprland with archinstall.

### After Reboot: Activate Wifi

```
sudo nmcli dev wifi connect [wifi name] password [wifi password]
```

### Update System

```
sudo pacman -Syyu
```

### Essential Dependencies

```
sudo pacman -S gcc make cmake git curl perl wget gwenview neovim
```

### Install SDDM

```
bash -c "$(curl -fsSL https://raw.githubusercontent.com/keyitdev/sddm-astronaut-theme/master/setup.sh)"
```

Repo: [sddm-astronaut-theme](https://github.com/Keyitdev/sddm-astronaut-theme)

### Install DankMaterialShell

```
curl -fsSL https://install.danklinux.com | sh
```
