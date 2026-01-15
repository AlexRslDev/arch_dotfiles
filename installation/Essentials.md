# Essentials

### Install Yay

```
git clone https://aur.archlinux.org/yay.git
cd yay
makepkg -si
cd
rm -rf yay
```

### Install Flatpak

```
sudo pacman -S --needed flatpak
```

**Note:** Reboot to apply changes.

### Polkit

```
sudo pacman -S --needed polkit-gnome
```

### Keyring

```
sudo pacman -S --needed gnome-keyring seahorse libsecret
```

Auto-Unlock: The file **/etc/pam.d/login** must has this lines at the end:

```
auth      optional     pam_gnome_keyring.so
session   optional     pam_gnome_keyring.so     auto_start
```

After reboot verify:

```
ps aux | grep gnome-keyring
```

**Chromium based browsers error:**

Chromium-based browsers: Sometimes they require an extra parameter. If it doesn't detect the keyring, try launching them with: --password-store=gnome-keyring
