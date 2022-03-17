from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField
from wtforms.validators import InputRequired

class TournamentCreateForm(FlaskForm):
    year = StringField('year', validators=[InputRequired()])
    region1 = StringField('region1', validators=[InputRequired()])
    region2 = StringField('region2', validators=[InputRequired()])
    region3 = StringField('region3', validators=[InputRequired()])
    region4 = StringField('region4', validators=[InputRequired()])


class TournamentEditForm(FlaskForm):
    last_round_completed = IntegerField('last_round_completed', validators=[InputRequired()])
