import os

from flask import Flask, make_response, jsonify
from flask_restful import Api

from . import config as Config
from .common import constants as COMMON_CONSTANTS
from .api.index import Index

# For import *
__all__ = ['create_app']


# Add all endpoints to app
# format as dicitionary with
# endpoint: endpoint Resource class
# urls: list of endpoint urls
ENDPOINTS = [
    {"endpoint": Index, 'urls': ['/api/v1/']},
]


def create_app(config=None, app_name=None, blueprints=None):
    """Create a Flask app."""

    if app_name is None:
        app_name = Config.DefaultConfig.PROJECT

    app = Flask(app_name,
                instance_path=COMMON_CONSTANTS.INSTANCE_FOLDER_PATH,
                instance_relative_config=True)

    # Currently used configs
    configure_app(app, config)
    configure_api_endpoints(app)
    configure_error_handlers(app)

    # Not in use - maybe future
    # configure_hook(app)
    # configure_extensions(app)
    # configure_logging(app)

    return app


def configure_app(app, config=None):
    """Different ways of configurations."""

    # http://flask.pocoo.org/docs/api/#configuration
    app.config.from_object(Config.DefaultConfig)

    if config:
        app.config.from_object(config)
        return

    # get mode from os environment
    application_mode = os.getenv('APPLICATION_MODE', 'LOCAL')
    app.config.from_object(Config.get_config(application_mode))


def configure_api_endpoints(app):
    api = Api(app)
    for my_endpoint in ENDPOINTS:
        api.add_resource(my_endpoint['endpoint'],
                         *my_endpoint['urls'])


def configure_error_handlers(app):
    # example
    @app.errorhandler(500)
    def server_error_page(error):
        return make_response(jsonify({'error': 'Error'}), 500)

    @app.errorhandler(404)
    def not_found(error):
        return make_response(jsonify({'error': 'Not found'}), 404)


# def configure_extensions(app):
#     pass
#
# def configure_hook(app):
#     @app.before_request
#     def before_request():
#         pass
#
# def configure_logging(app):
#     pass
