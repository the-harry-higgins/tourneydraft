from .db import db

class March_Madness_Team(db.Model):
    __tablename__ = 'march_madness_teams'

    id = db.Column(db.Integer, primary_key=True)
    tournament_id = db.Column(
        db.Integer, db.ForeignKey('tournaments.id'), nullable=False)
    seed_number = db.Column(db.Integer,  nullable=False)
    region = db.Column(db.String(50), nullable=False)
    # Nullable because of those dumb fake first round games
    college_id = db.Column(db.Integer, db.ForeignKey('colleges.id'), nullable=True)

    tournament = db.relationship(
        'Tournament', back_populates='march_madness_teams')
    college = db.relationship('College', back_populates='march_madness_teams')
    won_games = db.relationship('Game', back_populates='winning_team')
    # game_scores = db.relationship('Game_Team_Score', back_populates='team')
    games = db.relationship(
        'Game', secondary='game_team_scores', back_populates='teams')


    def calculate_points(self, round):
        won_rounds = [game.round_num for game in self.won_games]
        return sum([round + self.seed for round in range(1,round) if round in won_rounds])

    def to_dict(self, round=1):
        return {
            "id": self.id,
            "seed_number": self.seed_number,
            "region": self.region,
            "name": self.college.name,
            "logo": self.college.logo,
            "games_by_round": {game.round_num: game.id for game in self.games},
            "won_game_ids": [game.id for game in self.won_games],
            "points": self.calculate_points(round)
        }
