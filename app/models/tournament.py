from app.models.draft import Draft
from app.models.drafted_team import Drafted_Team
from app.models.game import Game
from app.models.db import db
from app.models.game_team_score import Game_Team_Score
from app.models.march_madness_team import March_Madness_Team
from app.utils import get_round_num


class Tournament(db.Model):
    __tablename__ = 'tournaments'

    id = db.Column(db.Integer, primary_key=True)
    year = db.Column(db.Integer, nullable=False, unique=True)
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

    def update(self, last_round_completed):
        self.last_round_completed = last_round_completed
        db.session.commit()
        return self

    def delete(self):
        delete_game_team_scores = Game_Team_Score.__table__.delete().where(Game_Team_Score.game.has(tournament_id=self.id))
        db.session.execute(delete_game_team_scores)
        delete_games = Game.__table__.delete().where(Game.tournament_id == self.id)
        db.session.execute(delete_games)
        delete_drafted_teams = Drafted_Team.__table__.delete().where(Drafted_Team.march_madness_team.has(tournament_id=self.id))
        db.session.execute(delete_drafted_teams)
        delete_drafts = Draft.__table__.delete().where(Draft.tournament_id == self.id)
        db.session.execute(delete_drafts)
        delete_march_madness_teams = March_Madness_Team.__table__.delete().where(March_Madness_Team.tournament_id == self.id)
        db.session.execute(delete_march_madness_teams)
        db.session.delete(self)
        db.session.commit()
        return

    @staticmethod
    def list():
        return { 'tournaments': {t.id: t.to_dict() for t in Tournament.query.all()} }

    @staticmethod
    def create(year, region1, region2, region3, region4):
        tournament = Tournament(year=year, region1=region1, region2=region2, region3=region3, region4=region4)
        db.session.add(tournament)
        db.session.commit()

        for i in range(1,64):
            round_num = get_round_num(i)
            game = Game(game_num=i, round_num=round_num, winning_team_id=None, tournament_id=tournament.id)
            db.session.add(game)
            db.session.commit()
        return tournament
