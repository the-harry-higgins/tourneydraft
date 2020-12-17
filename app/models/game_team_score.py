from .db import db

class Game_Team_Score(db.Model):
    __tablename__ = 'game_team_scores'

    id = db.Column(db.Integer, primary_key=True)
    game_id = db.Column(db.Integer, db.ForeignKey(
        'games.id'), nullable=False)
    team_id = db.Column(db.Integer, db.ForeignKey(
        'march_madness_teams.id'), nullable=False)
    score = db.Column(db.Integer, nullable=True, default=None)

    team = db.relationship('March_Madness_Team')
    game = db.relationship('Game', back_populates='game_team_scores')
