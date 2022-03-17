from app.models import db, Game, Tournament

from app.utils import get_round_num


def fix_2022_tournament():
    tournament = Tournament.query.filter(Tournament.year == 2022).one()
    for i in range(33, 64):
        round_num = get_round_num(i)
        game = Game(game_num=i, round_num=round_num,
                    winning_team_id=None, tournament_id=tournament.id)
        db.session.add(game)
        db.session.commit()
