export QT_QPA_PLATFORMTHEME=qt5ct

export ZSH="$HOME/.oh-my-zsh"

plugins=(git zsh-autosuggestions zsh-syntax-highlighting)

source $ZSH/oh-my-zsh.sh

source /usr/share/nvm/init-nvm.sh

eval "$(oh-my-posh init zsh --config ~/.config/oh-my-posh-themes/just_coffy.omp.json)"
