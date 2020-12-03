from .db import db
from sqlalchemy.sql import func


class Game_Team_Score(db.Model):
    __tablename__ = 'game_team_scores'

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey(
        'games.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey(
        'march_madness_teams.id'), nullable=False)
    score = db.Column(db.Integer, nullable=False)

    team = db.relationship('March_Madness_Team')
    game = db.relationship('Game', back_populates='game_team_scores')

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "march_madness_team_id": self.march_madness_team_id,
    #         "league_user_id": self.league_user_id,
    #         "draft_id": self.draft_id,
    #         "selection_num": self.selection_num,
    #     }
