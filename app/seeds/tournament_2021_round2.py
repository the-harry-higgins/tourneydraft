from app.models import db, March_Madness_Team, College, Game, Game_Team_Score, Tournament
import json
from datetime import datetime


def seed_2021_tournament_round2():
    tournament = Tournament.query.filter(Tournament.year == 2021).one()
    tournament.last_round_completed = 2

    # West
    Gonzaga = College.query.filter(College.name == 'Gonzaga').one()
    gonzaga = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Gonzaga.id
    ).one()

    Oklahoma = College.query.filter(College.name == 'Oklahoma').one()
    oklahoma = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Oklahoma.id
    ).one()

    Creighton = College.query.filter(College.name == 'Creighton').one()
    creighton = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Creighton.id
    ).one()

    Ohio = College.query.filter(College.name == 'Ohio').one()
    ohio = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Ohio.id
    ).one()

    USC = College.query.filter(College.name == 'USC').one()
    uSC = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == USC.id
    ).one()

    Kansas = College.query.filter(College.name == 'Kansas').one()
    kansas = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Kansas.id
    ).one()

    Oregon = College.query.filter(College.name == 'Oregon').one()
    oregon = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Oregon.id
    ).one()

    Iowa = College.query.filter(College.name == 'Iowa').one()
    iowa = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Iowa.id
    ).one()

    # South
    Baylor = College.query.filter(College.name == 'Baylor').one()
    baylor = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Baylor.id
    ).one()

    Wisconsin = College.query.filter(College.name == 'Wisconsin').one()
    wisconsin = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Wisconsin.id
    ).one()

    Villanova = College.query.filter(College.name == 'Villanova').one()
    villanova = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Villanova.id
    ).one()

    North_Texas = College.query.filter(College.name == 'North Texas').one()
    north_Texas = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == North_Texas.id
    ).one()

    Texas_Tech = College.query.filter(College.name == 'Texas Tech').one()
    texas_Tech = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Texas_Tech.id
    ).one()

    Arkansas = College.query.filter(College.name == 'Arkansas').one()
    arkansas = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Arkansas.id
    ).one()

    Florida = College.query.filter(College.name == 'Florida').one()
    florida = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Florida.id
    ).one()

    Oral_Roberts = College.query.filter(College.name == 'Oral Roberts').one()
    oral_Roberts = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Oral_Roberts.id
    ).one()

    # Midwest
    Illinois = College.query.filter(College.name == 'Illinois').one()
    illinois = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Illinois.id
    ).one()

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

    Oklahoma_State = College.query.filter(
        College.name == 'Oklahoma State').one()
    oklahoma_State = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Oklahoma_State.id
    ).one()

    Syracuse = College.query.filter(College.name == 'Syracuse').one()
    syracuse = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Syracuse.id
    ).one()

    West_Virginia = College.query.filter(College.name == 'West Virginia').one()
    west_Virginia = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == West_Virginia.id
    ).one()

    Rutgers = College.query.filter(College.name == 'Rutgers').one()
    rutgers = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Rutgers.id
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

    LSU = College.query.filter(College.name == 'LSU').one()
    lSU = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == LSU.id
    ).one()

    Colorado = College.query.filter(College.name == 'Colorado').one()
    colorado = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Colorado.id
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

    Abilene_Christian = College.query.filter(
        College.name == 'Abilene Christian').one()
    abilene_Christian = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Abilene_Christian.id
    ).one()

    Maryland = College.query.filter(College.name == 'Maryland').one()
    maryland = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Maryland.id
    ).one()

    Alabama = College.query.filter(College.name == 'Alabama').one()
    alabama = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Alabama.id
    ).one()

    game_33 = Game.query.filter(
        Game.game_num == 33
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_33.winning_team_id = gonzaga.id

    game_34 = Game.query.filter(
        Game.game_num == 34
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_34.winning_team_id = creighton.id

    game_35 = Game.query.filter(
        Game.game_num == 35
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_35.winning_team_id = uSC.id

    game_36 = Game.query.filter(
        Game.game_num == 36
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_36.winning_team_id = oregon.id

    game_37 = Game.query.filter(
        Game.game_num == 37
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_37.winning_team_id = michigan.id

    game_38 = Game.query.filter(
        Game.game_num == 38
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_38.winning_team_id = florida_State.id

    game_39 = Game.query.filter(
        Game.game_num == 39
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_39.winning_team_id = uCLA.id

    game_40 = Game.query.filter(
        Game.game_num == 40
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_40.winning_team_id = alabama.id

    game_41 = Game.query.filter(
        Game.game_num == 41
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_41.winning_team_id = baylor.id

    game_42 = Game.query.filter(
        Game.game_num == 42
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_42.winning_team_id = villanova.id

    game_43 = Game.query.filter(
        Game.game_num == 43
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_43.winning_team_id = arkansas.id

    game_44 = Game.query.filter(
        Game.game_num == 44
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_44.winning_team_id = oral_Roberts.id

    game_45 = Game.query.filter(
        Game.game_num == 45
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_45.winning_team_id = loyola_Chicago.id

    game_46 = Game.query.filter(
        Game.game_num == 46
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_46.winning_team_id = oregon_State.id

    game_47 = Game.query.filter(
        Game.game_num == 47
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_47.winning_team_id = syracuse.id

    game_48 = Game.query.filter(
        Game.game_num == 48
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_48.winning_team_id = houston.id

    db.session.commit()

    game_33_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_33.id).filter(
        Game_Team_Score.team_id == gonzaga.id
    ).one()
    game_33_win_score.score = 87
    game_33_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_33.id).filter(
        Game_Team_Score.team_id == oklahoma.id
    ).one()
    game_33_lose_score.score = 71

    game_34_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_34.id).filter(
        Game_Team_Score.team_id == creighton.id
    ).one()
    game_34_win_score.score = 72
    game_34_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_34.id).filter(
        Game_Team_Score.team_id == ohio.id
    ).one()
    game_34_lose_score.score = 58

    game_35_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_35.id).filter(
        Game_Team_Score.team_id == uSC.id
    ).one()
    game_35_win_score.score = 85
    game_35_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_35.id).filter(
        Game_Team_Score.team_id == kansas.id
    ).one()
    game_35_lose_score.score = 51

    game_36_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_36.id).filter(
        Game_Team_Score.team_id == oregon.id
    ).one()
    game_36_win_score.score = 95
    game_36_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_36.id).filter(
        Game_Team_Score.team_id == iowa.id
    ).one()
    game_36_lose_score.score = 80

    game_37_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_37.id).filter(
        Game_Team_Score.team_id == michigan.id
    ).one()
    game_37_win_score.score = 86
    game_37_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_37.id).filter(
        Game_Team_Score.team_id == lSU.id
    ).one()
    game_37_lose_score.score = 78

    game_38_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_38.id).filter(
        Game_Team_Score.team_id == florida_State.id
    ).one()
    game_38_win_score.score = 71
    game_38_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_38.id).filter(
        Game_Team_Score.team_id == colorado.id
    ).one()
    game_38_lose_score.score = 53

    game_39_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_39.id).filter(
        Game_Team_Score.team_id == uCLA.id
    ).one()
    game_39_win_score.score = 67
    game_39_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_39.id).filter(
        Game_Team_Score.team_id == abilene_Christian.id
    ).one()
    game_39_lose_score.score = 47

    game_40_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_40.id).filter(
        Game_Team_Score.team_id == alabama.id
    ).one()
    game_40_win_score.score = 96
    game_40_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_40.id).filter(
        Game_Team_Score.team_id == maryland.id
    ).one()
    game_40_lose_score.score = 77

    game_41_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_41.id).filter(
        Game_Team_Score.team_id == baylor.id
    ).one()
    game_41_win_score.score = 76
    game_41_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_41.id).filter(
        Game_Team_Score.team_id == wisconsin.id
    ).one()
    game_41_lose_score.score = 63

    game_42_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_42.id).filter(
        Game_Team_Score.team_id == villanova.id
    ).one()
    game_42_win_score.score = 84
    game_42_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_42.id).filter(
        Game_Team_Score.team_id == north_Texas.id
    ).one()
    game_42_lose_score.score = 61

    game_43_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_43.id).filter(
        Game_Team_Score.team_id == arkansas.id
    ).one()
    game_43_win_score.score = 68
    game_43_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_43.id).filter(
        Game_Team_Score.team_id == texas_Tech.id
    ).one()
    game_43_lose_score.score = 66

    game_44_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_44.id).filter(
        Game_Team_Score.team_id == oral_Roberts.id
    ).one()
    game_44_win_score.score = 81
    game_44_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_44.id).filter(
        Game_Team_Score.team_id == florida.id
    ).one()
    game_44_lose_score.score = 78

    game_45_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_45.id).filter(
        Game_Team_Score.team_id == loyola_Chicago.id
    ).one()
    game_45_win_score.score = 71
    game_45_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_45.id).filter(
        Game_Team_Score.team_id == illinois.id
    ).one()
    game_45_lose_score.score = 58

    game_46_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_46.id).filter(
        Game_Team_Score.team_id == oregon_State.id
    ).one()
    game_46_win_score.score = 80
    game_46_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_46.id).filter(
        Game_Team_Score.team_id == oklahoma_State.id
    ).one()
    game_46_lose_score.score = 70

    game_47_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_47.id).filter(
        Game_Team_Score.team_id == syracuse.id
    ).one()
    game_47_win_score.score = 75
    game_47_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_47.id).filter(
        Game_Team_Score.team_id == west_Virginia.id
    ).one()
    game_47_lose_score.score = 72

    game_48_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_48.id).filter(
        Game_Team_Score.team_id == houston.id
    ).one()
    game_48_win_score.score = 63
    game_48_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_48.id).filter(
        Game_Team_Score.team_id == rutgers.id
    ).one()
    game_48_lose_score.score = 60

    db.session.commit()

    game_49 = Game(game_num=49, round_num=3,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_49)
    game_50 = Game(game_num=50, round_num=3,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_50)
    game_51 = Game(game_num=51, round_num=3,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_51)
    game_52 = Game(game_num=52, round_num=3,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_52)
    game_53 = Game(game_num=53, round_num=3,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_53)
    game_54 = Game(game_num=54, round_num=3,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_54)
    game_55 = Game(game_num=55, round_num=3,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_55)
    game_56 = Game(game_num=56, round_num=3,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_56)

    db.session.commit()

    game_33.child_game_id = game_49.id
    game_34.child_game_id = game_49.id

    game_35.child_game_id = game_50.id
    game_36.child_game_id = game_50.id

    game_37.child_game_id = game_51.id
    game_38.child_game_id = game_51.id

    game_39.child_game_id = game_52.id
    game_40.child_game_id = game_52.id

    game_41.child_game_id = game_53.id
    game_42.child_game_id = game_53.id

    game_43.child_game_id = game_54.id
    game_44.child_game_id = game_54.id

    game_45.child_game_id = game_55.id
    game_46.child_game_id = game_55.id

    game_47.child_game_id = game_56.id
    game_48.child_game_id = game_56.id

    db.session.commit()

    game_49_win_score = Game_Team_Score(
        game_id=game_49.id, team_id=gonzaga.id, score=None)
    game_49_lose_score = Game_Team_Score(
        game_id=game_49.id, team_id=creighton.id, score=None)
    game_49.game_team_scores = [game_49_win_score, game_49_lose_score]

    game_50_win_score = Game_Team_Score(
        game_id=game_50.id, team_id=uSC.id, score=None)
    game_50_lose_score = Game_Team_Score(
        game_id=game_50.id, team_id=oregon.id, score=None)
    game_50.game_team_scores = [game_50_win_score, game_50_lose_score]

    game_51_win_score = Game_Team_Score(
        game_id=game_51.id, team_id=michigan.id, score=None)
    game_51_lose_score = Game_Team_Score(
        game_id=game_51.id, team_id=florida_State.id, score=None)
    game_51.game_team_scores = [game_51_win_score, game_51_lose_score]

    game_52_win_score = Game_Team_Score(
        game_id=game_52.id, team_id=uCLA.id, score=None)
    game_52_lose_score = Game_Team_Score(
        game_id=game_52.id, team_id=alabama.id, score=None)
    game_52.game_team_scores = [game_52_win_score, game_52_lose_score]

    game_53_win_score = Game_Team_Score(
        game_id=game_53.id, team_id=baylor.id, score=None)
    game_53_lose_score = Game_Team_Score(
        game_id=game_53.id, team_id=villanova.id, score=None)
    game_53.game_team_scores = [game_53_win_score, game_53_lose_score]

    game_54_win_score = Game_Team_Score(
        game_id=game_54.id, team_id=arkansas.id, score=None)
    game_54_lose_score = Game_Team_Score(
        game_id=game_54.id, team_id=oral_Roberts.id, score=None)
    game_54.game_team_scores = [game_54_win_score, game_54_lose_score]

    game_55_win_score = Game_Team_Score(
        game_id=game_55.id, team_id=loyola_Chicago.id, score=None)
    game_55_lose_score = Game_Team_Score(
        game_id=game_55.id, team_id=oregon_State.id, score=None)
    game_55.game_team_scores = [game_55_win_score, game_55_lose_score]

    game_56_win_score = Game_Team_Score(
        game_id=game_56.id, team_id=syracuse.id, score=None)
    game_56_lose_score = Game_Team_Score(
        game_id=game_56.id, team_id=houston.id, score=None)
    game_56.game_team_scores = [game_56_win_score, game_56_lose_score]

    db.session.commit()

    print('done')


def undo_2021_tournament_round2():
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
