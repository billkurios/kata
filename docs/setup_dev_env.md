## Setup the project in dev mode

First clone the repository

```sh
git clone https://github.com/billkurios/kata.git
```

### Install project dependencies

Create a [python virtual environment](https://docs.python.org/3/library/venv.html).
```sh
cd [your_local_path]/kata

python3 -m venv .venv
```
*.venv* I used specially this name because it's already defined to be ignored in my .gitignore file. We don't want to track changes on this folder.
So if you use another name, make sure you ignore tracking changes on it.

Now activate the virtual environment.
```sh
source .venv/bin/activate
```

To deactivate, just run *deactivate* command.

Now install all dependencies required by the project.
```
pip install -r requirements.txt
```

### add .env file
This file would contains environement variables required to run the project.
Especially, I use the keyword *.env* because it's already defined to be ignored in the .gitignore file.
So If you use another name, make sure you ignore tracking changes on it.

```txt
FLASK_DEBUG=True
FLASK_APP='.'
SECRET_KEY='MY_SECRET_KEY'
HOST='127.0.0.1'
PORT=3000

DB_HOST='127.0.0.1'
DB_NAME='properties'
DB_PASSWORD='secure_password'
DB_PORT=5423
DB_USERNAME='kata'
SQLALCHEMY_DATABASE_URI='postgresql://${DB_USERNAME}:${DB_PASSWORD}@${DB_HOST}:${DB_PORT}/${DB_NAME}'

DB_VOLUME_DIR='/Users/dev_bill/Projects/kata/postgres_data'
```
This is a sample of this file.

### Make sure you have a database running

First, you need to make sure you have installed [Docker](https://www.docker.com/) Engine on your computer.
If not, you can follow this [official guidelines](https://docs.docker.com/engine/install/) depending on your operating system (OS).

Run this command to start a postgres container on your machine.
```sh
docker run --name <container_name> -e POSTGRES_USER=<postgres_user> -e POSTGRES_DB=<db_name> -e POSTGRES_PASSWORD=<postgres_user_password> -v <vol_path_dir>:/var/lib/postgresql/data -p <db_port>:5432 postgres:14-alpine
```
*<container_name>* You can put *postgres*
*<postgres_user>* You can put *kata*
*<db_name>* You can put *properties*
*<postgres_user_password>* You can put *secure_password*
*<vol_path_dir>* You can put */Users/dev_bill/Projects/kata/postgres_data*
*<db_port>* You can put *5423*

I use postgres image version *14-alpine*, you can use any recent version depending of your choice.

So as example, the command could be
```sh
docker run --name postgres -e POSTGRES_USER=kata -e POSTGRES_DB=properties -e POSTGRES_PASSWORD=secure_password -v /Users/bill/Projects/kata/postgres_data:/var/lib/postgresql/data -p 5423:5432 postgres:14-alpine
```

If like me, you create your postgres volume folder in your project folder, make sure this folder (for it's *postgres_data*) is ignored in .gitignore file.

Now run your command to launch your postgres container.

### Make migrations to initialize database

...

### Run Our flask application

```sh
flask --env-file=.env run --host=127.0.0.1 --port=3000
```
Here I pass *.env* because this file exists at the root of my project. If your environment file have another name, *replace .env by your env file name*.


* [Back to first section](../README.md)