import os
from flask import Flask, render_template, request, session
from flask_cors import CORS
from flask_migrate import Migrate
from flask_wtf.csrf import CSRFProtect, generate_csrf
from flask_login import LoginManager
from flask_socketio import SocketIO, emit, send
from flask_socketio import join_room, leave_room
import json
import eventlet

from .models import db, User, Draft, Drafted_Team
from .api.auth_routes import auth_routes
from .api.league_routes import league_routes
from .api.draft_routes import draft_routes

from .seeds import seed_commands

from .config import Config

app = Flask(__name__)

# Setup login manager
login = LoginManager(app)
login.login_view = 'auth.unauthorized'


@login.user_loader
def load_user(id):
    return User.query.get(int(id))


# Tell flask about our seed commands
app.cli.add_command(seed_commands)

app.config.from_object(Config)

app.register_blueprint(auth_routes, url_prefix='/api/auth')
app.register_blueprint(league_routes, url_prefix='/api/leagues')
app.register_blueprint(
    draft_routes,
    url_prefix='/api/leagues/<int:league_id>/drafts'
)


db.init_app(app)
Migrate(app, db)

# Application Security
CORS(app)

socketio = SocketIO(
    app,
    cors_allowed_origins='*',
    logger=True,
    engineio_logger=True,
    async_mode='eventlet'
)


@app.before_request
def redirect_https():
    if os.environ.get('FLASK_ENV') == 'production':
        if request.headers.get('X-Forwarded-Proto') == 'http':
            url = request.url.replace('http://', 'https://', 1)
            code = 301
            return redirect(url, code=code)


@app.after_request
def inject_csrf_token(response):
    response.set_cookie('csrf_token',
                        generate_csrf(),
                        secure=True if os.environ.get(
                            'FLASK_ENV') == 'production' else False,
                        samesite='Strict' if os.environ.get(
                            'FLASK_ENV') == 'production' else None,
                        httponly=True)
    return response


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def react_root(path):
    if path and path not in ['draft', 'bracket', 'leaderboard', 'splash', 'demo-draft']:
        return app.send_static_file(path)
    print(path)
    return app.send_static_file('index.html')


@socketio.on('connect')
def test_connect():
    print('Client connected')


@socketio.on('disconnect')
def test_disconnect():
    print('Client disconnected')


@socketio.on('join')
def on_join(data):
    print('Join received message: ', json.dumps(data))
    username = data['username']
    room = data['room']
    join_room(room)
    emit('join_draft', username + ' has entered the room.', room=room)


@socketio.on('leave')
def on_leave(data):
    username = data['username']
    room = data['room']
    leave_room(room)
    send(username + ' has left the room.', room=room)


@socketio.on('draft team')
def draft_team(data):
    draft = Draft.query.filter(Draft.id == data['draft_id']).one()
    if draft.current_drafter_id == data['league_user_id'] and draft.draft_index == data['selection_num'] - 1:
        try:
            drafted_team = Drafted_Team(
                march_madness_team_id=data['march_madness_team_id'],
                league_user_id=data['league_user_id'],
                draft_id=data['draft_id'],
                selection_num=data['selection_num'])
            draft.draft_index += 1
            order = json.loads(draft.draft_order)
            draft.current_drafter_id = order[draft.draft_index]
            db.session.add(draft)
            db.session.add(drafted_team)
            db.session.commit()
            response = {
                'messages': [data['username'] + ' has drafted ' +
                            drafted_team.march_madness_team.college.name],
                'draftedTeams': {
                    drafted_team.id: drafted_team.to_dict()
                    for drafted_team in draft.drafted_teams
                },
                'draft': draft.to_dict()
            }
            print(response)
            emit('draft team', response, room=data['room'])
        except Exception as err:
            print('\n\n\n\n\nERROR', err)
            emit('error', ['That team has already been drafted'])

    else:
        emit('error', ['You are not the current drafter'])
