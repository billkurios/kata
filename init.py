import os

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from .apis.init import blueprint as documented_endpoint


db = SQLAlchemy()

def create_app(test_config=None):
    app = Flask(__name__)
    app.config.from_mapping(
        SECRET_KEY=os.environ.get('SECRET_KEY', default='dev_poc'),
    )

    if test_config is None:
        # Load configuration from config.py
        app.config.from_pyfile('config.py', silent=True)
    else:
        app.config.from_mapping(test_config)
    
    app.register_blueprint(documented_endpoint)

    db.init_app(app)

    return app