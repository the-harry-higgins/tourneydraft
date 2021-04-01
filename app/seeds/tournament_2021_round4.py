from app.models import db, March_Madness_Team, College, Game, Game_Team_Score, Tournament
import json
from datetime import datetime


def seed_2021_tournament_round4():
    tournament = Tournament.query.filter(Tournament.year == 2021).one()
    tournament.last_round_completed = 4

    # West
    Gonzaga = College.query.filter(College.name == 'Gonzaga').one()
    gonzaga = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Gonzaga.id
    ).one()

    USC = College.query.filter(College.name == 'USC').one()
    uSC = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == USC.id
    ).one()

    # South
    Baylor = College.query.filter(College.name == 'Baylor').one()
    baylor = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Baylor.id
    ).one()

    Arkansas = College.query.filter(College.name == 'Arkansas').one()
    arkansas = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Arkansas.id
    ).one()

    # Midwest
    Oregon_State = College.query.filter(College.name == 'Oregon State').one()
    oregon_State = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Oregon_State.id
    ).one()

    Houston = College.query.filter(College.name == 'Houston').one()
    houston = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Houston.id
    ).one()

    # East
    Michigan = College.query.filter(College.name == 'Michigan').one()
    michigan = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Michigan.id
    ).one()

    UCLA = College.query.filter(
        College.name == 'UCLA').one()
    uCLA = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == UCLA.id
    ).one()

    game_57 = Game.query.filter(
        Game.game_num == 57
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_57.winning_team_id = gonzaga.id

    game_58 = Game.query.filter(
        Game.game_num == 58
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_58.winning_team_id = uCLA.id

    game_59 = Game.query.filter(
        Game.game_num == 59
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_59.winning_team_id = baylor.id

    game_60 = Game.query.filter(
        Game.game_num == 60
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_60.winning_team_id = houston.id

    db.session.commit()

    game_57_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_57.id).filter(
        Game_Team_Score.team_id == gonzaga.id
    ).one()
    game_57_win_score.score = 85
    game_57_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_57.id).filter(
        Game_Team_Score.team_id == uSC.id
    ).one()
    game_57_lose_score.score = 66

    game_58_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_58.id).filter(
        Game_Team_Score.team_id == uCLA.id
    ).one()
    game_58_win_score.score = 51
    game_58_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_58.id).filter(
        Game_Team_Score.team_id == michigan.id
    ).one()
    game_58_lose_score.score = 49

    game_59_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_59.id).filter(
        Game_Team_Score.team_id == baylor.id
    ).one()
    game_59_win_score.score = 81
    game_59_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_59.id).filter(
        Game_Team_Score.team_id == arkansas.id
    ).one()
    game_59_lose_score.score = 72

    game_60_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_60.id).filter(
        Game_Team_Score.team_id == houston.id
    ).one()
    game_60_win_score.score = 67
    game_60_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_60.id).filter(
        Game_Team_Score.team_id == oregon_State.id
    ).one()
    game_60_lose_score.score = 61

    db.session.commit()

    game_61 = Game(game_num=61, round_num=5,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_61)
    game_62 = Game(game_num=62, round_num=5,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_62)

    db.session.commit()

    game_57.child_game_id = game_61.id
    game_58.child_game_id = game_61.id

    game_59.child_game_id = game_62.id
    game_60.child_game_id = game_62.id

    db.session.commit()

    game_61_win_score = Game_Team_Score(
        game_id=game_61.id, team_id=gonzaga.id, score=None)
    game_61_lose_score = Game_Team_Score(
        game_id=game_61.id, team_id=uCLA.id, score=None)
    game_61.game_team_scores = [game_61_win_score, game_61_lose_score]

    game_62_win_score = Game_Team_Score(
        game_id=game_62.id, team_id=baylor.id, score=None)
    game_62_lose_score = Game_Team_Score(
        game_id=game_62.id, team_id=houston.id, score=None)
    game_62.game_team_scores = [game_62_win_score, game_62_lose_score]

    db.session.commit()

    print('done')


def undo_2021_tournament_round4():
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
