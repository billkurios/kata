import os
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

    from .models import db, Manager, Property
    db.init_app(app)

    from flask_alembic import Alembic
    alembic = Alembic()
    alembic.init_app(app)


    @app.route('/')
    def index():
        abort(404, "Invalid url")

    @app.route('/manager/properties')
    def manager_properties():
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
        
        properties = Property.query.filter_by(manager_id=manager_id)
        return jsonify([property.to_json() for property in properties])

    return app