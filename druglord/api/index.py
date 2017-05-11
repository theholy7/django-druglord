"""
 Simple API endpoint for returning basic project info
"""
from flask import (current_app, jsonify, make_response)
from flask_restful import Resource
from druglord.common import auth


class Index(Resource):

    @auth.login_required
    def get(self):
        data = {'ProjectName': current_app.config['PROJECT'],
                'DEBUG': current_app.config['DEBUG'],
                'message': 'IndexPage'}

        return data, 200
