from flask.cli import AppGroup
from .dumb_friends_league import seed_dumb_friends_league, undo_dumb_friends_league
from .league_of_extraordinary_gentlemen import seed_league_of_extraordinary_gentlemen, undo_league_of_extraordinary_gentlemen
from .colleges import seed_colleges, undo_colleges
from .tournament_2018 import seed_2018_tournament, undo_2018_tournament
from .tournament_2019 import seed_2019_tournament, undo_2019_tournament
from .draft_2019 import seed_draft_2019, undo_draft_2019
from .colleges_2021 import seed_colleges_2021, undo_colleges_2021
from .tournament_2021 import seed_2021_tournament, undo_2021_tournament
from .tournament_2021_round1 import seed_2021_tournament_round1, undo_2021_tournament_round1
from .tournament_2021_round2 import seed_2021_tournament_round2, undo_2021_tournament_round2
from .tournament_2021_round3 import seed_2021_tournament_round3, undo_2021_tournament_round3
from .tournament_2021_round4 import seed_2021_tournament_round4, undo_2021_tournament_round4
from .tournament_2021_round5 import seed_2021_tournament_round5, undo_2021_tournament_round5
from .tournament_2021_round6 import seed_2021_tournament_round6, undo_2021_tournament_round6

# Creates a seed group to hold our commands
# So we can type `flask seed --help`
seed_commands = AppGroup('seed')

# Creates the `flask seed all` command


@seed_commands.command('all')
def seed():
    seed_dumb_friends_league()
    seed_league_of_extraordinary_gentlemen()
    seed_colleges()
    seed_2018_tournament()
    seed_2019_tournament()
    seed_draft_2019()

# Creates the `flask seed undo` command


@seed_commands.command('undo')
def undo():
    undo_dumb_friends_league()
    undo_league_of_extraordinary_gentlemen()
    undo_colleges()
    undo_2018_tournament()
    undo_2019_tournament()
    undo_draft_2019()


@seed_commands.command('2021')
def seed_2021():
    seed_colleges_2021()
    seed_2021_tournament()


@seed_commands.command('undo-2021')
def undo_2021():
    undo_colleges_2021()
    undo_2021_tournament()


@seed_commands.command('2021-round1')
def seed_2021():
    seed_2021_tournament_round1()


@seed_commands.command('2021-round2')
def seed_2021():
    seed_2021_tournament_round2()


@seed_commands.command('2021-round3')
def seed_2021():
    seed_2021_tournament_round3()


@seed_commands.command('2021-round4')
def seed_2021():
    seed_2021_tournament_round4()


@seed_commands.command('2021-round5')
def seed_2021():
    seed_2021_tournament_round5()


@seed_commands.command('2021-round6')
def seed_2021():
    seed_2021_tournament_round6()