from .db import db
from sqlalchemy.sql import func


class Drafted_Team(db.Model):
    __tablename__ = 'drafted_teams'

    id = db.Column(db.Integer, primary_key=True)
    march_madness_team_id = db.Column(db.Integer, db.ForeignKey(
        'march_madness_teams.id'), nullable=False)
    league_user_id = db.Column(db.Integer, db.ForeignKey(
        'league_users.id'), nullable=False)
    draft_id = db.Column(db.Integer, db.ForeignKey(
        'drafts.id'), nullable=False)
    selection_num = db.Column(db.Integer, nullable=False)

    __table_args__ = (db.Index("unique_per_draft", "draft_id",
                               "march_madness_team_id", unique=True),)

    march_madness_team = db.relationship('March_Madness_Team')
    league_user = db.relationship('League_User', back_populates='drafted_teams')
    draft = db.relationship('Draft', back_populates='drafted_teams')

    def to_dict(self):
        return {
            "id": self.id,
            "march_madness_team_id": self.march_madness_team_id,
            "league_user_id": self.league_user_id,
            "draft_id": self.draft_id,
            "selection_num": self.selection_num,
        }
