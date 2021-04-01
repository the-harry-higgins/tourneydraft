from app.models import db, March_Madness_Team, College, Game, Game_Team_Score, Tournament
import json
from datetime import datetime


def seed_2021_tournament_round3():
    tournament = Tournament.query.filter(Tournament.year == 2021).one()
    tournament.last_round_completed = 3

    # West
    Gonzaga = College.query.filter(College.name == 'Gonzaga').one()
    gonzaga = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Gonzaga.id
    ).one()

    Creighton = College.query.filter(College.name == 'Creighton').one()
    creighton = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Creighton.id
    ).one()

    USC = College.query.filter(College.name == 'USC').one()
    uSC = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == USC.id
    ).one()

    Oregon = College.query.filter(College.name == 'Oregon').one()
    oregon = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Oregon.id
    ).one()

    # South
    Baylor = College.query.filter(College.name == 'Baylor').one()
    baylor = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Baylor.id
    ).one()

    Villanova = College.query.filter(College.name == 'Villanova').one()
    villanova = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Villanova.id
    ).one()

    Arkansas = College.query.filter(College.name == 'Arkansas').one()
    arkansas = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Arkansas.id
    ).one()

    Oral_Roberts = College.query.filter(College.name == 'Oral Roberts').one()
    oral_Roberts = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Oral_Roberts.id
    ).one()

    # Midwest
    Loyola_Chicago = College.query.filter(
        College.name == 'Loyola Chicago').one()
    loyola_Chicago = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Loyola_Chicago.id
    ).one()

    Oregon_State = College.query.filter(College.name == 'Oregon State').one()
    oregon_State = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Oregon_State.id
    ).one()

    Syracuse = College.query.filter(College.name == 'Syracuse').one()
    syracuse = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Syracuse.id
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

    Florida_State = College.query.filter(College.name == 'Florida State').one()
    florida_State = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Florida_State.id
    ).one()

    UCLA = College.query.filter(
        College.name == 'UCLA').one()
    uCLA = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == UCLA.id
    ).one()

    Alabama = College.query.filter(College.name == 'Alabama').one()
    alabama = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Alabama.id
    ).one()

    game_49 = Game.query.filter(
        Game.game_num == 49
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_49.winning_team_id = gonzaga.id

    game_50 = Game.query.filter(
        Game.game_num == 50
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_50.winning_team_id = uSC.id

    game_51 = Game.query.filter(
        Game.game_num == 51
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_51.winning_team_id = michigan.id

    game_52 = Game.query.filter(
        Game.game_num == 52
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_52.winning_team_id = uCLA.id

    game_53 = Game.query.filter(
        Game.game_num == 53
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_53.winning_team_id = baylor.id

    game_54 = Game.query.filter(
        Game.game_num == 54
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_54.winning_team_id = arkansas.id

    game_55 = Game.query.filter(
        Game.game_num == 55
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_55.winning_team_id = oregon_State.id

    game_56 = Game.query.filter(
        Game.game_num == 56
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_56.winning_team_id = houston.id

    db.session.commit()

    game_49_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_49.id).filter(
        Game_Team_Score.team_id == gonzaga.id
    ).one()
    game_49_win_score.score = 83
    game_49_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_49.id).filter(
        Game_Team_Score.team_id == creighton.id
    ).one()
    game_49_lose_score.score = 65

    game_50_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_50.id).filter(
        Game_Team_Score.team_id == uSC.id
    ).one()
    game_50_win_score.score = 82
    game_50_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_50.id).filter(
        Game_Team_Score.team_id == oregon.id
    ).one()
    game_50_lose_score.score = 68

    game_51_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_51.id).filter(
        Game_Team_Score.team_id == michigan.id
    ).one()
    game_51_win_score.score = 76
    game_51_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_51.id).filter(
        Game_Team_Score.team_id == florida_State.id
    ).one()
    game_51_lose_score.score = 58

    game_52_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_52.id).filter(
        Game_Team_Score.team_id == uCLA.id
    ).one()
    game_52_win_score.score = 88
    game_52_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_52.id).filter(
        Game_Team_Score.team_id == alabama.id
    ).one()
    game_52_lose_score.score = 78

    game_53_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_53.id).filter(
        Game_Team_Score.team_id == baylor.id
    ).one()
    game_53_win_score.score = 62
    game_53_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_53.id).filter(
        Game_Team_Score.team_id == villanova.id
    ).one()
    game_53_lose_score.score = 51

    game_54_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_54.id).filter(
        Game_Team_Score.team_id == arkansas.id
    ).one()
    game_54_win_score.score = 72
    game_54_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_54.id).filter(
        Game_Team_Score.team_id == oral_Roberts.id
    ).one()
    game_54_lose_score.score = 70

    game_55_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_55.id).filter(
        Game_Team_Score.team_id == oregon_State.id
    ).one()
    game_55_win_score.score = 65
    game_55_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_55.id).filter(
        Game_Team_Score.team_id == loyola_Chicago.id
    ).one()
    game_55_lose_score.score = 58

    game_56_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_56.id).filter(
        Game_Team_Score.team_id == houston.id
    ).one()
    game_56_win_score.score = 62
    game_56_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_56.id).filter(
        Game_Team_Score.team_id == syracuse.id
    ).one()
    game_56_lose_score.score = 46

    db.session.commit()

    game_57 = Game(game_num=57, round_num=4,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_57)
    game_58 = Game(game_num=58, round_num=4,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_58)
    game_59 = Game(game_num=59, round_num=4,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_59)
    game_60 = Game(game_num=60, round_num=4,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_60)

    db.session.commit()

    game_49.child_game_id = game_57.id
    game_50.child_game_id = game_57.id

    game_51.child_game_id = game_58.id
    game_52.child_game_id = game_58.id

    game_53.child_game_id = game_59.id
    game_54.child_game_id = game_59.id

    game_55.child_game_id = game_60.id
    game_56.child_game_id = game_60.id

    db.session.commit()

    game_57_win_score = Game_Team_Score(
        game_id=game_57.id, team_id=gonzaga.id, score=None)
    game_57_lose_score = Game_Team_Score(
        game_id=game_57.id, team_id=uSC.id, score=None)
    game_57.game_team_scores = [game_57_win_score, game_57_lose_score]

    game_58_win_score = Game_Team_Score(
        game_id=game_58.id, team_id=michigan.id, score=None)
    game_58_lose_score = Game_Team_Score(
        game_id=game_58.id, team_id=uCLA.id, score=None)
    game_58.game_team_scores = [game_58_win_score, game_58_lose_score]

    game_59_win_score = Game_Team_Score(
        game_id=game_59.id, team_id=baylor.id, score=None)
    game_59_lose_score = Game_Team_Score(
        game_id=game_59.id, team_id=arkansas.id, score=None)
    game_59.game_team_scores = [game_59_win_score, game_59_lose_score]

    game_60_win_score = Game_Team_Score(
        game_id=game_60.id, team_id=oregon_State.id, score=None)
    game_60_lose_score = Game_Team_Score(
        game_id=game_60.id, team_id=houston.id, score=None)
    game_60.game_team_scores = [game_60_win_score, game_60_lose_score]

    db.session.commit()

    print('done')


def undo_2021_tournament_round3():
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
