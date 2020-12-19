from .db import db

class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer, primary_key=True)
    round_num = db.Column(db.Integer, nullable=False)
    game_num = db.Column(db.Integer, nullable=False)
    winning_team_id = db.Column(db.Integer, db.ForeignKey(
        'march_madness_teams.id'), nullable=True)
    child_game_id = db.Column(db.Integer, db.ForeignKey(
        'games.id'), nullable=True)
    tournament_id = db.Column(db.Integer, db.ForeignKey(
        'tournaments.id'), nullable=False)

    teams = db.relationship(
        'March_Madness_Team', secondary='game_team_scores', back_populates='games')
    game_team_scores = db.relationship(
        'Game_Team_Score', back_populates='game')
    winning_team = db.relationship('March_Madness_Team', back_populates='won_games')
    child_game = db.relationship('Game')
    tournament = db.relationship('Tournament', back_populates='games')

    def to_dict(self):
        return {
            "id": self.id,
            "tournament_id": self.tournament_id,
            "round_num": self.round_num,
            "game_num": self.game_num,
            "winning_team_id": self.winning_team_id,
            "team_ids": [team.id for team in self.teams],
        }
