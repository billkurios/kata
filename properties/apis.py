from flask import jsonify, abort, request

from .models.property import Property, PropertySchema
from .models.manager import Manager, ManagerSchema
from .common import blueprint as bp


properties_schema = PropertySchema(many=True)
managers_schema = ManagerSchema(many=True)


@bp.route('/managers')
def managers():
    managers = Manager.query.all()
    return jsonify(properties_schema.dump(managers))


@bp.route('/manager/properties')
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
    
    properties = Property.query.filter_by(manager_id=manager_id).all()
    return jsonify(properties_schema.dump(properties))