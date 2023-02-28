import os
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from apispec_webframeworks.flask import FlaskPlugin



spec = APISpec(
    title="Properties Portfolio APIs Docs",
    version=os.environ.get('VERSION', '0.0.1'),
    openapi_version="3.0.0",
    info={
        'contact': {
            'url': 'https://github.com/billkurios'
        },
        'license': {
            'name': 'MIT',
            'url': 'https://opensource.org/license/mit/',
        }
    },
    servers=[
        {
            'description': 'Test Server (Local)',
            'url': f"http://{os.environ.get('FLASK_HOST', 'localhost')}:{os.environ.get('FLASK_PORT', '3000')}"
        }
    ],
    tags=[
        {'name': 'Properties', 'description': 'Endpoints related to properties portfolio'},
    ],
    plugins=[FlaskPlugin(), MarshmallowPlugin()]
)