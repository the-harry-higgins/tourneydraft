from flask.cli import AppGroup
from .dumb_friends_league import seed_dumb_friends_league, undo_dumb_friends_league
from .colleges import seed_colleges, undo_colleges
from .tournament_2018 import seed_2018_tournament, undo_2018_tournament

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command
@seed_commands.command('all')
def seed():
    seed_dumb_friends_league()
    seed_colleges()
    seed_2018_tournament()

# Creates the `flask seed undo` command
@seed_commands.command('undo')
def undo():
    undo_dumb_friends_league()
    undo_colleges()
    undo_2018_tournament()
