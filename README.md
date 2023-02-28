# [kata](https://github.com/billkurios/kata)
Lab on Flask

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

FLASK_PORT=3000
FLASK_HOST=127.0.0.1
VERSION='0.0.1'

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

```sh
flask db upgrade
```

### Run Our flask application

```sh
flask --env-file=.env run --host=127.0.0.1 --port=3000
```
Here I pass *.env* because this file exists at the root of my project. If your environment file have another name, *replace .env by your env file name*.

Now It's good your project is up and available at *http://127.0.0.1:3000*

### Load some data [Optional]

```
flask tests load_data
```

## Context
"Properties Portfolio" is a web application developed by a real estate company that specializes
in property management. The application offers insights to around 1,000 investors on the
properties managed by the company's property managers. The application's frontend is built
using a SPA in Angular, while the backend is developed using Flask with Gunicorn and Python
3.9. The backend runs as a Docker image within a service in ECS (Fargate) behind an application
load balancer that is served by AWS API Gateway. The backend uses SQLAlchemy as an ORM
for CRUD operations and Pandas as an ETL (mainly to feed the database daily with properties
data). The database is deployed on a PostgreSQL 14 engine on AWS RDS.

## Use Case
The real estate company wants to improve the user experience of their web application by
adding new features which would impact existing API, models, database etc...

## Answers of Questions

#### Question 1
[Flask API endpoint who retrieved the list of properties managed by a specific property manager](https://github.com/billkurios/kata/blob/master/properties/apis.py)

Here it's the content file.

```py
from flask import jsonify, abort, request

from .models.property import Property, PropertySchema
from .models.manager import Manager, ManagerSchema
from .common import blueprint as bp
from ..apispec import spec


properties_schema = PropertySchema(many=True)
managers_schema = ManagerSchema(many=True)


@bp.route('/manager/properties', methods=["GET"])
def manager_properties():
    """Manager's properties endpoint.
    ---
    get:
      description: Get a list of properties linked to the given manager.
      responses:
        400:
          description: Manager Identifier #manager_id is required
        404:
          description: manager_id don't exist
        200:
          description: Should return a list
          content:
            application/json:
              schema: PropertySchema
    """
    manager_id = request.args.get('manager_id')

    if manager_id is None:
        abort(400, "manager_id is required.")
    
    try:
        manager_id = int(manager_id)
    except ValueError:
        abort(404, f"Bad value. {manager_id} should be an integer")

    manager = Manager.query.filter_by(id=manager_id).first()
    if manager is None:
        abort(404, f"Manager #Id {manager_id} doesn't exist.")
    
    properties = Property.query.filter_by(manager_id=manager_id).all()
    return jsonify(properties_schema.dump(properties))
```

#### Question 2
Swagger definition of the Flask API endpoint implement in Question 1.
In the project, the auto generated file is [here](https://github.com/billkurios/kata/blob/master/docs/swagger.json).
Below it's the swagger content file in yaml format.

```yaml
info:
  contact:
    url: https://github.com/billkurios
  license:
    name: MIT
    url: https://opensource.org/license/mit/
  title: Properties Portfolio APIs Docs
  version: 0.0.1
servers:
  - description: Test Server (Local)
    url: http://127.0.0.1:3000
tags:
  - name: Properties
    description: Endpoints related to properties portfolio
paths:
  /api/manager/properties:
    get:
      description: Get a list of properties linked to the given manager.
      responses:
        '200':
          description: Should return a list
          content:
            application/json:
              schema:
                $ref: '#/components/schemas/Property'
        '400':
          description: Manager Identifier
        '404':
          description: manager_id don't exist
openapi: 3.0.0
components:
  schemas:
    Property:
      type: object
      properties:
        type:
          type: string
          maxLength: 100
        location:
          type: string
          maxLength: 100
        number_bedrooms:
          type: integer
        price:
          type: integer
        id:
          type: integer
      required:
        - location
        - number_bedrooms
        - price
        - type
```

#### Question 3
We prevent SQL injection attacks by serialize user input data and by validate each field of
our new serialize object.
I would use a schema validation with Marshmallow library.
```py
from marshmallow import ValidationError

try
    user_input = PropertySchema().load(request.form)
except ValidationError as err:
    # .....
```

#### Question 4
For authentication, an SSO service can managed it. And for authorization on our web application, we can use the framework OAuth2 with the SSO service.

#### Question 5
We can define rate limiting for API endpoints at the web server configuration file. It's a good pratice, because if not defined, our web server would shut down. It's Denied Of Service if the web server get more connections than he can managed.

#### Question 7
I have create a command group *tests* and a command *load_data* to load my csv files data.
So the full command is *flask tests load_data*

[link to file in the project](https://github.com/billkurios/kata/blob/master/data/__init__.py).

```py
import click
import pandas as pd
from flask import Blueprint

from ..properties.models.manager import Manager
from ..properties.models.property import Property
from ..db import db


bp = Blueprint('tests', __name__, cli_group='tests')


def genManagers(managersDF):
    """Generateur d'objets Manager à partir du dataframe
    issu de la lecture du fichier csv"""
    for value in managersDF.values:
        managerArgs = {}
        for i in range(len(value)):
            managerArgs[managersDF.columns[i]] = value[i]
        yield Manager(**managerArgs)

def genProperties(propertiesDF):
    """Generateur d'objets Property à partir du dataframe
    issu de la lecture du fichier csv"""
    for value in propertiesDF.values:
        propertyArgs = {}
        for i in range(len(value)):
            propertyArgs[propertiesDF.columns[i]] = value[i]
        yield Property(**propertyArgs)


@bp.cli.command('load_data')
def load_data():
    """Load basic data in csv files in the database with pandas library."""
    click.echo("Step 1: Import managers data")
    managerObjects = genManagers(pd.read_csv(r'./data/managers.csv'))
    for manager in managerObjects:
        db.session.add(manager)
    click.echo("Step 1 doned !!!")
    click.echo("Step 2: Import properties data")
    propertyObjects = genProperties(pd.read_csv(r'./data/properties.csv'))
    for property in propertyObjects:
        db.session.add(property)
    db.session.commit()
    click.echo("Step 2 doned !!!")
```

