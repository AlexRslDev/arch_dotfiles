### Install Arch Linux

+ Download arch linux iso.
+ Boot it into a pendrive.

1. Identify the usb, it's usually sbd or sbdc.

```
lsblk
```

1. Unmount the usb.

```
sudo umount /dev/sdb*
```

1. Boot Iso in the usb.

```
sudo dd bs=4M if=archlinux-xxxx.iso of=/dev/sdb status=progress oflag=sync
```

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

**NOTE**: Install the desktop or wm, audio (pipewire), Bluetooth, NetworkManager, Session Manager (ly,sddm...), directly from archinstall, it's because archinstall ensure to install everything to make all works out of the box for you.

### After Reboot (if you don't have ly or sddm): Activate Wifi

```
sudo nmcli dev wifi connect [wifi name] password [wifi password]
```

### Update System

```
sudo pacman -Syyu
```
