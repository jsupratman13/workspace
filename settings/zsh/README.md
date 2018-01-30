# Install ZSH
```
sudo apt-get install zsh
```

# Change Shell
```
which zsh
chsh
```

# Install Oh My ZSH
```
cd
sh -c "$(curl -fsSL https://raw.github.com/robbyrussell/oh-my-zsh/master/tools/install.sh)"

```

# Setup Powerline
```
cd
wget https://github.com/powerline/powerline/raw/develop/font/PowerlineSymbols.otf
wget https://github.com/powerline/powerline/raw/develop/font/10-powerline-symbols.conf
mv PowerlineSymbols.otf ~/.fonts/
mkdir -p .config/fontconfig/conf.d 
fc-cache -vf ~/.fonts/
mv 10-powerline-symbols.conf ~/.config/fontconfig/conf.d/
```

# Change Theme to Solarize
```
sudo apt-get install dconf-cli
git clone http://github.com/sigurdga/gnome-terminal-colors-solarized.git ~/.solarized
cd ~/.solarized
./install.sh
```
* Recommend option 1
* Select option 1 to download seebi dirscolors-solarized

# Set Theme
Open theme and change theme and add line
```
ZSH_THEME="agnoster"
eval `dircolors ~/.dir_colors/dircolors`
```

