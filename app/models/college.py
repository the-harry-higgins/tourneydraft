from .db import db
from sqlalchemy.sql import func


class College(db.Model):
    __tablename__ = 'colleges'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False, unique=True)
    logo = db.Column(db.String(256), nullable=False)

    march_madness_teams = db.relationship('March_Madness_Team', back_populates='college')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "logo": self.logo,
        }
