# QA Render Template 


# Setup 
## First commands 

```bash
$ mkdir qa_render_template
$ cd qa_render_template
$ git init 
$ touch .gitignore
$ mkdir ./requirements
$ touch ./requirements/base.txt
```

## Env commands

Install tools
```bash
# Install brew
$ /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"

# Install pyenv 
$ git clone https://github.com/pyenv/pyenv.git ~/.pyenv

# Install pyenv in profile
$ echo 'export PYENV_ROOT="$HOME/.pyenv"' >> ~/.bash_profile
$ echo 'export PATH="$PYENV_ROOT/bin:$PATH"' >> ~/.bash_profile
$ echo 'PYENV_VIRTUALENV_DISABLE_PROMPT=1' >> ~/.bash_profile
$ echo 'eval "$(pyenv init -)"' >> ~/.bash_profile
$ echo 'eval "$(pyenv virtualenv-init -)"' >> ~/.bash_profile
```

Install python enviroment
```bash
$ pyenv install 3.9.0
$ pyenv virtualenv 3.9.0 qa_render_template
$ pyenv activate qa_render_template
$ pip install flask 
$ pip freeze > ./requirements/base.txt
```