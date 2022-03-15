from app.models import db, March_Madness_Team, College, Game, Game_Team_Score, Tournament
import json
from datetime import datetime


def seed_2021_tournament_round5():
    tournament = Tournament.query.filter(Tournament.year == 2021).one()
    tournament.last_round_completed = 6

    # West
    Gonzaga = College.query.filter(College.name == 'Gonzaga').one()
    gonzaga = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Gonzaga.id
    ).one()

    # South
    Baylor = College.query.filter(College.name == 'Baylor').one()
    baylor = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Baylor.id
    ).one()

    game_63 = Game.query.filter(
        Game.game_num == 63
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_63.winning_team_id = baylor.id

    db.session.commit()

    game_63_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_63.id).filter(
        Game_Team_Score.team_id == baylor.id
    ).one()
    game_63_win_score.score = 86
    game_63_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_63.id).filter(
        Game_Team_Score.team_id == gonzaga.id
    ).one()
    game_63_lose_score.score = 70

    db.session.commit()

    print('done')


def undo_2021_tournament_round5():
    # tournament = Tournament.query.filter(Tournament.year == 2021).one()

    # db.session.execute(
    #     'DELETE from games WHERE tournament_id = :id', {'id': tournament.id})
    # db.session.execute(
    #     'DELETE from march_madness_teams WHERE tournament_id = :id', {'id': tournament.id})
    # db.session.execute(
    #     'DELETE from march_madness_teams WHERE tournament_id = :id', {'id': tournament.id})
    # db.session.execute(
    #     'DELETE from tournaments WHERE id = :id', {'id': tournament.id})
    # db.session.commit()
    pass
