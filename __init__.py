import os
import json
from flask import Flask, abort, jsonify, url_for, request
from sqlalchemy.orm import exc



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

    from .properties import properties_bp, manager_properties
    from .data import bp as tests_bp
    app.register_blueprint(properties_bp)
    app.register_blueprint(tests_bp)


    from .db import db, alembic, ma
    db.init_app(app)
    ma.init_app(app)
    alembic.init_app(app) #ORM

    from .apispec import spec
    with app.test_request_context():
        spec.path(view=manager_properties)
    # Save our swagger file
    with open('docs/swagger.json', 'w') as f:
        json.dump(spec.to_dict(), f, indent=2)
    
    return app