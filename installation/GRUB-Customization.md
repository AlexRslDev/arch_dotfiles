# GRUB Customization

### Recommended Themes

+ [CyberGRUB-2077](https://www.gnome-look.org/p/2235245)

![CyberGRUB-2077 Preview](https://images.pling.com/img/00/00/82/52/18/2235245/preview1.png)

+ [Kali-Linux-Gray-Theme](https://www.gnome-look.org/p/2186668)

![Kali-Linux-Gray-Theme Preview](https://images.pling.com/img/00/00/80/02/68/2186668/thumbnail.png)

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
