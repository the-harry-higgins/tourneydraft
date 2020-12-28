from .db import db

class League_User(db.Model):
    __tablename__ = 'league_users'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey(
        'leagues.id'), nullable=False)
    
    __table_args__ = (db.Index("unique_user_per_league", "user_id",
                               "league_id", unique=True),)

    user = db.relationship('User', back_populates='league_users')
    league = db.relationship('League', back_populates='league_users')

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "league_id": self.league_id,
            "name": self.user.name,
            "profile_image": self.user.profile_image,
        }
