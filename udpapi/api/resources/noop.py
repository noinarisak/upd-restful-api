from flask_restful import Resource


class NoopResource(Resource):
    """Single object resource
    """

    def get(self):
        noop = {
            "msg": "hello there"
        }
        return {"noop": noop}
