from app.models import db, March_Madness_Team, College, Game, Game_Team_Score, League, League_User, Draft, Drafted_Team, User, Tournament
import json
from datetime import datetime


def seed_draft_2019():
    tournament = Tournament(year=2019, region1='South',
                            region2='West', region3='East', region4='Midwest')
    db.session.add(tournament)
    db.session.commit()

    Alabama = College.query.filter(College.name == 'Alabama').one()
    alabama = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='East', college_id=Alabama.id)
    db.session.add(alabama)

    Arizona = College.query.filter(College.name == 'Arizona').one()
    arizona = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='South', college_id=Arizona.id)
    db.session.add(arizona)

    Arkansas = College.query.filter(College.name == 'Arkansas').one()
    arkansas = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='East', college_id=Arkansas.id)
    db.session.add(arkansas)

    Syracuse = College.query.filter(College.name == 'Syracuse').one()
    syracuse = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='Midwest', college_id=Syracuse.id)
    db.session.add(syracuse)

    Auburn = College.query.filter(College.name == 'Auburn').one()
    auburn = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='Midwest', college_id=Auburn.id)
    db.session.add(auburn)

    Bucknell = College.query.filter(College.name == 'Bucknell').one()
    bucknell = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='Midwest', college_id=Bucknell.id)
    db.session.add(bucknell)

    Buffalo = College.query.filter(College.name == 'Buffalo').one()
    buffalo = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='South', college_id=Buffalo.id)
    db.session.add(buffalo)

    Butler = College.query.filter(College.name == 'Butler').one()
    butler = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='East', college_id=Butler.id)
    db.session.add(butler)

    Cal_State_Fullerton = College.query.filter(
        College.name == 'Cal State Fullerton').one()
    cal_State_Fullerton = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='East', college_id=Cal_State_Fullerton.id)
    db.session.add(cal_State_Fullerton)

    Charleston = College.query.filter(College.name == 'Charleston').one()
    charleston = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='Midwest', college_id=Charleston.id)
    db.session.add(charleston)

    Cincinnati = College.query.filter(College.name == 'Cincinnati').one()
    cincinnati = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='South', college_id=Cincinnati.id)
    db.session.add(cincinnati)

    Clemson = College.query.filter(College.name == 'Clemson').one()
    clemson = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='Midwest', college_id=Clemson.id)
    db.session.add(clemson)

    Creighton = College.query.filter(College.name == 'Creighton').one()
    creighton = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='South', college_id=Creighton.id)
    db.session.add(creighton)

    Davidson = College.query.filter(College.name == 'Davidson').one()
    davidson = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='South', college_id=Davidson.id)
    db.session.add(davidson)

    Duke = College.query.filter(College.name == 'Duke').one()
    duke = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='Midwest', college_id=Duke.id)
    db.session.add(duke)

    Florida_State = College.query.filter(College.name == 'Florida State').one()
    florida_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='West', college_id=Florida_State.id)
    db.session.add(florida_State)

    Florida = College.query.filter(College.name == 'Florida').one()
    florida = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='East', college_id=Florida.id)
    db.session.add(florida)

    Georgia_State = College.query.filter(College.name == 'Georgia State').one()
    georgia_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='South', college_id=Georgia_State.id)
    db.session.add(georgia_State)

    Gonzaga = College.query.filter(College.name == 'Gonzaga').one()
    gonzaga = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='West', college_id=Gonzaga.id)
    db.session.add(gonzaga)

    Houston = College.query.filter(College.name == 'Houston').one()
    houston = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='West', college_id=Houston.id)
    db.session.add(houston)

    Iona = College.query.filter(College.name == 'Iona').one()
    iona = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='Midwest', college_id=Iona.id)
    db.session.add(iona)

    Kansas_State = College.query.filter(College.name == 'Kansas State').one()
    kansas_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='South', college_id=Kansas_State.id)
    db.session.add(kansas_State)

    Kansas = College.query.filter(College.name == 'Kansas').one()
    kansas = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='Midwest', college_id=Kansas.id)
    db.session.add(kansas)

    Kentucky = College.query.filter(College.name == 'Kentucky').one()
    kentucky = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='South', college_id=Kentucky.id)
    db.session.add(kentucky)

    Lipscomb = College.query.filter(College.name == 'Lipscomb').one()
    lipscomb = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='West', college_id=Lipscomb.id)
    db.session.add(lipscomb)

    Radford = College.query.filter(College.name == 'Radford').one()
    radford = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='East', college_id=Radford.id)
    db.session.add(radford)

    Loyola_Chicago = College.query.filter(
        College.name == 'Loyola Chicago').one()
    loyola_Chicago = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='South', college_id=Loyola_Chicago.id)
    db.session.add(loyola_Chicago)

    Marshall = College.query.filter(College.name == 'Marshall').one()
    marshall = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='East', college_id=Marshall.id)
    db.session.add(marshall)

    Miami = College.query.filter(College.name == 'Miami').one()
    miami = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='South', college_id=Miami.id)
    db.session.add(miami)

    Michigan_State = College.query.filter(
        College.name == 'Michigan State').one()
    michigan_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='Midwest', college_id=Michigan_State.id)
    db.session.add(michigan_State)

    Michigan = College.query.filter(College.name == 'Michigan').one()
    michigan = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='West', college_id=Michigan.id)
    db.session.add(michigan)

    Missouri = College.query.filter(College.name == 'Missouri').one()
    missouri = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='West', college_id=Missouri.id)
    db.session.add(missouri)

    Montana = College.query.filter(College.name == 'Montana').one()
    montana = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='West', college_id=Montana.id)
    db.session.add(montana)

    Murray_State = College.query.filter(College.name == 'Murray State').one()
    murray_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='East', college_id=Murray_State.id)
    db.session.add(murray_State)

    Texas_Southern = College.query.filter(
        College.name == 'Texas Southern').one()
    texas_Southern = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='West', college_id=Texas_Southern.id)
    db.session.add(texas_Southern)

    UNC_Greensboro = College.query.filter(
        College.name == 'UNC Greensboro').one()
    uNC_Greensboro = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='West', college_id=UNC_Greensboro.id)
    db.session.add(uNC_Greensboro)

    Nevada = College.query.filter(College.name == 'Nevada').one()
    nevada = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='South', college_id=Nevada.id)
    db.session.add(nevada)

    New_Mexico_State = College.query.filter(
        College.name == 'New Mexico State').one()
    new_Mexico_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='Midwest', college_id=New_Mexico_State.id)
    db.session.add(new_Mexico_State)

    North_Carolina_State = College.query.filter(
        College.name == 'North Carolina State').one()
    north_Carolina_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='Midwest', college_id=North_Carolina_State.id)
    db.session.add(north_Carolina_State)

    North_Carolina = College.query.filter(
        College.name == 'North Carolina').one()
    north_Carolina = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='West', college_id=North_Carolina.id)
    db.session.add(north_Carolina)

    Ohio_State = College.query.filter(College.name == 'Ohio State').one()
    ohio_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='West', college_id=Ohio_State.id)
    db.session.add(ohio_State)

    Oklahoma = College.query.filter(College.name == 'Oklahoma').one()
    oklahoma = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='Midwest', college_id=Oklahoma.id)
    db.session.add(oklahoma)

    Penn = College.query.filter(College.name == 'Penn').one()
    penn = March_Madness_Team(tournament_id=tournament.id,
                              seed_number=16, region='Midwest', college_id=Penn.id)
    db.session.add(penn)

    Providence = College.query.filter(College.name == 'Providence').one()
    providence = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='West', college_id=Providence.id)
    db.session.add(providence)

    Purdue = College.query.filter(College.name == 'Purdue').one()
    purdue = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='East', college_id=Purdue.id)
    db.session.add(purdue)

    Rhode_Island = College.query.filter(College.name == 'Rhode Island').one()
    rhode_Island = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='Midwest', college_id=Rhode_Island.id)
    db.session.add(rhode_Island)

    San_Diego_State = College.query.filter(
        College.name == 'San Diego State').one()
    san_Diego_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='West', college_id=San_Diego_State.id)
    db.session.add(san_Diego_State)

    Seton_Hall = College.query.filter(College.name == 'Seton Hall').one()
    seton_Hall = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='Midwest', college_id=Seton_Hall.id)
    db.session.add(seton_Hall)

    South_Dakota_State = College.query.filter(
        College.name == 'South Dakota State').one()
    south_Dakota_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='West', college_id=South_Dakota_State.id)
    db.session.add(south_Dakota_State)

    St_Bonaventure = College.query.filter(
        College.name == 'St. Bonaventure').one()
    st_Bonaventure = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='East', college_id=St_Bonaventure.id)
    db.session.add(st_Bonaventure)

    Stephen_F_Austin = College.query.filter(
        College.name == 'Stephen F. Austin').one()
    stephen_F_Austin = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='East', college_id=Stephen_F_Austin.id)
    db.session.add(stephen_F_Austin)

    TCU = College.query.filter(College.name == 'TCU').one()
    tCU = March_Madness_Team(tournament_id=tournament.id,
                             seed_number=6, region='Midwest', college_id=TCU.id)
    db.session.add(tCU)

    Tennessee = College.query.filter(College.name == 'Tennessee').one()
    tennessee = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='South', college_id=Tennessee.id)
    db.session.add(tennessee)

    Texas_AM = College.query.filter(College.name == 'Texas A&M').one()
    texas_AM = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='West', college_id=Texas_AM.id)
    db.session.add(texas_AM)

    Texas_Tech = College.query.filter(College.name == 'Texas Tech').one()
    texas_Tech = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='East', college_id=Texas_Tech.id)
    db.session.add(texas_Tech)

    Texas = College.query.filter(College.name == 'Texas').one()
    texas = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='South', college_id=Texas.id)
    db.session.add(texas)

    UMBC = College.query.filter(College.name == 'UMBC').one()
    uMBC = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='South', college_id=UMBC.id)
    db.session.add(uMBC)

    Villanova = College.query.filter(College.name == 'Villanova').one()
    villanova = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='East',  college_id=Villanova.id)
    db.session.add(villanova)

    Virginia_Tech = College.query.filter(College.name == 'Virginia Tech').one()
    virginia_Tech = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='East', college_id=Virginia_Tech.id)
    db.session.add(virginia_Tech)

    Virginia = College.query.filter(College.name == 'Virginia').one()
    virginia = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='South', college_id=Virginia.id)
    db.session.add(virginia)

    West_Virginia = College.query.filter(College.name == 'West Virginia').one()
    west_Virginia = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='East', college_id=West_Virginia.id)
    db.session.add(west_Virginia)

    Wichita_State = College.query.filter(College.name == 'Wichita State').one()
    wichita_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='East', college_id=Wichita_State.id)
    db.session.add(wichita_State)

    Wright_State = College.query.filter(College.name == 'Wright State').one()
    wright_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='South', college_id=Wright_State.id)
    db.session.add(wright_State)

    Xavier = College.query.filter(College.name == 'Xavier').one()
    xavier = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='West', college_id=Xavier.id)
    db.session.add(xavier)

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
        game_id=game_1.id, team_id=uMBC.id)
    game_1_lose_score = Game_Team_Score(
        game_id=game_1.id, team_id=virginia.id)
    game_1.game_team_scores = [game_1_win_score, game_1_lose_score]

    game_2_win_score = Game_Team_Score(
        game_id=game_2.id, team_id=kansas_State.id)
    game_2_lose_score = Game_Team_Score(
        game_id=game_2.id, team_id=creighton.id)
    game_2.game_team_scores = [game_2_win_score, game_2_lose_score]

    game_3_win_score = Game_Team_Score(
        game_id=game_3.id, team_id=kentucky.id)
    game_3_lose_score = Game_Team_Score(
        game_id=game_3.id, team_id=davidson.id)
    game_3.game_team_scores = [game_3_win_score, game_3_lose_score]

    game_4_win_score = Game_Team_Score(
        game_id=game_4.id, team_id=buffalo.id)
    game_4_lose_score = Game_Team_Score(
        game_id=game_4.id, team_id=arizona.id)
    game_4.game_team_scores = [game_4_win_score, game_4_lose_score]

    game_5_win_score = Game_Team_Score(
        game_id=game_5.id, team_id=loyola_Chicago.id)
    game_5_lose_score = Game_Team_Score(
        game_id=game_5.id, team_id=miami.id)
    game_5.game_team_scores = [game_5_win_score, game_5_lose_score]

    game_6_win_score = Game_Team_Score(
        game_id=game_6.id, team_id=tennessee.id)
    game_6_lose_score = Game_Team_Score(
        game_id=game_6.id, team_id=wright_State.id)
    game_6.game_team_scores = [game_6_win_score, game_6_lose_score]

    game_7_win_score = Game_Team_Score(
        game_id=game_7.id, team_id=nevada.id)
    game_7_lose_score = Game_Team_Score(
        game_id=game_7.id, team_id=texas.id)
    game_7.game_team_scores = [game_7_win_score, game_7_lose_score]

    game_8_win_score = Game_Team_Score(
        game_id=game_8.id, team_id=cincinnati.id)
    game_8_lose_score = Game_Team_Score(
        game_id=game_8.id, team_id=georgia_State.id)
    game_8.game_team_scores = [game_8_win_score, game_8_lose_score]

    game_9_win_score = Game_Team_Score(
        game_id=game_9.id, team_id=xavier.id)
    game_9_lose_score = Game_Team_Score(
        game_id=game_9.id, team_id=texas_Southern.id)
    game_9.game_team_scores = [game_9_win_score, game_9_lose_score]

    game_10_win_score = Game_Team_Score(
        game_id=game_10.id, team_id=florida_State.id)
    game_10_lose_score = Game_Team_Score(
        game_id=game_10.id, team_id=missouri.id)
    game_10.game_team_scores = [game_10_win_score, game_10_lose_score]

    game_11_win_score = Game_Team_Score(
        game_id=game_11.id, team_id=ohio_State.id)
    game_11_lose_score = Game_Team_Score(
        game_id=game_11.id, team_id=south_Dakota_State.id)
    game_11.game_team_scores = [game_11_win_score, game_11_lose_score]

    game_12_win_score = Game_Team_Score(
        game_id=game_12.id, team_id=gonzaga.id)
    game_12_lose_score = Game_Team_Score(
        game_id=game_12.id, team_id=uNC_Greensboro.id)
    game_12.game_team_scores = [game_12_win_score, game_12_lose_score]

    game_13_win_score = Game_Team_Score(
        game_id=game_13.id, team_id=houston.id)
    game_13_lose_score = Game_Team_Score(
        game_id=game_13.id, team_id=san_Diego_State.id)
    game_13.game_team_scores = [game_13_win_score, game_13_lose_score]

    game_14_win_score = Game_Team_Score(
        game_id=game_14.id, team_id=michigan.id)
    game_14_lose_score = Game_Team_Score(
        game_id=game_14.id, team_id=montana.id)
    game_14.game_team_scores = [game_14_win_score, game_14_lose_score]

    game_15_win_score = Game_Team_Score(
        game_id=game_15.id, team_id=texas_AM.id)
    game_15_lose_score = Game_Team_Score(
        game_id=game_15.id, team_id=providence.id)
    game_15.game_team_scores = [game_15_win_score, game_15_lose_score]

    game_16_win_score = Game_Team_Score(
        game_id=game_16.id, team_id=north_Carolina.id)
    game_16_lose_score = Game_Team_Score(
        game_id=game_16.id, team_id=lipscomb.id)
    game_16.game_team_scores = [game_16_win_score, game_16_lose_score]

    game_17_win_score = Game_Team_Score(
        game_id=game_17.id, team_id=villanova.id)
    game_17_lose_score = Game_Team_Score(
        game_id=game_17.id, team_id=radford.id)
    game_17.game_team_scores = [game_17_win_score, game_17_lose_score]

    game_18_win_score = Game_Team_Score(
        game_id=game_18.id, team_id=alabama.id)
    game_18_lose_score = Game_Team_Score(
        game_id=game_18.id, team_id=virginia_Tech.id)
    game_18.game_team_scores = [game_18_win_score, game_18_lose_score]

    game_19_win_score = Game_Team_Score(
        game_id=game_19.id, team_id=west_Virginia.id)
    game_19_lose_score = Game_Team_Score(
        game_id=game_19.id, team_id=murray_State.id)
    game_19.game_team_scores = [game_19_win_score, game_19_lose_score]

    game_20_win_score = Game_Team_Score(
        game_id=game_20.id, team_id=marshall.id)
    game_20_lose_score = Game_Team_Score(
        game_id=game_20.id, team_id=wichita_State.id)
    game_20.game_team_scores = [game_20_win_score, game_20_lose_score]

    game_21_win_score = Game_Team_Score(
        game_id=game_21.id, team_id=florida.id)
    game_21_lose_score = Game_Team_Score(
        game_id=game_21.id, team_id=st_Bonaventure.id)
    game_21.game_team_scores = [game_21_win_score, game_21_lose_score]

    game_22_win_score = Game_Team_Score(
        game_id=game_22.id, team_id=texas_Tech.id)
    game_22_lose_score = Game_Team_Score(
        game_id=game_22.id, team_id=stephen_F_Austin.id)
    game_22.game_team_scores = [game_22_win_score, game_22_lose_score]

    game_23_win_score = Game_Team_Score(
        game_id=game_23.id, team_id=butler.id)
    game_23_lose_score = Game_Team_Score(
        game_id=game_23.id, team_id=arkansas.id)
    game_23.game_team_scores = [game_23_win_score, game_23_lose_score]

    game_24_win_score = Game_Team_Score(
        game_id=game_24.id, team_id=purdue.id)
    game_24_lose_score = Game_Team_Score(
        game_id=game_24.id, team_id=cal_State_Fullerton.id)
    game_24.game_team_scores = [game_24_win_score, game_24_lose_score]

    game_25_win_score = Game_Team_Score(
        game_id=game_25.id, team_id=kansas.id)
    game_25_lose_score = Game_Team_Score(
        game_id=game_25.id, team_id=penn.id)
    game_25.game_team_scores = [game_25_win_score, game_25_lose_score]

    game_26_win_score = Game_Team_Score(
        game_id=game_26.id, team_id=seton_Hall.id)
    game_26_lose_score = Game_Team_Score(
        game_id=game_26.id, team_id=north_Carolina_State.id)
    game_26.game_team_scores = [game_26_win_score, game_26_lose_score]

    game_27_win_score = Game_Team_Score(
        game_id=game_27.id, team_id=clemson.id)
    game_27_lose_score = Game_Team_Score(
        game_id=game_27.id, team_id=new_Mexico_State.id)
    game_27.game_team_scores = [game_27_win_score, game_27_lose_score]

    game_28_win_score = Game_Team_Score(
        game_id=game_28.id, team_id=auburn.id)
    game_28_lose_score = Game_Team_Score(
        game_id=game_28.id, team_id=charleston.id)
    game_28.game_team_scores = [game_28_win_score, game_28_lose_score]

    game_29_win_score = Game_Team_Score(
        game_id=game_29.id, team_id=syracuse.id)
    game_29_lose_score = Game_Team_Score(
        game_id=game_29.id, team_id=tCU.id)
    game_29.game_team_scores = [game_29_win_score, game_29_lose_score]

    game_30_win_score = Game_Team_Score(
        game_id=game_30.id, team_id=michigan_State.id)
    game_30_lose_score = Game_Team_Score(
        game_id=game_30.id, team_id=bucknell.id)
    game_30.game_team_scores = [game_30_win_score, game_30_lose_score]

    game_31_win_score = Game_Team_Score(
        game_id=game_31.id, team_id=rhode_Island.id)
    game_31_lose_score = Game_Team_Score(
        game_id=game_31.id, team_id=oklahoma.id)
    game_31.game_team_scores = [game_31_win_score, game_31_lose_score]

    game_32_win_score = Game_Team_Score(
        game_id=game_32.id, team_id=duke.id)
    game_32_lose_score = Game_Team_Score(
        game_id=game_32.id, team_id=iona.id)
    game_32.game_team_scores = [game_32_win_score, game_32_lose_score]

    db.session.commit()

    league = League.query.filter(
        League.name == 'The League of Extraordinary Gentlemen').one()
    lu_ids = {lu.user.name: lu.id for lu in league.league_users}
    draft_order = [
        lu_ids['Will'],
        lu_ids['Ryan'],
        lu_ids['Chase'],
        lu_ids['DemoDraft'],
        lu_ids['Mitch'],
        lu_ids['TJ'],
        lu_ids['Patrick'],
        lu_ids['Isaac'],
        lu_ids['Isaac'],
        lu_ids['Patrick'],
        lu_ids['TJ'],
        lu_ids['Mitch'],
        lu_ids['DemoDraft'],
        lu_ids['Chase'],
        lu_ids['Ryan'],
        lu_ids['Will'],
        lu_ids['Patrick'],
        lu_ids['Mitch'],
        lu_ids['Chase'],
        lu_ids['Will'],
        lu_ids['Ryan'],
        lu_ids['DemoDraft'],
        lu_ids['Isaac'],
        lu_ids['TJ'],
        lu_ids['TJ'],
        lu_ids['Isaac'],
        lu_ids['DemoDraft'],
        lu_ids['Ryan'],
        lu_ids['Will'],
        lu_ids['Chase'],
        lu_ids['Mitch'],
        lu_ids['Patrick'],
        lu_ids['Patrick'],
        lu_ids['Chase'],
        lu_ids['Isaac'],
        lu_ids['Ryan'],
        lu_ids['DemoDraft'],
        lu_ids['Will'],
        lu_ids['Mitch'],
        lu_ids['TJ'],
        lu_ids['TJ'],
        lu_ids['Mitch'],
        lu_ids['Will'],
        lu_ids['DemoDraft'],
        lu_ids['Ryan'],
        lu_ids['Isaac'],
        lu_ids['Chase'],
        lu_ids['Patrick'],
        lu_ids['Will'],
        lu_ids['DemoDraft'],
        lu_ids['Patrick'],
        lu_ids['Mitch'],
        lu_ids['Ryan'],
        lu_ids['TJ'],
        lu_ids['Isaac'],
        lu_ids['Chase'],
        lu_ids['Chase'],
        lu_ids['Isaac'],
        lu_ids['TJ'],
        lu_ids['Ryan'],
        lu_ids['Mitch'],
        lu_ids['Patrick'],
        lu_ids['DemoDraft'],
        lu_ids['Will'],
    ]

    draft = Draft(league_id=league.id,
                  tournament_id=tournament.id, draft_order=json.dumps(draft_order), draft_index=0,
                  draft_time=datetime.now(), drafting=True, current_drafter_id=lu_ids['Will'],
                  time_limit_mins=None)
    db.session.add(draft)
    db.session.commit()

    league = League.query.filter(
        League.name == 'The Dumb Friends League').one()
    lu_ids = {lu.user.name: lu.id for lu in league.league_users}
    draft_order = [
        lu_ids['Will'],
        lu_ids['Ryan'],
        lu_ids['DemoDraft'],
        lu_ids['Demo'],
        lu_ids['Mitch'],
        lu_ids['TJ'],
        lu_ids['Patrick'],
        lu_ids['Isaac'],
        lu_ids['Isaac'],
        lu_ids['Patrick'],
        lu_ids['TJ'],
        lu_ids['Mitch'],
        lu_ids['Demo'],
        lu_ids['DemoDraft'],
        lu_ids['Ryan'],
        lu_ids['Will'],
        lu_ids['Patrick'],
        lu_ids['Mitch'],
        lu_ids['DemoDraft'],
        lu_ids['Will'],
        lu_ids['Ryan'],
        lu_ids['Demo'],
        lu_ids['Isaac'],
        lu_ids['TJ'],
        lu_ids['TJ'],
        lu_ids['Isaac'],
        lu_ids['Demo'],
        lu_ids['Ryan'],
        lu_ids['Will'],
        lu_ids['DemoDraft'],
        lu_ids['Mitch'],
        lu_ids['Patrick'],
        lu_ids['Patrick'],
        lu_ids['DemoDraft'],
        lu_ids['Isaac'],
        lu_ids['Ryan'],
        lu_ids['Demo'],
        lu_ids['Will'],
        lu_ids['Mitch'],
        lu_ids['TJ'],
        lu_ids['TJ'],
        lu_ids['Mitch'],
        lu_ids['Will'],
        lu_ids['Demo'],
        lu_ids['Ryan'],
        lu_ids['Isaac'],
        lu_ids['DemoDraft'],
        lu_ids['Patrick'],
        lu_ids['Will'],
        lu_ids['Demo'],
        lu_ids['Patrick'],
        lu_ids['Mitch'],
        lu_ids['Ryan'],
        lu_ids['TJ'],
        lu_ids['Isaac'],
        lu_ids['DemoDraft'],
        lu_ids['DemoDraft'],
        lu_ids['Isaac'],
        lu_ids['TJ'],
        lu_ids['Ryan'],
        lu_ids['Mitch'],
        lu_ids['Patrick'],
        lu_ids['Demo'],
        lu_ids['Will'],
    ]

    draft = Draft(league_id=league.id,
                  tournament_id=tournament.id, draft_order=json.dumps(draft_order), draft_index=64,
                  draft_time=datetime.now(), drafting=False, current_drafter_id=lu_ids['Will'],
                  time_limit_mins=None)
    db.session.add(draft)
    db.session.commit()

    pick_1 = Drafted_Team(march_madness_team_id=virginia.id,
                          league_user_id=draft_order[0], draft_id=draft.id, selection_num=1)
    pick_2 = Drafted_Team(march_madness_team_id=michigan_State.id,
                          league_user_id=draft_order[1], draft_id=draft.id, selection_num=2)
    pick_3 = Drafted_Team(march_madness_team_id=duke.id,
                          league_user_id=draft_order[2], draft_id=draft.id, selection_num=3)
    pick_4 = Drafted_Team(march_madness_team_id=villanova.id,
                          league_user_id=draft_order[3], draft_id=draft.id, selection_num=4)
    pick_5 = Drafted_Team(march_madness_team_id=purdue.id,
                          league_user_id=draft_order[4], draft_id=draft.id, selection_num=5)
    pick_6 = Drafted_Team(march_madness_team_id=xavier.id,
                          league_user_id=draft_order[5], draft_id=draft.id, selection_num=6)
    pick_7 = Drafted_Team(march_madness_team_id=north_Carolina.id,
                          league_user_id=draft_order[6], draft_id=draft.id, selection_num=7)
    pick_8 = Drafted_Team(march_madness_team_id=cincinnati.id,
                          league_user_id=draft_order[7], draft_id=draft.id, selection_num=8)
    pick_9 = Drafted_Team(march_madness_team_id=gonzaga.id,
                          league_user_id=draft_order[8], draft_id=draft.id, selection_num=9)
    pick_10 = Drafted_Team(march_madness_team_id=michigan.id,
                           league_user_id=draft_order[9], draft_id=draft.id, selection_num=10)
    pick_11 = Drafted_Team(march_madness_team_id=tennessee.id,
                           league_user_id=draft_order[10], draft_id=draft.id, selection_num=11)
    pick_12 = Drafted_Team(march_madness_team_id=arizona.id,
                           league_user_id=draft_order[11], draft_id=draft.id, selection_num=12)
    pick_13 = Drafted_Team(march_madness_team_id=kansas.id,
                           league_user_id=draft_order[12], draft_id=draft.id, selection_num=13)
    pick_14 = Drafted_Team(march_madness_team_id=texas_Tech.id,
                           league_user_id=draft_order[13], draft_id=draft.id, selection_num=14)
    pick_15 = Drafted_Team(march_madness_team_id=west_Virginia.id,
                           league_user_id=draft_order[14], draft_id=draft.id, selection_num=15)
    pick_16 = Drafted_Team(march_madness_team_id=ohio_State.id,
                           league_user_id=draft_order[15], draft_id=draft.id, selection_num=16)
    pick_17 = Drafted_Team(march_madness_team_id=auburn.id,
                           league_user_id=draft_order[16], draft_id=draft.id, selection_num=17)
    pick_18 = Drafted_Team(march_madness_team_id=florida.id,
                           league_user_id=draft_order[17], draft_id=draft.id, selection_num=18)
    pick_19 = Drafted_Team(march_madness_team_id=wichita_State.id,
                           league_user_id=draft_order[18], draft_id=draft.id, selection_num=19)
    pick_20 = Drafted_Team(march_madness_team_id=kentucky.id,
                           league_user_id=draft_order[19], draft_id=draft.id, selection_num=20)
    pick_21 = Drafted_Team(march_madness_team_id=houston.id,
                           league_user_id=draft_order[20], draft_id=draft.id, selection_num=21)
    pick_22 = Drafted_Team(march_madness_team_id=syracuse.id,
                           league_user_id=draft_order[21], draft_id=draft.id, selection_num=22)
    pick_23 = Drafted_Team(march_madness_team_id=butler.id,
                           league_user_id=draft_order[22], draft_id=draft.id, selection_num=23)
    pick_24 = Drafted_Team(march_madness_team_id=alabama.id,
                           league_user_id=draft_order[23], draft_id=draft.id, selection_num=24)
    pick_25 = Drafted_Team(march_madness_team_id=miami.id,
                           league_user_id=draft_order[24], draft_id=draft.id, selection_num=25)
    pick_26 = Drafted_Team(march_madness_team_id=clemson.id,
                           league_user_id=draft_order[25], draft_id=draft.id, selection_num=26)
    pick_27 = Drafted_Team(march_madness_team_id=st_Bonaventure.id,
                           league_user_id=draft_order[26], draft_id=draft.id, selection_num=27)
    pick_28 = Drafted_Team(march_madness_team_id=loyola_Chicago.id,
                           league_user_id=draft_order[27], draft_id=draft.id, selection_num=28)
    pick_29 = Drafted_Team(march_madness_team_id=rhode_Island.id,
                           league_user_id=draft_order[28], draft_id=draft.id, selection_num=29)
    pick_30 = Drafted_Team(march_madness_team_id=south_Dakota_State.id,
                           league_user_id=draft_order[29], draft_id=draft.id, selection_num=30)
    pick_31 = Drafted_Team(march_madness_team_id=nevada.id,
                           league_user_id=draft_order[30], draft_id=draft.id, selection_num=31)
    pick_32 = Drafted_Team(march_madness_team_id=davidson.id,
                           league_user_id=draft_order[31], draft_id=draft.id, selection_num=32)
    pick_33 = Drafted_Team(march_madness_team_id=stephen_F_Austin.id,
                           league_user_id=draft_order[32], draft_id=draft.id, selection_num=33)
    pick_34 = Drafted_Team(march_madness_team_id=new_Mexico_State.id,
                           league_user_id=draft_order[33], draft_id=draft.id, selection_num=34)
    pick_35 = Drafted_Team(march_madness_team_id=tCU.id,
                           league_user_id=draft_order[34], draft_id=draft.id, selection_num=35)
    pick_36 = Drafted_Team(march_madness_team_id=texas.id,
                           league_user_id=draft_order[35], draft_id=draft.id, selection_num=36)
    pick_37 = Drafted_Team(march_madness_team_id=arkansas.id,
                           league_user_id=draft_order[36], draft_id=draft.id, selection_num=37)
    pick_38 = Drafted_Team(march_madness_team_id=north_Carolina_State.id,
                           league_user_id=draft_order[37], draft_id=draft.id, selection_num=38)
    pick_39 = Drafted_Team(march_madness_team_id=providence.id,
                           league_user_id=draft_order[38], draft_id=draft.id, selection_num=39)
    pick_40 = Drafted_Team(march_madness_team_id=missouri.id,
                           league_user_id=draft_order[39], draft_id=draft.id, selection_num=40)
    pick_41 = Drafted_Team(march_madness_team_id=creighton.id,
                           league_user_id=draft_order[40], draft_id=draft.id, selection_num=41)
    pick_42 = Drafted_Team(march_madness_team_id=florida_State.id,
                           league_user_id=draft_order[41], draft_id=draft.id, selection_num=42)
    pick_43 = Drafted_Team(march_madness_team_id=san_Diego_State.id,
                           league_user_id=draft_order[42], draft_id=draft.id, selection_num=43)
    pick_44 = Drafted_Team(march_madness_team_id=texas_AM.id,
                           league_user_id=draft_order[43], draft_id=draft.id, selection_num=44)
    pick_45 = Drafted_Team(march_madness_team_id=oklahoma.id,
                           league_user_id=draft_order[44], draft_id=draft.id, selection_num=45)
    pick_46 = Drafted_Team(march_madness_team_id=virginia_Tech.id,
                           league_user_id=draft_order[45], draft_id=draft.id, selection_num=46)
    pick_47 = Drafted_Team(march_madness_team_id=kansas_State.id,
                           league_user_id=draft_order[46], draft_id=draft.id, selection_num=47)
    pick_48 = Drafted_Team(march_madness_team_id=seton_Hall.id,
                           league_user_id=draft_order[47], draft_id=draft.id, selection_num=48)
    pick_49 = Drafted_Team(march_madness_team_id=buffalo.id,
                           league_user_id=draft_order[48], draft_id=draft.id, selection_num=49)
    pick_50 = Drafted_Team(march_madness_team_id=uNC_Greensboro.id,
                           league_user_id=draft_order[49], draft_id=draft.id, selection_num=50)
    pick_51 = Drafted_Team(march_madness_team_id=marshall.id,
                           league_user_id=draft_order[50], draft_id=draft.id, selection_num=51)
    pick_52 = Drafted_Team(march_madness_team_id=murray_State.id,
                           league_user_id=draft_order[51], draft_id=draft.id, selection_num=52)
    pick_53 = Drafted_Team(march_madness_team_id=montana.id,
                           league_user_id=draft_order[52], draft_id=draft.id, selection_num=53)
    pick_54 = Drafted_Team(march_madness_team_id=charleston.id,
                           league_user_id=draft_order[53], draft_id=draft.id, selection_num=54)
    pick_55 = Drafted_Team(march_madness_team_id=wright_State.id,
                           league_user_id=draft_order[54], draft_id=draft.id, selection_num=55)
    pick_56 = Drafted_Team(march_madness_team_id=georgia_State.id,
                           league_user_id=draft_order[55], draft_id=draft.id, selection_num=56)
    pick_57 = Drafted_Team(march_madness_team_id=bucknell.id,
                           league_user_id=draft_order[56], draft_id=draft.id, selection_num=57)
    pick_58 = Drafted_Team(march_madness_team_id=penn.id,
                           league_user_id=draft_order[57], draft_id=draft.id, selection_num=58)
    pick_59 = Drafted_Team(march_madness_team_id=iona.id,
                           league_user_id=draft_order[58], draft_id=draft.id, selection_num=59)
    pick_60 = Drafted_Team(march_madness_team_id=cal_State_Fullerton.id,
                           league_user_id=draft_order[59], draft_id=draft.id, selection_num=60)
    pick_61 = Drafted_Team(march_madness_team_id=texas_Southern.id,
                           league_user_id=draft_order[60], draft_id=draft.id, selection_num=61)
    pick_62 = Drafted_Team(march_madness_team_id=radford.id,
                           league_user_id=draft_order[61], draft_id=draft.id, selection_num=62)
    pick_63 = Drafted_Team(march_madness_team_id=lipscomb.id,
                           league_user_id=draft_order[62], draft_id=draft.id, selection_num=63)
    pick_64 = Drafted_Team(march_madness_team_id=uMBC.id,
                           league_user_id=draft_order[63], draft_id=draft.id, selection_num=64)

    db.session.add(pick_1)
    db.session.add(pick_2)
    db.session.add(pick_3)
    db.session.add(pick_4)
    db.session.add(pick_5)
    db.session.add(pick_6)
    db.session.add(pick_7)
    db.session.add(pick_8)
    db.session.add(pick_9)
    db.session.add(pick_10)
    db.session.add(pick_11)
    db.session.add(pick_12)
    db.session.add(pick_13)
    db.session.add(pick_14)
    db.session.add(pick_15)
    db.session.add(pick_16)
    db.session.add(pick_17)
    db.session.add(pick_18)
    db.session.add(pick_19)
    db.session.add(pick_20)
    db.session.add(pick_21)
    db.session.add(pick_22)
    db.session.add(pick_23)
    db.session.add(pick_24)
    db.session.add(pick_25)
    db.session.add(pick_26)
    db.session.add(pick_27)
    db.session.add(pick_28)
    db.session.add(pick_29)
    db.session.add(pick_30)
    db.session.add(pick_31)
    db.session.add(pick_32)
    db.session.add(pick_33)
    db.session.add(pick_34)
    db.session.add(pick_35)
    db.session.add(pick_36)
    db.session.add(pick_37)
    db.session.add(pick_38)
    db.session.add(pick_39)
    db.session.add(pick_40)
    db.session.add(pick_41)
    db.session.add(pick_42)
    db.session.add(pick_43)
    db.session.add(pick_44)
    db.session.add(pick_45)
    db.session.add(pick_46)
    db.session.add(pick_47)
    db.session.add(pick_48)
    db.session.add(pick_49)
    db.session.add(pick_50)
    db.session.add(pick_51)
    db.session.add(pick_52)
    db.session.add(pick_53)
    db.session.add(pick_54)
    db.session.add(pick_55)
    db.session.add(pick_56)
    db.session.add(pick_57)
    db.session.add(pick_58)
    db.session.add(pick_59)
    db.session.add(pick_60)
    db.session.add(pick_61)
    db.session.add(pick_62)
    db.session.add(pick_63)
    db.session.add(pick_64)

    db.session.commit()


def undo_draft_2019():
    db.session.execute(
        'TRUNCATE march_madness_teams RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE games RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE drafts RESTART IDENTITY CASCADE;')
    db.session.commit()
