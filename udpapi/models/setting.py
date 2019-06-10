from udpapi.extensions import db, pwd_context


class Setting(db.Model):
    """Basic Setting model
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255))
    value = db.Column(db.String(255))

    def __init__(self, **kwargs):
        super(Setting, self).__init__(**kwargs)

    def __repr__(self):
        return "<Setting %s>" % self.name