export QT_QPA_PLATFORMTHEME=qt5ct

source /usr/share/nvm/init-nvm.sh

plugins=(
    git 
    zsh-autosuggestions 
    zsh-syntax-highlighting
)

eval "$(oh-my-posh init zsh --config ~/.config/oh-my-posh-themes/just_coffy.omp.json)"
