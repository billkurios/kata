from flask_restx import Namespace, fields


namespace = Namespace('properties', 'Properties portfolio related endpoints')

property_model = namespace.model("Property", {
    'identity': fields.String(
        readonly=True,
        description='Property Id',
        attribute='id'
    ),
    'type': fields.String(
        description="Property Type (For ex: T1, T2, ...)."
    ),
    'location': fields.String(
        description="The place where the property is."
    ),
    'number_bedrooms': fields.String(
        description="The number of bedrooms in the property."
    ),
    'price': fields.String(
        description="The cost of the property."
    ),
})