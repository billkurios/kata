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