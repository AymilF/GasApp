from app import db


class Result(db.Model):
    """
    A model for the results table in the database.
    """
    id = db.Column(db.Text, primary_key=True)
    queued = db.Column(db.DateTime)
    started = db.Column(db.DateTime)
    completed = db.Column(db.DateTime)
    result = db.Column(db.Text)

    def __repr__(self):
        return "<Result %r>" % self.result
