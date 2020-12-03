from .db import db
from sqlalchemy.sql import func
import json


class Draft(db.Model):
    __tablename__ = 'drafts'

    id = db.Column(db.Integer, primary_key=True)
    league_id = db.Column(db.Integer, db.ForeignKey('leagues.id'), nullable=False)
    year = db.Column(db.Integer,  nullable=False)
    draft_order = db.Column(db.String(512), nullable=True)
    draft_index = db.Column(db.Integer,  nullable=False)
    draft_time = db.Column(db.DateTime(timezone=True), nullable=False)
    drafting = db.Column(db.Boolean, nullable=False)
    current_drafter_id = db.Column(db.Integer, db.ForeignKey('league_users.id'), nullable=True)
    time_limit_mins = db.Column(db.Integer,  nullable=True)

    __table_args__ = (db.Index("unique_draft_per_league_year", "league_id", "year", unique=True),)

    league = db.relationship('League', back_populates='drafts')
    current_drafter = db.relationship('League_User')
    drafted_teams = db.relationship('Drafted_Team', back_populates='draft')

    def to_dict(self):
        return {
            "id": self.id,
            "league_id": self.league_id,
            "year": self.year,
            "draft_order": json.loads(self.draft_order),
            "draft_index": self.draft_index,
            "draft_time": self.draft_time,
            "drafting": self.drafting,
            "current_drafter_id": self.current_drafter_id,
            "time_limit_mins": self.time_limit_mins,
            "drafted_team_ids": [drafted_team.id for drafted_team in self.drafted_teams]
        }
