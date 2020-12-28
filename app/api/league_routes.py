from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user
from app.models import db, League, League_User
from .auth_routes import get_user_data
import json

league_routes = Blueprint('leagues', __name__)


@league_routes.route('/')
@login_required
def get_joinable_leagues():
    print('\n\n\nLEAGUES:')
    print(current_user.leagues)
    league_ids = [league.id for league in current_user.leagues]
    joinable_leagues = League.query.filter(League.id.notin_(league_ids)).all()
    return {"leagues": [league.to_dict() for league in joinable_leagues
                        if len(league.league_users) < 8]}


@ league_routes.route('/join/', methods=['POST'])
@ login_required
def join_league():
    req_data = json.loads(request.data)
    name = req_data['name']
    league = League.query.filter(League.name == name).one()
    league_user = League_User(user_id=current_user.id, league_id=league.id)
    db.session.add(league_user)
    db.session.commit()
    data = get_user_data(current_user, league=league,
                         league_user_id=league_user.id)
    return data


@ league_routes.route('/', methods=['POST'])
@ login_required
def create_league():
    try:
        req_data = json.loads(request.data)
        name = req_data['name']
        league = League(name=name, admin_id=current_user.id)
        db.session.add(league)
        db.session.commit()
        league_user = League_User(user_id=current_user.id, league_id=league.id)
        db.session.add(league_user)
        db.session.commit()
        data = get_user_data(current_user, league=league,
                             league_user_id=league_user.id)
        print(data)
        return data
    except Exception as err:
        print(err)
        return {'errors': ['That league name is already in use.']}, 400
