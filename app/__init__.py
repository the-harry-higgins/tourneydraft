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

from .models import db, User
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
    if path:
        return app.send_static_file(path)
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
    emit('join_draft', {'Draft': 'New draft'})


# @socketio.on('my event')
# def handle_my_custom_event(json):
#     print('received json: ' + str(json))


# @socketio.on('join')
# def on_join(data):
#     username = data['username']
#     room = data['room']
#     join_room(room)
#     send(username + ' has entered the room.', room=room)


# @socketio.on('leave')
# def on_leave(data):
#     username = data['username']
#     room = data['room']
#     leave_room(room)
#     send(username + ' has left the room.', room=room)
