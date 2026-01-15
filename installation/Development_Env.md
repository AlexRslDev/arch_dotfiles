# Development Environment Configuration

### Node And NVM

```
yay -S --needed nvm
nvm install node
```

### Terminal

```
sudo pacman -S --needed zsh
chsh -s /usr/bin/zsh

git clone https://github.com/zsh-users/zsh-autosuggestions ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-autosuggestions
git clone https://github.com/zsh-users/zsh-syntax-highlighting.git ${ZSH_CUSTOM:-~/.oh-my-zsh/custom}/plugins/zsh-syntax-highlighting
source ~/.zshrc
```

**Note**: Logout to apply changes.

```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
source ~/.zshrc
```

```
yay -S --needed oh-my-posh-bin
```

### Docker

```
sudo pacman -S --needed docker docker-compose
sudo systemctl enable --now docker.service
sudo usermod -aG docker $USER
```

### Git Credentials

```
yay -S --needed git-credential-oauth
git config --global credential.helper oauth
```

### Python

```
sudo pacman -S --needed python python-pip
```
