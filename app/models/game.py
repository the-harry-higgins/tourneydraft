from .db import db
from sqlalchemy.sql import func


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    round_num = db.Column(db.Integer, nullable=False)
    game_num = db.Column(db.Integer, nullable=False)
    winning_team_id = db.Column(db.Integer, db.ForeignKey(
        'march_madness_teams.id'), nullable=True)
    child_game_id = db.Column(db.Integer, db.ForeignKey(
        'games.id'), nullable=True)

    teams = db.relationship(
        'March_Madness_Team', secondary='game_team_scores', back_populates='games')
    game_team_scores = db.relationship(
        'Game_Team_Score', back_populates='game')
    winning_team = db.relationship('March_Madness_Team', back_populates='won_games')
    child_game = db.relationship('Game')

    # def to_dict(self):
    #     return {
    #         "id": self.id,
    #         "march_madness_team_id": self.march_madness_team_id,
    #         "league_user_id": self.league_user_id,
    #         "draft_id": self.draft_id,
    #         "selection_num": self.selection_num,
    #     }
