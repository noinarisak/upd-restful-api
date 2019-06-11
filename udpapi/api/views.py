from flask import Blueprint
from flask_restful import Api

from udpapi.api.resources import UserResource, UserList
from udpapi.api.resources import ConfigResource, ConfigList, ConfigBySubdomainAndAppName
from udpapi.api.resources import NoopResource


blueprint = Blueprint('api', __name__, url_prefix='/api')
api = Api(blueprint)

api.add_resource(NoopResource, '/noop')
api.add_resource(UserResource, '/users/<int:user_id>')
api.add_resource(UserList, '/users')
api.add_resource(ConfigResource, '/configs/<int:config_id>')
api.add_resource(ConfigBySubdomainAndAppName,
                '/configs/<string:subdomain>/<string:app_name>/.well-known/default-setting',
                '/configs/<string:subdomain>/<string:app_name>')
api.add_resource(ConfigList, '/configs')
