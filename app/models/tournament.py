from .db import db


class Tournament(db.Model):
    __tablename__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    region1 = db.Column(db.String(20), nullable=False)
    region2 = db.Column(db.String(20), nullable=False)
    region3 = db.Column(db.String(20), nullable=False)
    region4 = db.Column(db.String(20), nullable=False)

    march_madness_teams = db.relationship(
        'March_Madness_Team', back_populates='tournament')

    def to_dict(self):
        return {
            "id": self.id,
            "year": self.year,
            "region1": self.region1,
            "region1": self.region1,
            "region1": self.region1,
            "region1": self.region1,
            "march_madness_teams_ids": [team.id for team in self.march_madness_teams],
        }
