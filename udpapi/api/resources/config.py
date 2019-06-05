from flask import request
from flask_restful import Resource
from flask_jwt_extended import jwt_required

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
    method_decorators = [jwt_required]

    def get(self, config_id):
        schema = ConfigSchema()
        config = Config.query.get_or_404(config_id)
        return {"config": schema.dump(config).data}

    def put(self, config_id):
        schema = UserSchema(partial=True)
        config = Config.query.get_or_404(config_id)
        config, errors = schema.load(request.json, instance=config)
        if errors:
            return errors, 422

        return {"msg": "config updated", "config": schema.dump(config).data}

    def delete(self, config_id):
        config = Config.query.get_or_404(config_id)
        db.session.delete(config)
        db.session.commit()

        return {"msg": "config deleted"}


class ConfigList(Resource):
    """Creation and get_all
    """
    method_decorators = [jwt_required]

    def get(self):
        schema = ConfigSchema(many=True)
        query = Config.query
        return paginate(query, schema)

    def post(self):
        schema = ConfigSchema()
        config, errors = schema.load(request.json)
        if errors:
            return errors, 422

        db.session.add(config)
        db.session.commit()

        return {"msg": "config created", "config": schema.dump(config).data}, 201
