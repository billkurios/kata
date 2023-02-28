from ...db import db, ma


class Manager(db.Model):
    __tablename__ = 'manager'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)


class ManagerSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Manager