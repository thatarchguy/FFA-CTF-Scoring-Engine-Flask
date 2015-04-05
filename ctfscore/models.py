from ctfscore import db


class Flags(db.Model):
    """
    Database models for flags

    >>> from ctfscore import app,db,models
    >>> flag = models.Flags(flag="flag-ABD12FE", points="20")
    >>> db.session.add(flag)
    >>> db.session.commit()
    """
    id          = db.Column(db.Integer, primary_key=True)
    flag        = db.Column(db.String(20))
    points       = db.Column(db.Integer)


class Completed(db.Model):
    id           = db.Column(db.Integer, primary_key=True)
    user         = db.Column(db.String(255))
    flag_id      = db.Column(db.Integer)
