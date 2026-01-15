# Install Applications

### Yay Apps

```
yay -S --needed figma-linux-bin visual-studio-code-bin webapp-manager iriunwebcam-bin ccrypt burpsuite vesktop-bin ab-download-manager-bin localsend-bin
```

### Pacman Apps

```
sudo pacman -S --needed obs-studio kdeconnect gparted mtools dosfstools ntfs-3g exfatprogs f2fs-tools vlc vlc-plugins-all 7zip unrar zip unzip rustup qbittorrent syncthing
```

### Notes

- For Rust:

```
rustup default stable
```

- For Syncthing (Run to startup):

```
systemctl --user enable --now syncthing.service
```

### Virtual Machines

```
sudo pacman -S --needed qemu-desktop virt-manager libvirt dnsmasq iptables-nft edk2-ovmf bridge-utils ebtables

sudo systemctl enable --now libvirtd

sudo usermod -aG libvirt $USER

sudo virsh net-autostart default
sudo virsh net-start default
sudo virsh net-start default
```

**Note:** Verify kvm modules:

```
sudo modprobe kvm-intel
```

### Steam, Wine, Lutris for Gaming

```

sudo pacman -S --needed lutris wine-staging wine-gecko winetricks giflib lib32-giflib lib32-gnutls lib32-v4l-utils lib32-libpulse lib32-alsa-plugins lib32-libxcomposite lib32-libxinerama lib32-ncurses lib32-libxml2 lib32-freetype2 lib32-libpng lib32-sdl2 lib32-mesa vulkan-intel lib32-vulkan-intel steam

yay -S protonup-qt
```

### Flatpak Apps

```
flatpak install flathub -y --or-update com.bitwarden.desktop com.github.PintaProject.Pinta com.github.flxzt.rnote com.github.huluti.Curtail com.github.tenderowl.frog com.github.unrud.VideoDownloader com.jeffser.Pigment com.protonvpn.www com.rafaelmardojai.Blanket com.rafaelmardojai.SharePreview com.spotify.Client com.warlordsoftwares.formatlab io.github.alainm23.planify io.github.bytezz.IPLookup io.github.shundhammer.qdirstat io.github.wartybix.Constrict io.github.zefr0x.hashes io.gitlab.adhami3310.Converter it.mijorus.gearlever me.iepure.devtoolbox org.feichtmeier.Musicpod org.gnome.Loupe org.gnome.Mines org.gnome.Papers org.gnome.TextEditor org.inkscape.Inkscape org.kde.kalk org.kde.kdenlive org.kde.kruler org.onlyoffice.desktopeditors org.sqlitebrowser.sqlitebrowser org.telegram.desktop org.tenacityaudio.Tenacity org.upscayl.Upscayl rest.insomnia.Insomnia org.gnome.baobab
```

### Reminder

Remember Install your web apps: Zynga Poker, Whatsapp, Notion, Flathub, and install another apps like: Osu.
