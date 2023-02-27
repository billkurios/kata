from flask_restx import Resource

from .utils import namespace, property_model
from models import Property


@namespace.route('/properties/<manager_id>')
@namespace.doc(
    params={'manager_id': 'Properties manager #ID'}
)
class PropertyAPI(Resource):

    @namespace.marshal_list_with(property_model)
    @namespace.response(500, 'Internal Server error')
    @namespace.doc(
        body=[property_model]
    )
    def get(self):
        '''List properties'''
        return Property.query.all()