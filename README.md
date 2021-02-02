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
```bash
$ pyenv install 3.9.0
$ pyenv virtualenv 3.9.0 qa_render_template
$ pyenv activate qa_render_template
$ pip install flask 
$ pip freeze > ./requirements/base.txt
```