# GRUB Customization

### Recommended Themes

+ [CyberGRUB-2077](https://www.gnome-look.org/p/2235245)
+ [Kali-Linux-Gray-Theme](https://www.gnome-look.org/p/2186668)

### How to install themes

1. Download the theme.
2. Extract it.
3. Copy the theme to the GRUB Themes Route.

```
sudo cp -r /Downloads/Your-Theme/ /boot/grub/themes/
```

4. Set theme into the GRUB config file.

```
sudo nvim /etc/default/grub

# Uncomment and replace with your theme.
GRUB_THEME="/boot/grub/themes/Your-Theme/theme.txt"
```

5. Apply Changes.

```
sudo grub-mkconfig -o /boot/grub/grub.cfg
```

6. Reboot to see the changes.

### Notes

+ Some themes brings "install.sh" in that case you can "sudo ./install.sh" to install the theme automatically.
