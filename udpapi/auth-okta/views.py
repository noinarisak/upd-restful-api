from flask import request, jsonify, Blueprint, current_app as app

from udpapi.models import User
from udpapi.extensions import pwd_context, jwt
from udpapi.auth.helpers import OktaUtil

blueprint = Blueprint('auth-okta', __name__, url_prefix='/auth-okta')


@blueprint.route('/login', methods=['POST'])
def login():
    """Authenticate user and return token
    """
    if not request.is_json:
        return jsonify({"msg": "Missing JSON in request"}), 400

    username = request.json.get('username', None)
    password = request.json.get('password', None)
    if not username or not password:
        return jsonify({"msg": "Missing username or password"}), 400

    # user = User.query.filter_by(username=username).first()
    # if user is None or not pwd_context.verify(password, user.password):
    #     return jsonify({"msg": "Bad credentials"}), 400

    # access_token = create_access_token(identity=user.id)
    # refresh_token = create_refresh_token(identity=user.id)
    # add_token_to_database(access_token, app.config['JWT_IDENTITY_CLAIM'])
    # add_token_to_database(refresh_token, app.config['JWT_IDENTITY_CLAIM'])

    ret = {
        'access_token': access_token,
        'refresh_token': refresh_token
    }
    return jsonify(ret), 200
