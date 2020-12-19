from .db import db


class Tournament(db.Model):
    __tablename__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False)
    region1 = db.Column(db.String(20), nullable=False)
    region2 = db.Column(db.String(20), nullable=False)
    region3 = db.Column(db.String(20), nullable=False)
    region4 = db.Column(db.String(20), nullable=False)
    last_round_completed = db.Column(db.Integer, nullable=False, default=0)

    games = db.relationship('Game', back_populates='tournament')
    march_madness_teams = db.relationship(
        'March_Madness_Team', back_populates='tournament')

    def to_dict(self):
        return {
            "id": self.id,
            "year": self.year,
            "region1": self.region1,
            "region2": self.region2,
            "region3": self.region3,
            "region4": self.region4,
            "last_round_completed": self.last_round_completed,
            "march_madness_teams_ids": [team.id for team in self.march_madness_teams],
            "games_ids": [game.id for game in self.games],
        }
