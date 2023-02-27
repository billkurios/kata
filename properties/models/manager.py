from ...db import db


class Manager(db.Model):
    __tablename__ = 'manager'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)

    def to_json(self):
        """
        Return the JSON serializable format
        """
        return {
            'id': self.id,
            'name': self.name,
        }