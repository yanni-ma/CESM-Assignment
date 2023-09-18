# .bash_profile

# Get the aliases and functions
if [ -f ~/.bashrc ]; then
	. ~/.bashrc
fi

# User specific environment and startup programs
if [ -f "$HOME/openrc" ]; then
    source "$HOME/openrc"
fi
