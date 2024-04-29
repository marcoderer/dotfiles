#######################
### OH MY ZSH SETUP ###
#######################

# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# If you come from bash you might have to change your $PATH.
export PATH=$HOME/bin:/usr/local/bin:$PATH
export PATH=$HOME/.local/bin:$PATH
# Path to your oh-my-zsh installation.
export ZSH="$HOME/.oh-my-zsh"

# Set name of the theme to load
ZSH_THEME="powerlevel10k/powerlevel10k"

# Enable command auto-correction.
ENABLE_CORRECTION="true"

plugins=(
  z
  git
  history
  colored-man-pages
  jsontools
  sudo
  copyfile
  web-search
  you-should-use
  zsh-autosuggestions
  zsh-syntax-highlighting
  dirhistory
  copypath
  )

source $ZSH/oh-my-zsh.sh

##########################
### USER CONFIGURATION ###
##########################

# Sourcing
source /home/marco/dev/shell/utils.sh

# exports for deno runtime
export DENO_INSTALL="/home/marco/.deno"
export PATH="$DENO_INSTALL/bin:$PATH"
# export MANPATH="/usr/local/man:$MANPATH"
export EDITOR=nvim
export VISUAL="$EDITOR"
export PATH="$PATH:/home/marco/.local/kitty.app/bin"

# ===>> Aliases <<===

# cd shorthands
alias dc="cd ~/.config/"
alias cdh="cd ~/"
alias mkcd='foo(){ mkdir -p "$1"; cd "$1" }; foo ' # mkdir and cd into it
alias cddl='cd ~/Downloads/'
alias cddt='cd ~/Desktop/'
alias cdcf='cd ~/.config/'
alias cdh='cd ~'
alias -g ...='../..'
alias -g ....='../../..'
alias -g .....='../../../..'
alias -g ......='../../../../..'
alias -- -='cd -'
alias 1='cd -1'
alias 2='cd -2'
alias 3='cd -3'
alias 4='cd -4'
alias 5='cd -5'
alias 6='cd -6'
alias 7='cd -7'
alias 8='cd -8'
alias 9='cd -9'

# Dir history
function d () {
  if [[ -n $1 ]]; then
    dirs "$@"
  else
    dirs -v | head -n 10
  fi
}
compdef _dirs d

# List directory contents
alias la='ls -A'
alias ll='ls -lh'
alias lla='ls -lAh'

# dotgit: aliases for git actions on bare .dotfiles repo
alias dg="git --git-dir=$HOME/.dotfiles/ --work-tree=$HOME"
alias dga="dg add"
alias dgc="dg commit -vm"
alias dgca="dg commit -avm"
alias dgp="dg push"
alias dgs="dg status"
alias gz="dga ~/.zshrc && dgc ~/.zshrc && dgp"
alias ga="dga ~/.config/alacritty/alacritty.toml && dgc  ~/.config/alacritty/alacritty.toml && dgp"

# edit and reload dotfiles
alias et="nvim ~/.tmux.conf"
alias ez="nvim ~/.zshrc"
alias ea="nvim  ~/.config/alacritty/alacritty.toml"
alias ek="nvim ~/.config/kitty/kitty.conf"
alias rz="exec zsh" #see: https://github.com/ohmyzsh/ohmyzsh/wiki/FAQ#how-do-i-reload-the-zshrc-file
alias ra="source ~/.config/alacritty/alacritty.toml"
alias rt="tmux source-file ~/.tmux.conf"
# shorthands
alias ta="tmux a"

# command tools
alias ls="lsd"
alias bat='batcat'

# other
alias colors="for i in {0..255}; do print -Pn "%K{$i}  %k%F{$i}${(l:3::0:)i}%f " ${${(M)$((i%6)):#3}:+$'\n'}; done"
alias myip="curl http://ipecho.net/plain; echo"
alias tpl="powerlevel10k_plugin_unload; PS1='>> '"



# ===>> Run & source <<===

# Powerline10 k (to customize, run `p10k configure` or edit ~/.p10k.zsh.)
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh
# eval "$(zoxide init zsh)"

export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion
