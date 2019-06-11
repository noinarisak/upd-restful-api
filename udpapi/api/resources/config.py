from flask import request, make_response
from flask_restful import Resource
# from flask_jwt_extended import jwt_required

from udpapi.models import Config
from udpapi.extensions import ma, db
from udpapi.commons.pagination import paginate


class ConfigSchema(ma.ModelSchema):

    class Meta:
        model = Config
        sqla_session = db.session


class ConfigResource(Resource):
    """Single object resource
    """
    # method_decorators = [jwt_required]

    def get(self, config_id):
        schema = ConfigSchema()
        print('config_id:' + str(config_id))
        config = Config.query.get_or_404(config_id)
        return {"config": schema.dump(config).data}, 200, {'Access-Control-Allow-Origin': '*'}

    def put(self, config_id):
        schema = ConfigSchema(partial=True)
        print('config_id:' + str(config_id))
        config = Config.query.get_or_404(config_id)
        config, errors = schema.load(request.json, instance=config)
        if errors:
            return errors, 422

        return {"msg": "config updated", "config": schema.dump(config).data}, 200, {'Access-Control-Allow-Origin': '*'}

    def delete(self, config_id):
        config = Config.query.get_or_404(config_id)
        db.session.delete(config)
        db.session.commit()

        return {"msg": "config deleted"}


class ConfigBySubdomainAndAppName(Resource):
    """Single object resource
    """
    # method_decorators = [jwt_required]

    def get(self, subdomain, app_name):
        schema = ConfigSchema()
        # print('udp_subdomain' + udp_subdomain)
        # print('demo_app_name' + demo_app_name)
        config = Config.query.filter_by(udp_subdomain=subdomain, demo_app_name=app_name).first_or_404()
        return {"config": schema.dump(config).data}, 200, {'Access-Control-Allow-Origin': '*'}

    def put(self, subdomain, app_name):
        schema = ConfigSchema(partial=True)
        # print('udp_subdomain' + subdomain)
        # print('demo_app_name' + app_name)
        config = Config.query.filter_by(udp_subdomain=subdomain, demo_app_name=app_name).first_or_404()
        config, errors = schema.load(request.json, instance=config)
        if errors:
            return errors, 422

        db.session.commit()

        return {"msg": "config updated", "config": schema.dump(config).data}, 200, {'Access-Control-Allow-Origin': '*'}


class ConfigSecret(Resource):
    """Single object resource
    """
    # method_decorators = [jwt_required]

    def get(self, subdomain, app_name):
        # print('udp_subdomain' + udp_subdomain)
        # print('demo_app_name' + demo_app_name)
        config = Config.query.filter_by(udp_subdomain=subdomain, demo_app_name=app_name).first_or_404()

        # Over write flask_restful default "{Content-Type: application/json}" HTTP response to "text/dotenv"
        output = "# WARNING: These values are HIGHLY SENSITIVE and MUST only be used by server side APIs!\n"
        output += "OKTA_API_TOKEN={token}".format(token=config.okta_api_token)
        response = make_response(output)
        response.headers['Content-Type'] = 'text/dotenv'
        return response


class ConfigList(Resource):
    """Creation and get_all
    """
    # method_decorators = [jwt_required]

    def get(self):
        schema = ConfigSchema(many=True)
        query = Config.query
        return paginate(query, schema), 200, {'Access-Control-Allow-Origin': '*'}

    def post(self):
        schema = ConfigSchema()
        config, errors = schema.load(request.json)
        if errors:
            return errors, 422

        config_exist = Config.query.filter_by(udp_subdomain=config.udp_subdomain, demo_app_name=config.demo_app_name).first()
        if config_exist is not None:
            return {"msg": "config already exist"}, 409

        db.session.add(config)
        db.session.commit()

        return {"msg": "config created", "config": schema.dump(config).data}, 201, {'Access-Control-Allow-Origin': '*'}
