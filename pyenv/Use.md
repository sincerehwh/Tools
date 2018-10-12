
https://github.com/pyenv/pyenv


### 1.安装

git clone https://github.com/pyenv/pyenv.git ~/.pyenv

brew install pyenv

### 2.配置

Mac Bash:
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile

Ubutu Bash:
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bashrc
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bashrc

Mac Zsh:
echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.zshenv
echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.zshenv


#### 重启Shell
exec "$SHELL"

### 4.更新 

cd $(pyenv root)
git pull 
// git fetch 
// git tag 
// git checkout v0.1.0

### 5.卸载

移除2文件中的路径
rm -rf $(pyenv root)

brew uninstall pyenv 

### 6.使用

pyenv install 3.6.0

