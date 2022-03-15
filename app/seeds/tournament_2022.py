from app.models import db, March_Madness_Team, College, Game, Game_Team_Score, League, League_User, Draft, Drafted_Team, User, Tournament
import json
from datetime import datetime


def seed_2022_tournament():
    tournament = Tournament(year=2022, region1='West',
                            region2='East', region3='South', region4='Midwest', last_round_completed=0)
    db.session.add(tournament)
    db.session.commit()

    # West
    Gonzaga = College.query.filter(College.name == 'Gonzaga').one()
    gonzaga = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='West', college_id=Gonzaga.id)
    db.session.add(gonzaga)

    Georgia_State = College.query.filter(College.name == 'Georgia State').one()
    georgia_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='West', college_id=Georgia_State.id)
    db.session.add(georgia_State)

    Boise_State = College.query.filter(College.name == 'Boise State').one()
    boise_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='West', college_id=Boise_State.id)
    db.session.add(boise_State)

    Memphis = College.query.filter(College.name == 'Memphis').one()
    memphis = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='West', college_id=Memphis.id)
    db.session.add(memphis)

    UCONN = College.query.filter(College.name == 'UCONN').one()
    uCONN = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='West', college_id=UCONN.id)
    db.session.add(uCONN)

    NMSU = College.query.filter(College.name == 'New Mexico State').one()
    nMSU = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='West', college_id=NMSU.id)
    db.session.add(nMSU)

    Arkansas = College.query.filter(College.name == 'Arkansas').one()
    arkansas = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='West', college_id=Arkansas.id)
    db.session.add(arkansas)

    Vermont = College.query.filter(College.name == 'Vermont').one()
    vermont = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='West', college_id=Vermont.id)
    db.session.add(vermont)

    Alabama = College.query.filter(College.name == 'Alabama').one()
    alabama = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='West', college_id=Alabama.id)
    db.session.add(alabama)

    Rutgers = College.query.filter(College.name == 'Rutgers').one()
    rutgers = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='West', college_id=Rutgers.id)
    db.session.add(rutgers)

    Texas_Tech = College.query.filter(College.name == 'Texas Tech').one()
    texas_Tech = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='West', college_id=Texas_Tech.id)
    db.session.add(texas_Tech)

    Montana_State = College.query.filter(
        College.name == 'Montana State').one()
    montana_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='West', college_id=Montana_State.id)
    db.session.add(montana_State)

    Michigan_State = College.query.filter(College.name == 'Michigan State').one()
    michigan_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='West', college_id=Michigan_State.id)
    db.session.add(michigan_State)

    Davidson = College.query.filter(College.name == 'Davidson').one()
    davidson = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='West', college_id=Davidson.id)
    db.session.add(davidson)

    Duke = College.query.filter(College.name == 'Duke').one()
    duke = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='West', college_id=Duke.id)
    db.session.add(duke)

    Cal_State_Fullerton = College.query.filter(College.name == 'Cal State Fullerton').one()
    cal_State_Fullerton = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='West', college_id=Cal_State_Fullerton.id)
    db.session.add(cal_State_Fullerton)

    # East
    Baylor = College.query.filter(College.name == 'Baylor').one()
    baylor = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='East', college_id=Baylor.id)
    db.session.add(baylor)

    Norfolk_State = College.query.filter(
        College.name == 'Norfolk State').one()
    norfolk_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='East', college_id=Norfolk_State.id)
    db.session.add(norfolk_State)

    North_Carolina = College.query.filter(College.name == 'North Carolina').one()
    north_Carolina = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='East', college_id=North_Carolina.id)
    db.session.add(north_Carolina)

    Marquette = College.query.filter(
        College.name == 'Marquette').one()
    marquette = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='East', college_id=Marquette.id)
    db.session.add(marquette)

    Saint_Marys = College.query.filter(College.name == 'Saint Mary\'s').one()
    saint_Marys = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='East', college_id=Saint_Marys.id)
    db.session.add(saint_Marys)

    Indiana = College.query.filter(College.name == 'Indiana').one()
    indiana = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='East', college_id=Indiana.id)
    db.session.add(indiana)

    UCLA = College.query.filter(College.name == 'UCLA').one()
    uCLA = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='East', college_id=UCLA.id)
    db.session.add(uCLA)

    Akron = College.query.filter(
        College.name == 'Akron').one()
    akron = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='East', college_id=Akron.id)
    db.session.add(akron)

    Texas = College.query.filter(College.name == 'Texas').one()
    texas = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='East', college_id=Texas.id)
    db.session.add(texas)

    Virginia_Tech = College.query.filter(
        College.name == 'Virginia Tech').one()
    virginia_Tech = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='East', college_id=Virginia_Tech.id)
    db.session.add(virginia_Tech)

    Purdue = College.query.filter(College.name == 'Purdue').one()
    purdue = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='East', college_id=Purdue.id)
    db.session.add(purdue)

    Yale = College.query.filter(
        College.name == 'Yale').one()
    yale = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='East', college_id=Yale.id)
    db.session.add(yale)

    Murray_State = College.query.filter(College.name == 'Murray State').one()
    murray_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='East', college_id=Murray_State.id)
    db.session.add(murray_State)

    San_Francisco = College.query.filter(College.name == 'San Francisco').one()
    san_Francisco = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='East', college_id=San_Francisco.id)
    db.session.add(san_Francisco)

    Kentucky = College.query.filter(College.name == 'Kentucky').one()
    kentucky = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='East', college_id=Kentucky.id)
    db.session.add(kentucky)

    Saint_Peters = College.query.filter(College.name == 'Saint Peter\'s').one()
    saint_Peters = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='East', college_id=Saint_Peters.id)
    db.session.add(saint_Peters)

    # South
    Arizona = College.query.filter(College.name == 'Arizona').one()
    arizona = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='South', college_id=Arizona.id)
    db.session.add(arizona)

    Wright_State = College.query.filter(College.name == 'Wright State').one()
    wright_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='South', college_id=Wright_State.id)
    db.session.add(wright_State)

    Seton_Hall = College.query.filter(
        College.name == 'Seton Hall').one()
    seton_Hall = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='South', college_id=Seton_Hall.id)
    db.session.add(seton_Hall)

    TCU = College.query.filter(College.name == 'TCU').one()
    tCU = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='South', college_id=TCU.id)
    db.session.add(tCU)

    Houston = College.query.filter(College.name == 'Houston').one()
    houston = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='South', college_id=Houston.id)
    db.session.add(houston)

    UAB = College.query.filter(College.name == 'UAB').one()
    uAB = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='South', college_id=UAB.id)
    db.session.add(uAB)

    Illinois = College.query.filter(College.name == 'Illinois').one()
    illinois = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='South', college_id=Illinois.id)
    db.session.add(illinois)

    Chattanooga = College.query.filter(College.name == 'Chattanooga').one()
    chattanooga = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='South', college_id=Chattanooga.id)
    db.session.add(chattanooga)

    Colorado_State = College.query.filter(College.name == 'Colorado State').one()
    colorado_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='South', college_id=Colorado_State.id)
    db.session.add(colorado_State)

    Michigan = College.query.filter(College.name == 'Michigan').one()
    michigan = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='South', college_id=Michigan.id)
    db.session.add(michigan)

    Tennessee = College.query.filter(College.name == 'Tennessee').one()
    tennessee = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='South', college_id=Tennessee.id)
    db.session.add(tennessee)

    Longwood = College.query.filter(College.name == 'Longwood').one()
    longwood = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='South', college_id=Longwood.id)
    db.session.add(longwood)

    Ohio_State = College.query.filter(College.name == 'Ohio State').one()
    ohio_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='South', college_id=Ohio_State.id)
    db.session.add(ohio_State)

    Loyola_Chicago = College.query.filter(College.name == 'Loyola Chicago').one()
    loyola_Chicago = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='South', college_id=Loyola_Chicago.id)
    db.session.add(loyola_Chicago)

    Villanova = College.query.filter(College.name == 'Villanova').one()
    villanova = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='South', college_id=Villanova.id)
    db.session.add(villanova)

    Delaware = College.query.filter(College.name == 'Delaware').one()
    delaware = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='South', college_id=Delaware.id)
    db.session.add(delaware)

    # Midwest
    Kansas = College.query.filter(College.name == 'Kansas').one()
    kansas = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='Midwest', college_id=Kansas.id)
    db.session.add(kansas)

    Texas_Southern = College.query.filter(College.name == 'Texas Southern').one()
    texas_Southern = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='Midwest', college_id=Texas_Southern.id)
    db.session.add(texas_Southern)

    San_Diego_State = College.query.filter(
        College.name == 'San Diego State').one()
    san_Diego_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='Midwest', college_id=San_Diego_State.id)
    db.session.add(san_Diego_State)

    Creighton = College.query.filter(College.name == 'Creighton').one()
    creighton = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='Midwest', college_id=Creighton.id)
    db.session.add(creighton)

    Iowa = College.query.filter(College.name == 'Iowa').one()
    iowa = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='Midwest', college_id=Iowa.id)
    db.session.add(iowa)

    Richmond = College.query.filter(College.name == 'Richmond').one()
    richmond = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='Midwest', college_id=Richmond.id)
    db.session.add(richmond)

    Providence = College.query.filter(
        College.name == 'Providence').one()
    providence = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='Midwest', college_id=Providence.id)
    db.session.add(providence)

    South_Dakota_State = College.query.filter(College.name == 'South Dakota State').one()
    south_Dakota_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='Midwest', college_id=South_Dakota_State.id)
    db.session.add(south_Dakota_State)

    LSU = College.query.filter(
        College.name == 'LSU').one()
    lSU = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='Midwest', college_id=LSU.id)
    db.session.add(lSU)

    Iowa_State = College.query.filter(College.name == 'Iowa State').one()
    iowa_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='Midwest', college_id=Iowa_State.id)
    db.session.add(iowa_State)

    Wisconsin = College.query.filter(College.name == 'Wisconsin').one()
    wisconsin = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='Midwest', college_id=Wisconsin.id)
    db.session.add(wisconsin)

    Colgate = College.query.filter(
        College.name == 'Colgate').one()
    colgate = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='Midwest', college_id=Colgate.id)
    db.session.add(colgate)

    USC = College.query.filter(College.name == 'USC').one()
    uSC = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='Midwest', college_id=USC.id)
    db.session.add(uSC)

    Miami = College.query.filter(College.name == 'Miami').one()
    miami = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='Midwest', college_id=Miami.id)
    db.session.add(miami)

    Auburn = College.query.filter(College.name == 'Auburn').one()
    auburn = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='Midwest', college_id=Auburn.id)
    db.session.add(auburn)

    Jacksonville_State = College.query.filter(
        College.name == 'Jacksonville State').one()
    jacksonville_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='Midwest', college_id=Jacksonville_State.id)
    db.session.add(jacksonville_State)


    db.session.commit()

    game_1 = Game(game_num=1, round_num=1, winning_team_id=None,
                  tournament_id=tournament.id)
    db.session.add(game_1)
    game_2 = Game(game_num=2, round_num=1, winning_team_id=None,
                  tournament_id=tournament.id)
    db.session.add(game_2)
    game_3 = Game(game_num=3, round_num=1, winning_team_id=None,
                  tournament_id=tournament.id)
    db.session.add(game_3)
    game_4 = Game(game_num=4, round_num=1, winning_team_id=None,
                  tournament_id=tournament.id)
    db.session.add(game_4)
    game_5 = Game(game_num=5, round_num=1, winning_team_id=None,
                  tournament_id=tournament.id)
    db.session.add(game_5)
    game_6 = Game(game_num=6, round_num=1, winning_team_id=None,
                  tournament_id=tournament.id)
    db.session.add(game_6)
    game_7 = Game(game_num=7, round_num=1, winning_team_id=None,
                  tournament_id=tournament.id)
    db.session.add(game_7)
    game_8 = Game(game_num=8, round_num=1, winning_team_id=None,
                  tournament_id=tournament.id)
    db.session.add(game_8)
    game_9 = Game(game_num=9, round_num=1, winning_team_id=None,
                  tournament_id=tournament.id)
    db.session.add(game_9)
    game_10 = Game(game_num=10, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_10)
    game_11 = Game(game_num=11, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_11)
    game_12 = Game(game_num=12, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_12)
    game_13 = Game(game_num=13, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_13)
    game_14 = Game(game_num=14, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_14)
    game_15 = Game(game_num=15, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_15)
    game_16 = Game(game_num=16, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_16)
    game_17 = Game(game_num=17, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_17)
    game_18 = Game(game_num=18, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_18)
    game_19 = Game(game_num=19, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_19)
    game_20 = Game(game_num=20, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_20)
    game_21 = Game(game_num=21, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_21)
    game_22 = Game(game_num=22, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_22)
    game_23 = Game(game_num=23, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_23)
    game_24 = Game(game_num=24, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_24)
    game_25 = Game(game_num=25, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_25)
    game_26 = Game(game_num=26, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_26)
    game_27 = Game(game_num=27, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_27)
    game_28 = Game(game_num=28, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_28)
    game_29 = Game(game_num=29, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_29)
    game_30 = Game(game_num=30, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_30)
    game_31 = Game(game_num=31, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_31)
    game_32 = Game(game_num=32, round_num=1,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_32)

    db.session.commit()

    game_1_win_score = Game_Team_Score(
        game_id=game_1.id, team_id=gonzaga.id, score=None)
    game_1_lose_score = Game_Team_Score(
        game_id=game_1.id, team_id=georgia_State.id, score=None)
    game_1.game_team_scores = [game_1_win_score, game_1_lose_score]

    game_2_win_score = Game_Team_Score(
        game_id=game_2.id, team_id=boise_State.id, score=None)
    game_2_lose_score = Game_Team_Score(
        game_id=game_2.id, team_id=memphis.id, score=None)
    game_2.game_team_scores = [game_2_win_score, game_2_lose_score]

    game_3_win_score = Game_Team_Score(
        game_id=game_3.id, team_id=uCONN.id, score=None)
    game_3_lose_score = Game_Team_Score(
        game_id=game_3.id, team_id=nMSU.id, score=None)
    game_3.game_team_scores = [game_3_win_score, game_3_lose_score]

    game_4_win_score = Game_Team_Score(
        game_id=game_4.id, team_id=arkansas.id, score=None)
    game_4_lose_score = Game_Team_Score(
        game_id=game_4.id, team_id=vermont.id, score=None)
    game_4.game_team_scores = [game_4_win_score, game_4_lose_score]

    game_5_win_score = Game_Team_Score(
        game_id=game_5.id, team_id=alabama.id, score=None)
    game_5_lose_score = Game_Team_Score(
        game_id=game_5.id, team_id=rutgers.id, score=None)
    game_5.game_team_scores = [game_5_win_score, game_5_lose_score]

    game_6_win_score = Game_Team_Score(
        game_id=game_6.id, team_id=texas_Tech.id, score=None)
    game_6_lose_score = Game_Team_Score(
        game_id=game_6.id, team_id=montana_State.id, score=None)
    game_6.game_team_scores = [game_6_win_score, game_6_lose_score]

    game_7_win_score = Game_Team_Score(
        game_id=game_7.id, team_id=michigan_State.id, score=None)
    game_7_lose_score = Game_Team_Score(
        game_id=game_7.id, team_id=davidson.id, score=None)
    game_7.game_team_scores = [game_7_win_score, game_7_lose_score]

    game_8_win_score = Game_Team_Score(
        game_id=game_8.id, team_id=duke.id, score=None)
    game_8_lose_score = Game_Team_Score(
        game_id=game_8.id, team_id=cal_State_Fullerton.id, score=None)
    game_8.game_team_scores = [game_8_win_score, game_8_lose_score]

    game_9_win_score = Game_Team_Score(
        game_id=game_9.id, team_id=baylor.id, score=None)
    game_9_lose_score = Game_Team_Score(
        game_id=game_9.id, team_id=norfolk_State.id, score=None)
    game_9.game_team_scores = [game_9_win_score, game_9_lose_score]

    game_10_win_score = Game_Team_Score(
        game_id=game_10.id, team_id=north_Carolina.id, score=None)
    game_10_lose_score = Game_Team_Score(
        game_id=game_10.id, team_id=marquette.id, score=None)
    game_10.game_team_scores = [game_10_win_score, game_10_lose_score]

    game_11_win_score = Game_Team_Score(
        game_id=game_11.id, team_id=saint_Marys.id, score=None)
    game_11_lose_score = Game_Team_Score(
        game_id=game_11.id, team_id=indiana.id, score=None)
    game_11.game_team_scores = [game_11_win_score, game_11_lose_score]

    game_12_win_score = Game_Team_Score(
        game_id=game_12.id, team_id=uCLA.id, score=None)
    game_12_lose_score = Game_Team_Score(
        game_id=game_12.id, team_id=akron.id, score=None)
    game_12.game_team_scores = [game_12_win_score, game_12_lose_score]

    game_13_win_score = Game_Team_Score(
        game_id=game_13.id, team_id=texas.id, score=None)
    game_13_lose_score = Game_Team_Score(
        game_id=game_13.id, team_id=virginia_Tech.id, score=None)
    game_13.game_team_scores = [game_13_win_score, game_13_lose_score]

    game_14_win_score = Game_Team_Score(
        game_id=game_14.id, team_id=purdue.id, score=None)
    game_14_lose_score = Game_Team_Score(
        game_id=game_14.id, team_id=yale.id, score=None)
    game_14.game_team_scores = [game_14_win_score, game_14_lose_score]

    game_15_win_score = Game_Team_Score(
        game_id=game_15.id, team_id=murray_State.id, score=None)
    game_15_lose_score = Game_Team_Score(
        game_id=game_15.id, team_id=san_Francisco.id, score=None)
    game_15.game_team_scores = [game_15_win_score, game_15_lose_score]

    game_16_win_score = Game_Team_Score(
        game_id=game_16.id, team_id=kentucky.id, score=None)
    game_16_lose_score = Game_Team_Score(
        game_id=game_16.id, team_id=saint_Peters.id, score=None)
    game_16.game_team_scores = [game_16_win_score, game_16_lose_score]

    game_17_win_score = Game_Team_Score(
        game_id=game_17.id, team_id=arizona.id, score=None)
    game_17_lose_score = Game_Team_Score(
        game_id=game_17.id, team_id=wright_State.id, score=None)
    game_17.game_team_scores = [game_17_win_score, game_17_lose_score]

    game_18_win_score = Game_Team_Score(
        game_id=game_18.id, team_id=seton_Hall.id, score=None)
    game_18_lose_score = Game_Team_Score(
        game_id=game_18.id, team_id=tCU.id, score=None)
    game_18.game_team_scores = [game_18_win_score, game_18_lose_score]

    game_19_win_score = Game_Team_Score(
        game_id=game_19.id, team_id=houston.id, score=None)
    game_19_lose_score = Game_Team_Score(
        game_id=game_19.id, team_id=uAB.id, score=None)
    game_19.game_team_scores = [game_19_win_score, game_19_lose_score]

    game_20_win_score = Game_Team_Score(
        game_id=game_20.id, team_id=illinois.id, score=None)
    game_20_lose_score = Game_Team_Score(
        game_id=game_20.id, team_id=chattanooga.id, score=None)
    game_20.game_team_scores = [game_20_win_score, game_20_lose_score]

    game_21_win_score = Game_Team_Score(
        game_id=game_21.id, team_id=colorado_State.id, score=None)
    game_21_lose_score = Game_Team_Score(
        game_id=game_21.id, team_id=michigan.id, score=None)
    game_21.game_team_scores = [game_21_win_score, game_21_lose_score]

    game_22_win_score = Game_Team_Score(
        game_id=game_22.id, team_id=tennessee.id, score=None)
    game_22_lose_score = Game_Team_Score(
        game_id=game_22.id, team_id=longwood.id, score=None)
    game_22.game_team_scores = [game_22_win_score, game_22_lose_score]

    game_23_win_score = Game_Team_Score(
        game_id=game_23.id, team_id=ohio_State.id, score=None)
    game_23_lose_score = Game_Team_Score(
        game_id=game_23.id, team_id=loyola_Chicago.id, score=None)
    game_23.game_team_scores = [game_23_win_score, game_23_lose_score]

    game_24_win_score = Game_Team_Score(
        game_id=game_24.id, team_id=villanova.id, score=None)
    game_24_lose_score = Game_Team_Score(
        game_id=game_24.id, team_id=delaware.id, score=None)
    game_24.game_team_scores = [game_24_win_score, game_24_lose_score]

    game_25_win_score = Game_Team_Score(
        game_id=game_25.id, team_id=kansas.id, score=None)
    game_25_lose_score = Game_Team_Score(
        game_id=game_25.id, team_id=texas_Southern.id, score=None)
    game_25.game_team_scores = [game_25_win_score, game_25_lose_score]

    game_26_win_score = Game_Team_Score(
        game_id=game_26.id, team_id=san_Diego_State.id, score=None)
    game_26_lose_score = Game_Team_Score(
        game_id=game_26.id, team_id=creighton.id, score=None)
    game_26.game_team_scores = [game_26_win_score, game_26_lose_score]

    game_27_win_score = Game_Team_Score(
        game_id=game_27.id, team_id=iowa.id, score=None)
    game_27_lose_score = Game_Team_Score(
        game_id=game_27.id, team_id=richmond.id, score=None)
    game_27.game_team_scores = [game_27_win_score, game_27_lose_score]

    game_28_win_score = Game_Team_Score(
        game_id=game_28.id, team_id=providence.id, score=None)
    game_28_lose_score = Game_Team_Score(
        game_id=game_28.id, team_id=south_Dakota_State.id, score=None)
    game_28.game_team_scores = [game_28_win_score, game_28_lose_score]

    game_29_win_score = Game_Team_Score(
        game_id=game_29.id, team_id=lSU.id, score=None)
    game_29_lose_score = Game_Team_Score(
        game_id=game_29.id, team_id=iowa_State.id, score=None)
    game_29.game_team_scores = [game_29_win_score, game_29_lose_score]

    game_30_win_score = Game_Team_Score(
        game_id=game_30.id, team_id=wisconsin.id, score=None)
    game_30_lose_score = Game_Team_Score(
        game_id=game_30.id, team_id=colgate.id, score=None)
    game_30.game_team_scores = [game_30_win_score, game_30_lose_score]

    game_31_win_score = Game_Team_Score(
        game_id=game_31.id, team_id=uSC.id, score=None)
    game_31_lose_score = Game_Team_Score(
        game_id=game_31.id, team_id=miami.id, score=None)
    game_31.game_team_scores = [game_31_win_score, game_31_lose_score]

    game_32_win_score = Game_Team_Score(
        game_id=game_32.id, team_id=auburn.id, score=None)
    game_32_lose_score = Game_Team_Score(
        game_id=game_32.id, team_id=jacksonville_State.id, score=None)
    game_32.game_team_scores = [game_32_win_score, game_32_lose_score]

    db.session.commit()


def undo_2022_tournament():
    tournament = Tournament.query.filter(Tournament.year == 2022).one()

    db.session.execute(
        '''DELETE from game_team_scores WHERE game_id in(
          SELECT id FROM games WHERE tournament_id = :id
        )''', {'id': tournament.id})
    db.session.execute(
        'DELETE from games WHERE tournament_id = :id', {'id': tournament.id})
    db.session.execute(
        '''DELETE from drafted_teams WHERE march_madness_team_id in(
          SELECT id FROM march_madness_teams WHERE tournament_id = :id
        )''', {'id': tournament.id})
    db.session.execute(
        'DELETE from drafts WHERE tournament_id = :id', {'id': tournament.id})
    db.session.execute(
        'DELETE from march_madness_teams WHERE tournament_id = :id', {'id': tournament.id})
    db.session.execute(
        'DELETE from march_madness_teams WHERE tournament_id = :id', {'id': tournament.id})
    db.session.execute(
        'DELETE from tournaments WHERE id = :id', {'id': tournament.id})
    db.session.commit()
