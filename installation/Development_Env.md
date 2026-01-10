# Development Environment Configuration

### Node And NVM

```
yay -S nvm
nvm install node
```

### Terminal

```
sudo pacman -S zsh
chsh -s $(which zsh)
```

**Note**: Logout to apply changes.

```
sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)"
source ~/.zshrc
```

```
yay -S oh-my-posh-bin
```

### Docker

```
sudo pacman -S docker docker-compose
sudo systemctl enable --now docker.service
sudo usermod -aG docker $USER
```
