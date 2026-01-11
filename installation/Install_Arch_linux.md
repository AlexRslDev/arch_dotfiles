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

**NOTE**: Install the desktok that you want with archinstall.

### After Reboot: Activate Wifi

```
sudo nmcli dev wifi connect [wifi name] password [wifi password]
```

### Update System

```
sudo pacman -Syyu
```
