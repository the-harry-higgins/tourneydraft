import os

class Config:
  SECRET_KEY=os.environ.get('SECRET_KEY')
  SQLALCHEMY_TRACK_MODIFICATIONS=False
  SQLALCHEMY_DATABASE_URI=os.environ.get('DATABASE_URL')
  SQLALCHEMY_ECHO=True

  MAIL_SERVER='smtp.gmail.com'
  MAIL_PORT=465
  MAIL_USE_SSL=True
  MAIL_USERNAME='harryrhiggins@gmail.com'
  MAIL_PASSWORD=os.environ.get('MAIL_PASSWORD')