from .db import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from time import time
import os
import jwt

class User(db.Model, UserMixin):
    __tablename__ = 'users'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(40), nullable=False)
    email = db.Column(db.String(255), nullable=False, unique=True)
    hashed_password = db.Column(db.String(255), nullable=False)
    profile_image = db.Column(db.String(255), nullable=True, default=None)
    is_admin = db.Column(db.Boolean, nullable=False, default=False)

    leagues = db.relationship('League', secondary='league_users')
    league_users = db.relationship('League_User', back_populates='user')

    @property
    def password(self):
        return self.hashed_password

    @password.setter
    def password(self, password):
        self.hashed_password = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password, password)

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "profile_image": self.profile_image,
            "league_user_ids": [league_user.id for league_user in self.league_users],
            "league_ids": [league.id for league in self.leagues],
            "is_admin": self.is_admin,
        }

    def get_reset_token(self, expires=500):
        return jwt.encode({'reset_password': self.email,
                           'exp':    time() + expires},
                           key=os.getenv('SECRET_KEY')).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        try:
            email = jwt.decode(token, key=os.getenv('SECRET_KEY'), algorithms=['HS256'])['reset_password']
            print(email)
        except Exception as e:
            print(e)
            return
        return User.query.filter_by(email=email).first()
