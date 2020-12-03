from .db import db
from sqlalchemy.sql import func


class League(db.Model):
    __tablename__ = 'leagues'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    admin_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    admin = db.relationship('User')
    drafts = db.relationship('Draft', back_populates='league')
    league_users = db.relationship('League_User', back_populates='league')

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "admin_id": self.admin_id,
            "draft_ids": [draft.id for draft in self.drafts]
            "league_user_ids": [league_user.id for league_user in self.league_users]
        }
