from sqlalchemy.dialects.postgresql import JSON

from udpapi.extensions import db


class Config(db.Model):
    """Basic Config model
    """
    # id = db.Column(db.Integer, unique=True, primary_key=True)
    user_id = db.Column(db.String(80), nullable=False)
    udp_subdomain = db.Column(db.String(80), primary_key=True)
    demo_app_name = db.Column(db.String(255), primary_key=True)
    okta_api_token = db.Column(db.String(255), nullable=False)
    base_url = db.Column(db.String(255), nullable=False)
    client_id = db.Column(db.String(255), nullable=False)
    client_secret = db.Column(db.String(255), nullable=False)
    issuer = db.Column(db.String(255), nullable=False)
    redirect_uri = db.Column(db.String(255), nullable=False)
    status = db.Column(db.String(80))
    settings = db.Column(JSON)

    def __init__(self, **kwargs):
        super(Config, self).__init__(**kwargs)

    def __repr__(self):
        return "<Config %s>" % ("{subdomain}:{app_name}".format(
                                                                subdomain=self.udp_subdomain,
                                                                app_name=self.demo_app_name))
