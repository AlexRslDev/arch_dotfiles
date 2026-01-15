# Fix Errors

### Figma-Linux

Go to "/usr/share/applications/" and paste this into "figma-linux.desktop":

```
[Desktop Entry]
Name=Figma Linux
Comment=Unofficial desktop application for linux
Exec=figma-linux --disable-gpu-sandbox --ignore-gpu-blocklist --enable-gpu-rasterization --enable-zero-copy %U
Terminal=false
Type=Application
Icon=figma-linux
StartupWMClass=figma-linux
Categories=Graphics;
MimeType=application/figma;x-scheme-handler/figma;
```
