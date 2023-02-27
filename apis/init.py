from flask import Blueprint
from flask_restx import Api

from .properties.utils import namespace as property_ns


blueprint = Blueprint('api', __name__, url_prefix='/api')

api_extension = Api(
    blueprint,
    title='Properties Portfolio APIs',
    version='0.0.1',
    description="Web application developed by a real estate company that specializes in property management. And we have an auto generated apis documentation.",
    doc="/docs"
)

api_extension.add_namespace(property_ns)