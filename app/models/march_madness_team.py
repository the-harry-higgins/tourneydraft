from .db import db
from sqlalchemy.sql import func
import json


class March_Madness_Team(db.Model):
    __tablename__ = 'march_madness_teams'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer,  nullable=False)
    seed_number = db.Column(db.Integer,  nullable=False)
    region = db.Column(db.String(50), nullable=False)
    eliminated = db.Column(db.Boolean, nullable=False, default=False)
    # Nullable because of those dumb fake first round games
    college_id = db.Column(db.Integer, db.ForeignKey('colleges.id'), nullable=True)

    college = db.relationship('College', back_populates='march_madness_teams')
    won_games = db.relationship('Game', back_populates='winning_team')
    # game_scores = db.relationship('Game_Team_Score', back_populates='team')
    games = db.relationship(
        'Game', secondary='game_team_scores', back_populates='teams')


    def to_dict(self):
        return {
            "id": self.id,
            "year": self.year,
            "seed_number": self.seed_number,
            "region": self.region,
            "eliminated": self.eliminated,
            "college_id": self.college_id,
            "name": self.college.name,
            "logo": self.college.logo,
            "games_by_round": {game.round_num: game.id for game in self.games},
            "won_game_ids": [game.id for game in self.won_games],
            "points": 0
        }
