from app.models import db, March_Madness_Team, College, Game, Game_Team_Score, Tournament
import json
from datetime import datetime


def seed_2021_tournament_round5():
    tournament = Tournament.query.filter(Tournament.year == 2021).one()
    # tournament.last_round_completed = 5

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

    # Midwest
    # Houston = College.query.filter(College.name == 'Houston').one()
    # houston = March_Madness_Team.query.filter(
    #     March_Madness_Team.tournament_id == tournament.id).filter(
    #     March_Madness_Team.college_id == Houston.id
    # ).one()

    # # East
    # UCLA = College.query.filter(
    #     College.name == 'UCLA').one()
    # uCLA = March_Madness_Team.query.filter(
    #     March_Madness_Team.tournament_id == tournament.id).filter(
    #     March_Madness_Team.college_id == UCLA.id
    # ).one()

    # game_61 = Game.query.filter(
    #     Game.game_num == 61
    # ).filter(
    #     Game.tournament_id == tournament.id
    # ).one()
    # game_61.winning_team_id = gonzaga.id

    # game_62 = Game.query.filter(
    #     Game.game_num == 62
    # ).filter(
    #     Game.tournament_id == tournament.id
    # ).one()
    # game_62.winning_team_id = baylor.id

    # db.session.commit()

    # game_61_win_score = Game_Team_Score.query.filter(
    #     Game_Team_Score.game_id == game_61.id).filter(
    #     Game_Team_Score.team_id == gonzaga.id
    # ).one()
    # game_61_win_score.score = 93
    # game_61_lose_score = Game_Team_Score.query.filter(
    #     Game_Team_Score.game_id == game_61.id).filter(
    #     Game_Team_Score.team_id == uCLA.id
    # ).one()
    # game_61_lose_score.score = 90

    # game_62_win_score = Game_Team_Score.query.filter(
    #     Game_Team_Score.game_id == game_62.id).filter(
    #     Game_Team_Score.team_id == baylor.id
    # ).one()
    # game_62_win_score.score = 78
    # game_62_lose_score = Game_Team_Score.query.filter(
    #     Game_Team_Score.game_id == game_62.id).filter(
    #     Game_Team_Score.team_id == houston.id
    # ).one()
    # game_62_lose_score.score = 59

    # db.session.commit()

    # game_63 = Game(game_num=63, round_num=6,
    #                winning_team_id=None, tournament_id=tournament.id)
    # db.session.add(game_63)

    # db.session.commit()

    # game_61.child_game_id = game_63.id
    # game_62.child_game_id = game_63.id

    # db.session.commit()

    game_63 = Game.query.filter(
        Game.game_num == 63
    ).filter(
        Game.tournament_id == tournament.id
    ).one()

    game_63_win_score = Game_Team_Score(
        game_id=game_63.id, team_id=gonzaga.id, score=None)
    game_63_lose_score = Game_Team_Score(
        game_id=game_63.id, team_id=baylor.id, score=None)
    game_63.game_team_scores = [game_63_win_score, game_63_lose_score]

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
