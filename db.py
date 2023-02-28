from flask_sqlalchemy import SQLAlchemy
from flask_alembic import Alembic
from flask_marshmallow import Marshmallow


alembic = Alembic()

db = SQLAlchemy()

ma = Marshmallow()