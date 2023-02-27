# kata
Lab on Flask

## Setup the project in dev mode

First clone the repository

```sh
git clone https://github.com/billkurios/kata.git
```

When it's doned, in the repository folder create a [python virtual environment](https://docs.python.org/3/library/venv.html).
```sh
cd [your_local_path]/kata

python3 -m venv .venv
```
*.venv* I used specially this name because it's already defined to be ignored in my .gitignore file. We don't want to track changes on this folder.
Now activate the virtual environment.
```sh
source .venv/bin/activate
```
To deactivate, just run *deactivate* command.

Now install all dependencies required by the project.
```
pip install -r requirements.txt
```