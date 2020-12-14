from app.models import db, March_Madness_Team, College, Game, Game_Team_Score, League, League_User, Draft, User
import json
from datetime import datetime


def seed_draft_2019():
    Alabama = College.query.filter(College.name == 'Alabama').one()
    alabama = March_Madness_Team(
        year=2019, seed_number=9, region='East', eliminated=True, college_id=Alabama.id)
    db.session.add(alabama)

    Arizona = College.query.filter(College.name == 'Arizona').one()
    arizona = March_Madness_Team(
        year=2019, seed_number=4, region='South', eliminated=True, college_id=Arizona.id)
    db.session.add(arizona)

    Arkansas = College.query.filter(College.name == 'Arkansas').one()
    arkansas = March_Madness_Team(
        year=2019, seed_number=7, region='East', eliminated=True, college_id=Arkansas.id)
    db.session.add(arkansas)

    Syracuse = College.query.filter(College.name == 'Syracuse').one()
    syracuse = March_Madness_Team(
        year=2019, seed_number=11, region='Midwest', eliminated=True, college_id=Syracuse.id)
    db.session.add(syracuse)

    Auburn = College.query.filter(College.name == 'Auburn').one()
    auburn = March_Madness_Team(
        year=2019, seed_number=4, region='Midwest', eliminated=True, college_id=Auburn.id)
    db.session.add(auburn)

    Bucknell = College.query.filter(College.name == 'Bucknell').one()
    bucknell = March_Madness_Team(
        year=2019, seed_number=14, region='Midwest', eliminated=True, college_id=Bucknell.id)
    db.session.add(bucknell)

    Buffalo = College.query.filter(College.name == 'Buffalo').one()
    buffalo = March_Madness_Team(
        year=2019, seed_number=13, region='South', eliminated=True, college_id=Buffalo.id)
    db.session.add(buffalo)

    Butler = College.query.filter(College.name == 'Butler').one()
    butler = March_Madness_Team(
        year=2019, seed_number=10, region='East', eliminated=True, college_id=Butler.id)
    db.session.add(butler)

    Cal_State_Fullerton = College.query.filter(
        College.name == 'Cal State Fullerton').one()
    cal_State_Fullerton = March_Madness_Team(
        year=2019, seed_number=15, region='East', eliminated=True, college_id=Cal_State_Fullerton.id)
    db.session.add(cal_State_Fullerton)

    Charleston = College.query.filter(College.name == 'Charleston').one()
    charleston = March_Madness_Team(
        year=2019, seed_number=13, region='Midwest', eliminated=True, college_id=Charleston.id)
    db.session.add(charleston)

    Cincinnati = College.query.filter(College.name == 'Cincinnati').one()
    cincinnati = March_Madness_Team(
        year=2019, seed_number=2, region='South', eliminated=True, college_id=Cincinnati.id)
    db.session.add(cincinnati)

    Clemson = College.query.filter(College.name == 'Clemson').one()
    clemson = March_Madness_Team(
        year=2019, seed_number=5, region='Midwest', eliminated=True, college_id=Clemson.id)
    db.session.add(clemson)

    Creighton = College.query.filter(College.name == 'Creighton').one()
    creighton = March_Madness_Team(
        year=2019, seed_number=8, region='South', eliminated=True, college_id=Creighton.id)
    db.session.add(creighton)

    Davidson = College.query.filter(College.name == 'Davidson').one()
    davidson = March_Madness_Team(
        year=2019, seed_number=12, region='South', eliminated=True, college_id=Davidson.id)
    db.session.add(davidson)

    Duke = College.query.filter(College.name == 'Duke').one()
    duke = March_Madness_Team(
        year=2019, seed_number=2, region='Midwest', eliminated=True, college_id=Duke.id)
    db.session.add(duke)

    Florida_State = College.query.filter(College.name == 'Florida State').one()
    florida_State = March_Madness_Team(
        year=2019, seed_number=9, region='West', eliminated=True, college_id=Florida_State.id)
    db.session.add(florida_State)

    Florida = College.query.filter(College.name == 'Florida').one()
    florida = March_Madness_Team(
        year=2019, seed_number=6, region='East', eliminated=True, college_id=Florida.id)
    db.session.add(florida)

    Georgia_State = College.query.filter(College.name == 'Georgia State').one()
    georgia_State = March_Madness_Team(
        year=2019, seed_number=15, region='South', eliminated=True, college_id=Georgia_State.id)
    db.session.add(georgia_State)

    Gonzaga = College.query.filter(College.name == 'Gonzaga').one()
    gonzaga = March_Madness_Team(
        year=2019, seed_number=4, region='West', eliminated=True, college_id=Gonzaga.id)
    db.session.add(gonzaga)

    Houston = College.query.filter(College.name == 'Houston').one()
    houston = March_Madness_Team(
        year=2019, seed_number=6, region='West', eliminated=True, college_id=Houston.id)
    db.session.add(houston)

    Iona = College.query.filter(College.name == 'Iona').one()
    iona = March_Madness_Team(
        year=2019, seed_number=15, region='Midwest', eliminated=True, college_id=Iona.id)
    db.session.add(iona)

    Kansas_State = College.query.filter(College.name == 'Kansas State').one()
    kansas_State = March_Madness_Team(
        year=2019, seed_number=9, region='South', eliminated=True, college_id=Kansas_State.id)
    db.session.add(kansas_State)

    Kansas = College.query.filter(College.name == 'Kansas').one()
    kansas = March_Madness_Team(
        year=2019, seed_number=1, region='Midwest', eliminated=True, college_id=Kansas.id)
    db.session.add(kansas)

    Kentucky = College.query.filter(College.name == 'Kentucky').one()
    kentucky = March_Madness_Team(
        year=2019, seed_number=5, region='South', eliminated=True, college_id=Kentucky.id)
    db.session.add(kentucky)

    Lipscomb = College.query.filter(College.name == 'Lipscomb').one()
    lipscomb = March_Madness_Team(
        year=2019, seed_number=15, region='West', eliminated=True, college_id=Lipscomb.id)
    db.session.add(lipscomb)

    Radford = College.query.filter(College.name == 'Radford').one()
    radford = March_Madness_Team(
        year=2019, seed_number=16, region='East', eliminated=True, college_id=Radford.id)
    db.session.add(radford)

    Loyola_Chicago = College.query.filter(
        College.name == 'Loyola Chicago').one()
    loyola_Chicago = March_Madness_Team(
        year=2019, seed_number=11, region='South', eliminated=True, college_id=Loyola_Chicago.id)
    db.session.add(loyola_Chicago)

    Marshall = College.query.filter(College.name == 'Marshall').one()
    marshall = March_Madness_Team(
        year=2019, seed_number=13, region='East', eliminated=True, college_id=Marshall.id)
    db.session.add(marshall)

    Miami = College.query.filter(College.name == 'Miami').one()
    miami = March_Madness_Team(
        year=2019, seed_number=6, region='South', eliminated=True, college_id=Miami.id)
    db.session.add(miami)

    Michigan_State = College.query.filter(
        College.name == 'Michigan State').one()
    michigan_State = March_Madness_Team(
        year=2019, seed_number=3, region='Midwest', eliminated=True, college_id=Michigan_State.id)
    db.session.add(michigan_State)

    Michigan = College.query.filter(College.name == 'Michigan').one()
    michigan = March_Madness_Team(
        year=2019, seed_number=4, region='West', eliminated=True, college_id=Michigan.id)
    db.session.add(michigan)

    Missouri = College.query.filter(College.name == 'Missouri').one()
    missouri = March_Madness_Team(
        year=2019, seed_number=8, region='West', eliminated=True, college_id=Missouri.id)
    db.session.add(missouri)

    Montana = College.query.filter(College.name == 'Montana').one()
    montana = March_Madness_Team(
        year=2019, seed_number=14, region='West', eliminated=True, college_id=Montana.id)
    db.session.add(montana)

    Murray_State = College.query.filter(College.name == 'Murray State').one()
    murray_State = March_Madness_Team(
        year=2019, seed_number=12, region='East', eliminated=True, college_id=Murray_State.id)
    db.session.add(murray_State)

    Texas_Southern = College.query.filter(
        College.name == 'Texas Southern').one()
    texas_Southern = March_Madness_Team(
        year=2019, seed_number=16, region='West', eliminated=True, college_id=Texas_Southern.id)
    db.session.add(texas_Southern)

    UNC_Greensboro = College.query.filter(
        College.name == 'UNC Greensboro').one()
    uNC_Greensboro = March_Madness_Team(
        year=2019, seed_number=13, region='West', eliminated=True, college_id=UNC_Greensboro.id)
    db.session.add(uNC_Greensboro)

    Nevada = College.query.filter(College.name == 'Nevada').one()
    nevada = March_Madness_Team(
        year=2019, seed_number=7, region='South', eliminated=True, college_id=Nevada.id)
    db.session.add(nevada)

    New_Mexico_State = College.query.filter(
        College.name == 'New Mexico State').one()
    new_Mexico_State = March_Madness_Team(
        year=2019, seed_number=12, region='Midwest', eliminated=True, college_id=New_Mexico_State.id)
    db.session.add(new_Mexico_State)

    North_Carolina_State = College.query.filter(
        College.name == 'North Carolina State').one()
    north_Carolina_State = March_Madness_Team(
        year=2019, seed_number=9, region='Midwest', eliminated=True, college_id=North_Carolina_State.id)
    db.session.add(north_Carolina_State)

    North_Carolina = College.query.filter(
        College.name == 'North Carolina').one()
    north_Carolina = March_Madness_Team(
        year=2019, seed_number=2, region='West', eliminated=True, college_id=North_Carolina.id)
    db.session.add(north_Carolina)

    Ohio_State = College.query.filter(College.name == 'Ohio State').one()
    ohio_State = March_Madness_Team(
        year=2019, seed_number=5, region='West', eliminated=True, college_id=Ohio_State.id)
    db.session.add(ohio_State)

    Oklahoma = College.query.filter(College.name == 'Oklahoma').one()
    oklahoma = March_Madness_Team(
        year=2019, seed_number=10, region='Midwest', eliminated=True, college_id=Oklahoma.id)
    db.session.add(oklahoma)

    Penn = College.query.filter(College.name == 'Penn').one()
    penn = March_Madness_Team(
        year=2019, seed_number=16, region='Midwest', eliminated=True, college_id=Penn.id)
    db.session.add(penn)

    Providence = College.query.filter(College.name == 'Providence').one()
    providence = March_Madness_Team(
        year=2019, seed_number=10, region='West', eliminated=True, college_id=Providence.id)
    db.session.add(providence)

    Purdue = College.query.filter(College.name == 'Purdue').one()
    purdue = March_Madness_Team(
        year=2019, seed_number=2, region='East', eliminated=True, college_id=Purdue.id)
    db.session.add(purdue)

    Rhode_Island = College.query.filter(College.name == 'Rhode Island').one()
    rhode_Island = March_Madness_Team(
        year=2019, seed_number=7, region='Midwest', eliminated=True, college_id=Rhode_Island.id)
    db.session.add(rhode_Island)

    San_Diego_State = College.query.filter(
        College.name == 'San Diego State').one()
    san_Diego_State = March_Madness_Team(
        year=2019, seed_number=11, region='West', eliminated=True, college_id=San_Diego_State.id)
    db.session.add(san_Diego_State)

    Seton_Hall = College.query.filter(College.name == 'Seton Hall').one()
    seton_Hall = March_Madness_Team(
        year=2019, seed_number=8, region='Midwest', eliminated=True, college_id=Seton_Hall.id)
    db.session.add(seton_Hall)

    South_Dakota_State = College.query.filter(
        College.name == 'South Dakota State').one()
    south_Dakota_State = March_Madness_Team(
        year=2019, seed_number=12, region='West', eliminated=True, college_id=South_Dakota_State.id)
    db.session.add(south_Dakota_State)

    St_Bonaventure = College.query.filter(
        College.name == 'St. Bonaventure').one()
    st_Bonaventure = March_Madness_Team(
        year=2019, seed_number=11, region='East', eliminated=True, college_id=St_Bonaventure.id)
    db.session.add(st_Bonaventure)

    Stephen_F_Austin = College.query.filter(
        College.name == 'Stephen F. Austin').one()
    stephen_F_Austin = March_Madness_Team(
        year=2019, seed_number=14, region='East', eliminated=True, college_id=Stephen_F_Austin.id)
    db.session.add(stephen_F_Austin)

    TCU = College.query.filter(College.name == 'TCU').one()
    tCU = March_Madness_Team(
        year=2019, seed_number=6, region='Midwest', eliminated=True, college_id=TCU.id)
    db.session.add(tCU)

    Tennessee = College.query.filter(College.name == 'Tennessee').one()
    tennessee = March_Madness_Team(
        year=2019, seed_number=3, region='South', eliminated=True, college_id=Tennessee.id)
    db.session.add(tennessee)

    Texas_AM = College.query.filter(College.name == 'Texas A&M').one()
    texas_AM = March_Madness_Team(
        year=2019, seed_number=7, region='West', eliminated=True, college_id=Texas_AM.id)
    db.session.add(texas_AM)

    Texas_Tech = College.query.filter(College.name == 'Texas Tech').one()
    texas_Tech = March_Madness_Team(
        year=2019, seed_number=3, region='East', eliminated=True, college_id=Texas_Tech.id)
    db.session.add(texas_Tech)

    Texas = College.query.filter(College.name == 'Texas').one()
    texas = March_Madness_Team(
        year=2019, seed_number=10, region='South', eliminated=True, college_id=Texas.id)
    db.session.add(texas)

    UMBC = College.query.filter(College.name == 'UMBC').one()
    uMBC = March_Madness_Team(
        year=2019, seed_number=16, region='South', eliminated=True, college_id=UMBC.id)
    db.session.add(uMBC)

    Villanova = College.query.filter(College.name == 'Villanova').one()
    villanova = March_Madness_Team(
        year=2019, seed_number=1, region='East', eliminated=False, college_id=Villanova.id)
    db.session.add(villanova)

    Virginia_Tech = College.query.filter(College.name == 'Virginia Tech').one()
    virginia_Tech = March_Madness_Team(
        year=2019, seed_number=8, region='East', eliminated=True, college_id=Virginia_Tech.id)
    db.session.add(virginia_Tech)

    Virginia = College.query.filter(College.name == 'Virginia').one()
    virginia = March_Madness_Team(
        year=2019, seed_number=1, region='South', eliminated=True, college_id=Virginia.id)
    db.session.add(virginia)

    West_Virginia = College.query.filter(College.name == 'West Virginia').one()
    west_Virginia = March_Madness_Team(
        year=2019, seed_number=5, region='East', eliminated=True, college_id=West_Virginia.id)
    db.session.add(west_Virginia)

    Wichita_State = College.query.filter(College.name == 'Wichita State').one()
    wichita_State = March_Madness_Team(
        year=2019, seed_number=4, region='East', eliminated=True, college_id=Wichita_State.id)
    db.session.add(wichita_State)

    Wright_State = College.query.filter(College.name == 'Wright State').one()
    wright_State = March_Madness_Team(
        year=2019, seed_number=14, region='South', eliminated=True, college_id=Wright_State.id)
    db.session.add(wright_State)

    Xavier = College.query.filter(College.name == 'Xavier').one()
    xavier = March_Madness_Team(
        year=2019, seed_number=1, region='West', eliminated=True, college_id=Xavier.id)
    db.session.add(xavier)

    db.session.commit()

    game_1 = Game(game_num=1, round_num=1, winning_team_id=None)
    db.session.add(game_1)
    game_2 = Game(game_num=2, round_num=1, winning_team_id=None)
    db.session.add(game_2)
    game_3 = Game(game_num=3, round_num=1, winning_team_id=None)
    db.session.add(game_3)
    game_4 = Game(game_num=4, round_num=1, winning_team_id=None)
    db.session.add(game_4)
    game_5 = Game(game_num=5, round_num=1, winning_team_id=None)
    db.session.add(game_5)
    game_6 = Game(game_num=6, round_num=1, winning_team_id=None)
    db.session.add(game_6)
    game_7 = Game(game_num=7, round_num=1, winning_team_id=None)
    db.session.add(game_7)
    game_8 = Game(game_num=8, round_num=1, winning_team_id=None)
    db.session.add(game_8)
    game_9 = Game(game_num=9, round_num=1, winning_team_id=None)
    db.session.add(game_9)
    game_10 = Game(game_num=10, round_num=1, winning_team_id=None)
    db.session.add(game_10)
    game_11 = Game(game_num=11, round_num=1, winning_team_id=None)
    db.session.add(game_11)
    game_12 = Game(game_num=12, round_num=1, winning_team_id=None)
    db.session.add(game_12)
    game_13 = Game(game_num=13, round_num=1, winning_team_id=None)
    db.session.add(game_13)
    game_14 = Game(game_num=14, round_num=1, winning_team_id=None)
    db.session.add(game_14)
    game_15 = Game(game_num=15, round_num=1, winning_team_id=None)
    db.session.add(game_15)
    game_16 = Game(game_num=16, round_num=1, winning_team_id=None)
    db.session.add(game_16)
    game_17 = Game(game_num=17, round_num=1, winning_team_id=None)
    db.session.add(game_17)
    game_18 = Game(game_num=18, round_num=1, winning_team_id=None)
    db.session.add(game_18)
    game_19 = Game(game_num=19, round_num=1, winning_team_id=None)
    db.session.add(game_19)
    game_20 = Game(game_num=20, round_num=1, winning_team_id=None)
    db.session.add(game_20)
    game_21 = Game(game_num=21, round_num=1, winning_team_id=None)
    db.session.add(game_21)
    game_22 = Game(game_num=22, round_num=1, winning_team_id=None)
    db.session.add(game_22)
    game_23 = Game(game_num=23, round_num=1, winning_team_id=None)
    db.session.add(game_23)
    game_24 = Game(game_num=24, round_num=1, winning_team_id=None)
    db.session.add(game_24)
    game_25 = Game(game_num=25, round_num=1, winning_team_id=None)
    db.session.add(game_25)
    game_26 = Game(game_num=26, round_num=1, winning_team_id=None)
    db.session.add(game_26)
    game_27 = Game(game_num=27, round_num=1, winning_team_id=None)
    db.session.add(game_27)
    game_28 = Game(game_num=28, round_num=1, winning_team_id=None)
    db.session.add(game_28)
    game_29 = Game(game_num=29, round_num=1, winning_team_id=None)
    db.session.add(game_29)
    game_30 = Game(game_num=30, round_num=1, winning_team_id=None)
    db.session.add(game_30)
    game_31 = Game(game_num=31, round_num=1, winning_team_id=None)
    db.session.add(game_31)
    game_32 = Game(game_num=32, round_num=1, winning_team_id=None)
    db.session.add(game_32)

    db.session.commit()

    game_1_win_score = Game_Team_Score(
        game_id=game_1.id, team_id=uMBC.id, score=74)
    game_1_lose_score = Game_Team_Score(
        game_id=game_1.id, team_id=virginia.id, score=54)
    game_1.game_team_scores = [game_1_win_score, game_1_lose_score]
    # game_1.child_game_id = game_33.id

    game_2_win_score = Game_Team_Score(
        game_id=game_2.id, team_id=kansas_State.id, score=69)
    game_2_lose_score = Game_Team_Score(
        game_id=game_2.id, team_id=creighton.id, score=59)
    game_2.game_team_scores = [game_2_win_score, game_2_lose_score]
    # game_2.child_game_id = game_33.id

    game_3_win_score = Game_Team_Score(
        game_id=game_3.id, team_id=kentucky.id, score=78)
    game_3_lose_score = Game_Team_Score(
        game_id=game_3.id, team_id=davidson.id, score=73)
    game_3.game_team_scores = [game_3_win_score, game_3_lose_score]
    # game_3.child_game_id = game_34.id

    game_4_win_score = Game_Team_Score(
        game_id=game_4.id, team_id=buffalo.id, score=89)
    game_4_lose_score = Game_Team_Score(
        game_id=game_4.id, team_id=arizona.id, score=68)
    game_4.game_team_scores = [game_4_win_score, game_4_lose_score]
    # game_4.child_game_id = game_34.id

    game_5_win_score = Game_Team_Score(
        game_id=game_5.id, team_id=loyola_Chicago.id, score=64)
    game_5_lose_score = Game_Team_Score(
        game_id=game_5.id, team_id=miami.id, score=62)
    game_5.game_team_scores = [game_5_win_score, game_5_lose_score]
    # game_5.child_game_id = game_35.id

    game_6_win_score = Game_Team_Score(
        game_id=game_6.id, team_id=tennessee.id, score=73)
    game_6_lose_score = Game_Team_Score(
        game_id=game_6.id, team_id=wright_State.id, score=47)
    game_6.game_team_scores = [game_6_win_score, game_6_lose_score]
    # game_6.child_game_id = game_35.id

    game_7_win_score = Game_Team_Score(
        game_id=game_7.id, team_id=nevada.id, score=87)
    game_7_lose_score = Game_Team_Score(
        game_id=game_7.id, team_id=texas.id, score=83)
    game_7.game_team_scores = [game_7_win_score, game_7_lose_score]
    # game_7.child_game_id = game_36.id

    game_8_win_score = Game_Team_Score(
        game_id=game_8.id, team_id=cincinnati.id, score=68)
    game_8_lose_score = Game_Team_Score(
        game_id=game_8.id, team_id=georgia_State.id, score=53)
    game_8.game_team_scores = [game_8_win_score, game_8_lose_score]
    # game_8.child_game_id = game_36.id

    game_9_win_score = Game_Team_Score(
        game_id=game_9.id, team_id=xavier.id, score=102)
    game_9_lose_score = Game_Team_Score(
        game_id=game_9.id, team_id=texas_Southern.id, score=83)
    game_9.game_team_scores = [game_9_win_score, game_9_lose_score]
    # game_9.child_game_id = game_37.id

    game_10_win_score = Game_Team_Score(
        game_id=game_10.id, team_id=florida_State.id, score=67)
    game_10_lose_score = Game_Team_Score(
        game_id=game_10.id, team_id=missouri.id, score=54)
    game_10.game_team_scores = [game_10_win_score, game_10_lose_score]
    # game_10.child_game_id = game_37.id

    game_11_win_score = Game_Team_Score(
        game_id=game_11.id, team_id=ohio_State.id, score=81)
    game_11_lose_score = Game_Team_Score(
        game_id=game_11.id, team_id=south_Dakota_State.id, score=73)
    game_11.game_team_scores = [game_11_win_score, game_11_lose_score]
    # game_11.child_game_id = game_38.id

    game_12_win_score = Game_Team_Score(
        game_id=game_12.id, team_id=gonzaga.id, score=68)
    game_12_lose_score = Game_Team_Score(
        game_id=game_12.id, team_id=uNC_Greensboro.id, score=64)
    game_12.game_team_scores = [game_12_win_score, game_12_lose_score]
    # game_12.child_game_id = game_38.id

    game_13_win_score = Game_Team_Score(
        game_id=game_13.id, team_id=houston.id, score=67)
    game_13_lose_score = Game_Team_Score(
        game_id=game_13.id, team_id=san_Diego_State.id, score=65)
    game_13.game_team_scores = [game_13_win_score, game_13_lose_score]
    # game_13.child_game_id = game_39.id

    game_14_win_score = Game_Team_Score(
        game_id=game_14.id, team_id=michigan.id, score=61)
    game_14_lose_score = Game_Team_Score(
        game_id=game_14.id, team_id=montana.id, score=47)
    game_14.game_team_scores = [game_14_win_score, game_14_lose_score]
    # game_14.child_game_id = game_39.id

    game_15_win_score = Game_Team_Score(
        game_id=game_15.id, team_id=texas_AM.id, score=73)
    game_15_lose_score = Game_Team_Score(
        game_id=game_15.id, team_id=providence.id, score=69)
    game_15.game_team_scores = [game_15_win_score, game_15_lose_score]
    # game_15.child_game_id = game_40.id

    game_16_win_score = Game_Team_Score(
        game_id=game_16.id, team_id=north_Carolina.id, score=84)
    game_16_lose_score = Game_Team_Score(
        game_id=game_16.id, team_id=lipscomb.id, score=66)
    game_16.game_team_scores = [game_16_win_score, game_16_lose_score]
    # game_16.child_game_id = game_40.id

    game_17_win_score = Game_Team_Score(
        game_id=game_17.id, team_id=villanova.id, score=87)
    game_17_lose_score = Game_Team_Score(
        game_id=game_17.id, team_id=radford.id, score=61)
    game_17.game_team_scores = [game_17_win_score, game_17_lose_score]
    # game_17.child_game_id = game_41.id

    game_18_win_score = Game_Team_Score(
        game_id=game_18.id, team_id=alabama.id, score=86)
    game_18_lose_score = Game_Team_Score(
        game_id=game_18.id, team_id=virginia_Tech.id, score=83)
    game_18.game_team_scores = [game_18_win_score, game_18_lose_score]
    # game_18.child_game_id = game_41.id

    game_19_win_score = Game_Team_Score(
        game_id=game_19.id, team_id=west_Virginia.id, score=85)
    game_19_lose_score = Game_Team_Score(
        game_id=game_19.id, team_id=murray_State.id, score=68)
    game_19.game_team_scores = [game_19_win_score, game_19_lose_score]
    # game_19.child_game_id = game_42.id

    game_20_win_score = Game_Team_Score(
        game_id=game_20.id, team_id=marshall.id, score=81)
    game_20_lose_score = Game_Team_Score(
        game_id=game_20.id, team_id=wichita_State.id, score=75)
    game_20.game_team_scores = [game_20_win_score, game_20_lose_score]
    # game_20.child_game_id = game_42.id

    game_21_win_score = Game_Team_Score(
        game_id=game_21.id, team_id=florida.id, score=77)
    game_21_lose_score = Game_Team_Score(
        game_id=game_21.id, team_id=st_Bonaventure.id, score=62)
    game_21.game_team_scores = [game_21_win_score, game_21_lose_score]
    # game_21.child_game_id = game_43.id

    game_22_win_score = Game_Team_Score(
        game_id=game_22.id, team_id=texas_Tech.id, score=70)
    game_22_lose_score = Game_Team_Score(
        game_id=game_22.id, team_id=stephen_F_Austin.id, score=60)
    game_22.game_team_scores = [game_22_win_score, game_22_lose_score]
    # game_22.child_game_id = game_43.id

    game_23_win_score = Game_Team_Score(
        game_id=game_23.id, team_id=butler.id, score=79)
    game_23_lose_score = Game_Team_Score(
        game_id=game_23.id, team_id=arkansas.id, score=62)
    game_23.game_team_scores = [game_23_win_score, game_23_lose_score]
    # game_23.child_game_id = game_44.id

    game_24_win_score = Game_Team_Score(
        game_id=game_24.id, team_id=purdue.id, score=74)
    game_24_lose_score = Game_Team_Score(
        game_id=game_24.id, team_id=cal_State_Fullerton.id, score=48)
    game_24.game_team_scores = [game_24_win_score, game_24_lose_score]
    # game_24.child_game_id = game_44.id

    game_25_win_score = Game_Team_Score(
        game_id=game_25.id, team_id=kansas.id, score=76)
    game_25_lose_score = Game_Team_Score(
        game_id=game_25.id, team_id=penn.id, score=60)
    game_25.game_team_scores = [game_25_win_score, game_25_lose_score]
    # game_25.child_game_id = game_45.id

    game_26_win_score = Game_Team_Score(
        game_id=game_26.id, team_id=seton_Hall.id, score=94)
    game_26_lose_score = Game_Team_Score(
        game_id=game_26.id, team_id=north_Carolina_State.id, score=83)
    game_26.game_team_scores = [game_26_win_score, game_26_lose_score]
    # game_26.child_game_id = game_45.id

    game_27_win_score = Game_Team_Score(
        game_id=game_27.id, team_id=clemson.id, score=79)
    game_27_lose_score = Game_Team_Score(
        game_id=game_27.id, team_id=new_Mexico_State.id, score=68)
    game_27.game_team_scores = [game_27_win_score, game_27_lose_score]
    # game_27.child_game_id = game_46.id

    game_28_win_score = Game_Team_Score(
        game_id=game_28.id, team_id=auburn.id, score=62)
    game_28_lose_score = Game_Team_Score(
        game_id=game_28.id, team_id=charleston.id, score=58)
    game_28.game_team_scores = [game_28_win_score, game_28_lose_score]
    # game_28.child_game_id = game_46.id

    game_29_win_score = Game_Team_Score(
        game_id=game_29.id, team_id=syracuse.id, score=57)
    game_29_lose_score = Game_Team_Score(
        game_id=game_29.id, team_id=tCU.id, score=52)
    game_29.game_team_scores = [game_29_win_score, game_29_lose_score]
    # game_29.child_game_id = game_47.id

    game_30_win_score = Game_Team_Score(
        game_id=game_30.id, team_id=michigan_State.id, score=82)
    game_30_lose_score = Game_Team_Score(
        game_id=game_30.id, team_id=bucknell.id, score=78)
    game_30.game_team_scores = [game_30_win_score, game_30_lose_score]
    # game_30.child_game_id = game_47.id

    game_31_win_score = Game_Team_Score(
        game_id=game_31.id, team_id=rhode_Island.id, score=83)
    game_31_lose_score = Game_Team_Score(
        game_id=game_31.id, team_id=oklahoma.id, score=78)
    game_31.game_team_scores = [game_31_win_score, game_31_lose_score]
    # game_31.child_game_id = game_48.id

    game_32_win_score = Game_Team_Score(
        game_id=game_32.id, team_id=duke.id, score=89)
    game_32_lose_score = Game_Team_Score(
        game_id=game_32.id, team_id=iona.id, score=67)
    game_32.game_team_scores = [game_32_win_score, game_32_lose_score]
    # game_32.child_game_id = game_48.id

    db.session.commit()

    league = League.query.filter(
        League.name == 'The Dumb Friends League').one()
    lu_ids = {lu.user.name: lu.id for lu in league.league_users}
    draft_order = [
        lu_ids['Will'],
        lu_ids['Ryan'],
        lu_ids['Chase'],
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
        lu_ids['Chase'],
        lu_ids['Ryan'],
        lu_ids['Will'],
        lu_ids['Patrick'],
        lu_ids['Mitch'],
        lu_ids['Chase'],
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
        lu_ids['Chase'],
        lu_ids['Mitch'],
        lu_ids['Patrick'],
        lu_ids['Patrick'],
        lu_ids['Chase'],
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
        lu_ids['Chase'],
        lu_ids['Patrick'],
        lu_ids['Will'],
        lu_ids['Demo'],
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
        lu_ids['Demo'],
        lu_ids['Will'],
    ]

    draft = Draft(league_id=league.id,
                  year=2019, draft_order=json.dumps(draft_order), draft_index=0,
                  draft_time=datetime.now(), drafting=True, current_drafter_id=None,
                  time_limit_mins=None)
    db.session.add(draft)
    db.session.commit()


def undo_draft_2019():
    db.session.execute(
        'TRUNCATE march_madness_teams RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE games RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE drafts RESTART IDENTITY CASCADE;')
    db.session.commit()
