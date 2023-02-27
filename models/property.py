from ..init import db


class Property(db.Model):
    __tablename__ = 'property'

    id = db.Column(db.Integer, primary_key=True)
    type = db.Column(db.String(100), nullable=False)
    location = db.Column(db.String(100), nullable=False)
    number_bedrooms = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Integer, nullable=False)
    manager_id = db.Column(db.Integer, db.ForeignKey('manager.id'))