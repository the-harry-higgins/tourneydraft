from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, Tournament, March_Madness_Team, College
from .auth_routes import get_user_data
import json

admin_routes = Blueprint('admin', __name__)


@admin_routes.route('/')
def test():
    return "You did it"


@admin_routes.route('/', methods=['POST'])
def update_game_score():
    req_data = json.loads(request.data)

    year = req_data['year']

    tournament = Tournament.query.filter(Tournament.year == year).one()

    print(tournament)

    team1_name = req_data['team1Name']
    team1_score = req_data['team1Score']

    college1 = College.query.filter(College.name == team1_name).one()

    print(college1.to_dict())

    team1 = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id
    ).filter(
        March_Madness_Team.college_id == college1.id
    ).one()

    team1dict = team1.to_dict()

    print(team1dict)
    print(team1dict['games_by_round'][1])
    return team1
