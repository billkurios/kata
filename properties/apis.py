from flask import jsonify, abort, request

from .models.property import Property, PropertySchema
from .models.manager import Manager
from .common import blueprint as bp


properties_schema = PropertySchema(many=True)

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
    
    # properties = Property.get_objects(Property)
    # return jsonify([property.to_json() for property in properties])
    properties = Property.query.filter_by(Property).all()
    return jsonify(properties_schema.dump(properties))