from ..init import db


class Manager(db.Model):
    __tablename__ = 'manager'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)