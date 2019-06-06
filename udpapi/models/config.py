from sqlalchemy.dialects.postgresql import JSON

from udpapi.extensions import db, pwd_context


class Config(db.Model):
    """Basic Config model
    """
    id = db.Column(db.Integer, primary_key=True)
    udp_subdomain = db.Column(db.String(80), nullable=False)
    # demo_app_name = db.Column(db.String(255), nullable=False)
    # okta_api_key = db.Column(db.String(255), nullable=False)
    # okta_org_name = db.Column(db.String(255), nullable=False)
    context = db.Column(JSON)

    def __init__(self, **kwargs):
        super(Config, self).__init__(**kwargs)

    def __repr__(self):
        return "<Config %s>" % self.udp_subdomain