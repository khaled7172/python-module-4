# Set up the prompt
autoload -U colors && colors
setopt prompt_subst
PROMPT='%F{white}%n %~ $(git rev-parse --abbrev-ref HEAD 2>/dev/null | sed "s/.*/(&)/")%f
❯ '
setopt histignorealldups sharehistory
# Use emacs keybindings even if our EDITOR is set to vi
bindkey -e
# Keep 1000 lines of history within the shell and save it to ~/.zsh_history:
HISTSIZE=1000
SAVEHIST=1000
HISTFILE=~/.zsh_history
# Use modern completion system
autoload -Uz compinit
compinit
zstyle ':completion:*' auto-description 'specify: %d'
zstyle ':completion:*' completer _expand _complete _correct _approximate
zstyle ':completion:*' format 'Completing %d'
zstyle ':completion:*' group-name ''
zstyle ':completion:*' menu select=2
eval "$(dircolors -b)"
zstyle ':completion:*:default' list-colors ${(s.:.)LS_COLORS}
zstyle ':completion:*' list-colors ''
zstyle ':completion:*' list-prompt %SAt %p: Hit TAB for more, or the character to insert%s
zstyle ':completion:*' matcher-list '' 'm:{a-z}={A-Z}' 'm:{a-zA-Z}={A-Za-z}' 'r:|[._-]=* r:|=* l:|=*'
zstyle ':completion:*' menu select=long
zstyle ':completion:*' select-prompt %SScrolling active: current selection at %p%s
zstyle ':completion:*' use-compctl false
zstyle ':completion:*' verbose true
zstyle ':completion:*:*:kill:*:processes' list-colors '=(#b) #([0-9]#)*=0=01;31'
zstyle ':completion:*:kill:*' command 'ps -u $USER -o pid,%cpu,tty,cputime,cmd'
# Custom config
alias l='ls -l'
alias go2="cd ~/sgoinfre/core/python"
alias go1="cd ~/sgoinfre/core"
alias ..="cd .."
alias q="exit"
alias ce="code ."
alias cl="clear"
alias ob="~/sgoinfre/obsidian/Obsidian-1.5.12.AppImage"
alias f="flake8"
alias ga="git add ."
alias gc="git commit -m \"project commit\""
alias gp="git push"
BINDIR="${XDG_BIN_HOME:-$HOME/.local/bin}"
if ! echo $PATH | grep "$BINDIR" >/dev/null 2>&1; then
export PATH="$PATH:$BINDIR"
fi
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"
# Load zsh-autosuggestions from sgoinfre (42 safe delay)
for i in {1..5}; do
if [ -f ~/sgoinfre/zsh-autosuggestions/zsh-autosuggestions.zsh ]; then
source ~/sgoinfre/zsh-autosuggestions/zsh-autosuggestions.zsh
break
fi
sleep 0.2
done