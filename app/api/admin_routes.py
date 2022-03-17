import json

from flask import Blueprint, jsonify, request
from flask_login import login_required, current_user

from app.api.utils import validation_errors_to_error_messages
from app.forms import TournamentCreateForm, TournamentEditForm
from app.models import db, Tournament, March_Madness_Team, College
from app.models.game import Game
from app.models.game_team_score import Game_Team_Score
from app.utils import get_next_game_num


admin_routes = Blueprint('admin', __name__)


@admin_routes.route('/tournament',  methods=['GET', 'POST'])
def tournaments():
    if request.method == 'GET':
        return Tournament.list()
    elif request.method == 'POST':
        form = TournamentCreateForm()
        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            d = {**form.data}
            d.pop('csrf_token')
            try:
                tournament = Tournament.create(**d)
                return {'tournament': tournament.to_dict()}, 201
            except Exception as e:
                return {'errors': [str(e.orig)]}, 500
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@admin_routes.route('/tournament/<int:id>',  methods=['GET', 'PUT', 'DELETE'])
def tournament(id):
    if request.method == 'GET':
        tournament = Tournament.query.get(id)
        return {'tournament': tournament.to_dict()}, 200
    elif request.method == 'PUT':
        form = TournamentEditForm()
        form['csrf_token'].data = request.cookies['csrf_token']
        if form.validate_on_submit():
            tournament = Tournament.query.get(id)
            tournament.update(
                last_round_completed=form.data['last_round_completed'])
            return {'tournament': tournament.to_dict()}, 200
        return {'errors': validation_errors_to_error_messages(form.errors)}, 401
    elif request.method == 'DELETE':
        tournament = Tournament.query.get(id)
        tournament.delete()
        return {'messages': {'success': ['Tournament deleted successfully']}}, 200


@admin_routes.route('/game/<int:id>',  methods=['GET', 'PUT'])
def game(id):
    if request.method == 'GET':
        game = Game.query.get(id)
        return {'game': game.to_admin_dict()}, 200
    elif request.method == 'PUT':
        game = Game.query.get(id)
        req_data = json.loads(request.data)
        game_team_score1 = Game_Team_Score.query.get(
            req_data['game_team_score1']['id'])
        game_team_score1.score = req_data['game_team_score1']['score']
        game_team_score2 = Game_Team_Score.query.get(
            req_data['game_team_score2']['id'])
        game_team_score2.score = req_data['game_team_score2']['score']
        winning_game_team_score = game_team_score1 if game_team_score1.score > game_team_score2.score else game_team_score2
        game.winning_team_id = winning_game_team_score.team_id
        next_game_num = get_next_game_num(game.game_num)
        if next_game_num:
            next_game = Game.query.filter(Game.tournament_id == game.tournament_id).filter(
                Game.game_num == next_game_num).first()
            new_game_team_score = Game_Team_Score(
                game_id=next_game.id, team_id=winning_game_team_score.team_id, score=None)
            db.session.add(new_game_team_score)
        db.session.commit()

        return {'game': game.to_admin_dict()}, 200
