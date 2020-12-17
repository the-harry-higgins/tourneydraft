from .db import db

class League_User(db.Model):
    __tablename__ = 'league_users'

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    league_id = db.Column(db.Integer, db.ForeignKey(
        'leagues.id'), nullable=False)

    user = db.relationship('User', back_populates='league_users')
    league = db.relationship('League', back_populates='league_users')
    # drafted_teams = db.relationship('Drafted_Team', back_populates='league_user')

    def to_dict(self):
        return {
            "id": self.id,
            "user_id": self.user_id,
            "league_id": self.league_id,
            # "drafted_teams": [drafted_team.id for drafted_team in self.drafted_teams],
            "name": self.user.name,
            "profile_image": self.user.profile_image,
        }
