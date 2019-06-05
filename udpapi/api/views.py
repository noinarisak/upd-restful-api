from flask import Blueprint
from flask_restful import Api

from udpapi.api.resources import UserResource, UserList
from udpapi.api.resources import ConfigResource, ConfigList


blueprint = Blueprint('api', __name__, url_prefix='/api/v1')
api = Api(blueprint)


api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(ConfigResource, '/configs/<int:config_id>')
api.add_resource(ConfigList, '/configs')