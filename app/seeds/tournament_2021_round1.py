from app.models import db, March_Madness_Team, College, Game, Game_Team_Score, League, League_User, Draft, Drafted_Team, User, Tournament
import json
from datetime import datetime


def seed_2021_tournament_round1():
    tournament = Tournament.query.filter(Tournament.year == 2021).one()
    tournament.last_round_completed = 1

    # West
    Gonzaga = College.query.filter(College.name == 'Gonzaga').one()
    gonzaga = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Gonzaga.id
    ).one()

    Norfolk_State = College.query.filter(College.name == 'Norfolk St.').one()
    norfolk_State = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Norfolk_State.id
    ).one()

    Oklahoma = College.query.filter(College.name == 'Oklahoma').one()
    oklahoma = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Oklahoma.id
    ).one()

    Missouri = College.query.filter(College.name == 'Missouri').one()
    missouri = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Missouri.id
    ).one()

    Creighton = College.query.filter(College.name == 'Creighton').one()
    creighton = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Creighton.id
    ).one()

    UCSB = College.query.filter(College.name == 'UCSB').one()
    uCSB = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == UCSB.id
    ).one()

    Virginia = College.query.filter(College.name == 'Virginia').one()
    virginia = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Virginia.id
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

    Drake = College.query.filter(College.name == 'Drake').one()
    drake = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Drake.id
    ).one()

    Kansas = College.query.filter(College.name == 'Kansas').one()
    kansas = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Kansas.id
    ).one()

    Eastern_Washington = College.query.filter(
        College.name == 'Eastern Washington').one()
    eastern_Washington = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Eastern_Washington.id
    ).one()

    Oregon = College.query.filter(College.name == 'Oregon').one()
    oregon = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Oregon.id
    ).one()

    VCU = College.query.filter(College.name == 'VCU').one()
    vCU = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == VCU.id
    ).one()

    Iowa = College.query.filter(College.name == 'Iowa').one()
    iowa = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Iowa.id
    ).one()

    Grand_Canyon = College.query.filter(College.name == 'Grand Canyon').one()
    grand_Canyon = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Grand_Canyon.id
    ).one()

    # South
    Baylor = College.query.filter(College.name == 'Baylor').one()
    baylor = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Baylor.id
    ).one()

    Hartford = College.query.filter(College.name == 'Hartford').one()
    hartford = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Hartford.id
    ).one()

    North_Carolina = College.query.filter(
        College.name == 'North Carolina').one()
    north_Carolina = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == North_Carolina.id
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

    Winthrop = College.query.filter(College.name == 'Winthrop').one()
    winthrop = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Winthrop.id
    ).one()

    Purdue = College.query.filter(College.name == 'Purdue').one()
    purdue = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Purdue.id
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

    Utah_State = College.query.filter(College.name == 'Utah State').one()
    utah_State = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Utah_State.id
    ).one()

    Arkansas = College.query.filter(College.name == 'Arkansas').one()
    arkansas = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Arkansas.id
    ).one()

    Colgate = College.query.filter(College.name == 'Colgate').one()
    colgate = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Colgate.id
    ).one()

    Florida = College.query.filter(College.name == 'Florida').one()
    florida = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Florida.id
    ).one()

    Virginia_Tech = College.query.filter(College.name == 'Virginia Tech').one()
    virginia_Tech = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Virginia_Tech.id
    ).one()

    Ohio_State = College.query.filter(College.name == 'Ohio State').one()
    ohio_State = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Ohio_State.id
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

    Drexel = College.query.filter(College.name == 'Drexel').one()
    drexel = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Drexel.id
    ).one()

    Loyola_Chicago = College.query.filter(
        College.name == 'Loyola Chicago').one()
    loyola_Chicago = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Loyola_Chicago.id
    ).one()

    Georgia_Tech = College.query.filter(College.name == 'Georgia Tech').one()
    georgia_Tech = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Georgia_Tech.id
    ).one()

    Tennessee = College.query.filter(College.name == 'Tennessee').one()
    tennessee = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Tennessee.id
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

    Liberty = College.query.filter(College.name == 'Liberty').one()
    liberty = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Liberty.id
    ).one()

    San_Diego_State = College.query.filter(
        College.name == 'San Diego State').one()
    san_Diego_State = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == San_Diego_State.id
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

    Morehead_State = College.query.filter(
        College.name == 'Morehead State').one()
    morehead_State = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Morehead_State.id
    ).one()

    Clemson = College.query.filter(College.name == 'Clemson').one()
    clemson = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Clemson.id
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

    Cleveland_State = College.query.filter(
        College.name == 'Cleveland State').one()
    cleveland_State = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Cleveland_State.id
    ).one()

    # East
    Michigan = College.query.filter(College.name == 'Michigan').one()
    michigan = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Michigan.id
    ).one()

    Texas_Southern = College.query.filter(
        College.name == 'Texas Southern').one()
    texas_Southern = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Texas_Southern.id
    ).one()

    LSU = College.query.filter(College.name == 'LSU').one()
    lSU = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == LSU.id
    ).one()

    St_Bonaventure = College.query.filter(
        College.name == 'St. Bonaventure').one()
    st_Bonaventure = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == St_Bonaventure.id
    ).one()

    Colorado = College.query.filter(College.name == 'Colorado').one()
    colorado = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Colorado.id
    ).one()

    Georgetown = College.query.filter(College.name == 'Georgetown').one()
    georgetown = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Georgetown.id
    ).one()

    Florida_State = College.query.filter(College.name == 'Florida State').one()
    florida_State = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Florida_State.id
    ).one()

    UNC_Greensboro = College.query.filter(
        College.name == 'UNC Greensboro').one()
    uNC_Greensboro = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == UNC_Greensboro.id
    ).one()

    BYU = College.query.filter(College.name == 'BYU').one()
    bYU = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == BYU.id
    ).one()

    UCLA = College.query.filter(
        College.name == 'UCLA').one()
    uCLA = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == UCLA.id
    ).one()

    Texas = College.query.filter(College.name == 'Texas').one()
    texas = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Texas.id
    ).one()

    Abilene_Christian = College.query.filter(
        College.name == 'Abilene Christian').one()
    abilene_Christian = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Abilene_Christian.id
    ).one()

    UCONN = College.query.filter(College.name == 'UCONN').one()
    uCONN = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == UCONN.id
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

    Iona = College.query.filter(College.name == 'Iona').one()
    iona = March_Madness_Team.query.filter(
        March_Madness_Team.tournament_id == tournament.id).filter(
        March_Madness_Team.college_id == Iona.id
    ).one()

    game_1 = Game.query.filter(
        Game.game_num == 1
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_1.winning_team_id = gonzaga.id

    game_2 = Game.query.filter(
        Game.game_num == 2
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_2.winning_team_id = oklahoma.id

    game_3 = Game.query.filter(
        Game.game_num == 3
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_3.winning_team_id = creighton.id

    game_4 = Game.query.filter(
        Game.game_num == 4
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_4.winning_team_id = ohio.id

    game_5 = Game.query.filter(
        Game.game_num == 5
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_5.winning_team_id = uSC.id

    game_6 = Game.query.filter(
        Game.game_num == 6
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_6.winning_team_id = kansas.id

    game_7 = Game.query.filter(
        Game.game_num == 7
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_7.winning_team_id = oregon.id

    game_8 = Game.query.filter(
        Game.game_num == 8
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_8.winning_team_id = iowa.id

    game_9 = Game.query.filter(
        Game.game_num == 9
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_9.winning_team_id = michigan.id

    game_10 = Game.query.filter(
        Game.game_num == 10
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_10.winning_team_id = lSU.id

    game_11 = Game.query.filter(
        Game.game_num == 11
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_11.winning_team_id = colorado.id

    game_12 = Game.query.filter(
        Game.game_num == 12
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_12.winning_team_id = florida_State.id

    game_13 = Game.query.filter(
        Game.game_num == 13
    ).filter(
        Game.round_num == 1
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_13.winning_team_id = uCLA.id

    game_14 = Game.query.filter(
        Game.game_num == 14
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_14.winning_team_id = abilene_Christian.id

    game_15 = Game.query.filter(
        Game.game_num == 15
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_15.winning_team_id = maryland.id

    game_16 = Game.query.filter(
        Game.game_num == 16
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_16.winning_team_id = alabama.id

    game_17 = Game.query.filter(
        Game.game_num == 17
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_17.winning_team_id = baylor.id

    game_18 = Game.query.filter(
        Game.game_num == 18
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_18.winning_team_id = wisconsin.id

    game_19 = Game.query.filter(
        Game.game_num == 19
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_19.winning_team_id = villanova.id

    game_20 = Game.query.filter(
        Game.game_num == 20
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_20.winning_team_id = north_Texas.id

    game_21 = Game.query.filter(
        Game.game_num == 21
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_21.winning_team_id = texas_Tech.id

    game_22 = Game.query.filter(
        Game.game_num == 22
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_22.winning_team_id = arkansas.id

    game_23 = Game.query.filter(
        Game.game_num == 23
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_23.winning_team_id = florida.id

    game_24 = Game.query.filter(
        Game.game_num == 24
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_24.winning_team_id = oral_Roberts.id

    game_25 = Game.query.filter(
        Game.game_num == 25
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_25.winning_team_id = illinois.id

    game_26 = Game.query.filter(
        Game.game_num == 26
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_26.winning_team_id = loyola_Chicago.id

    game_27 = Game.query.filter(
        Game.game_num == 27
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_27.winning_team_id = oregon_State.id

    game_28 = Game.query.filter(
        Game.game_num == 28
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_28.winning_team_id = oklahoma_State.id

    game_29 = Game.query.filter(
        Game.game_num == 29
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_29.winning_team_id = syracuse.id

    game_30 = Game.query.filter(
        Game.game_num == 30
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_30.winning_team_id = west_Virginia.id

    game_31 = Game.query.filter(
        Game.game_num == 31
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_31.winning_team_id = rutgers.id

    game_32 = Game.query.filter(
        Game.game_num == 32
    ).filter(
        Game.tournament_id == tournament.id
    ).one()
    game_32.winning_team_id = houston.id

    db.session.commit()

    game_1_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_1.id).filter(
        Game_Team_Score.team_id == gonzaga.id
    ).one()
    game_1_win_score.score = 98
    game_1_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_1.id).filter(
        Game_Team_Score.team_id == norfolk_State.id
    ).one()
    game_1_lose_score.score = 55

    game_2_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_2.id).filter(
        Game_Team_Score.team_id == oklahoma.id
    ).one()
    game_2_win_score.score = 72
    game_2_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_2.id).filter(
        Game_Team_Score.team_id == missouri.id
    ).one()
    game_2_lose_score.score = 68

    game_3_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_3.id).filter(
        Game_Team_Score.team_id == creighton.id
    ).one()
    game_3_win_score.score = 63
    game_3_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_3.id).filter(
        Game_Team_Score.team_id == uCSB.id
    ).one()
    game_3_lose_score.score = 63

    game_4_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_4.id).filter(
        Game_Team_Score.team_id == ohio.id
    ).one()
    game_4_win_score.score = 62
    game_4_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_4.id).filter(
        Game_Team_Score.team_id == virginia.id
    ).one()
    game_4_lose_score.score = 58

    game_5_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_5.id).filter(
        Game_Team_Score.team_id == uSC.id
    ).one()
    game_5_win_score.score = 72
    game_5_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_5.id).filter(
        Game_Team_Score.team_id == drake.id
    ).one()
    game_5_lose_score.score = 56

    game_6_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_6.id).filter(
        Game_Team_Score.team_id == kansas.id
    ).one()
    game_6_win_score.score = 93
    game_6_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_6.id).filter(
        Game_Team_Score.team_id == eastern_Washington.id
    ).one()
    game_6_lose_score.score = 84

    game_7_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_7.id).filter(
        Game_Team_Score.team_id == oregon.id
    ).one()
    game_7_win_score.score = 1
    game_7_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_7.id).filter(
        Game_Team_Score.team_id == vCU.id
    ).one()
    game_7_lose_score.score = 0

    game_8_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_8.id).filter(
        Game_Team_Score.team_id == iowa.id
    ).one()
    game_8_win_score.score = 86
    game_8_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_8.id).filter(
        Game_Team_Score.team_id == grand_Canyon.id
    ).one()
    game_8_lose_score.score = 74

    game_9_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_9.id).filter(
        Game_Team_Score.team_id == michigan.id
    ).one()
    game_9_win_score.score = 82
    game_9_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_9.id).filter(
        Game_Team_Score.team_id == texas_Southern.id
    ).one()
    game_9_lose_score.score = 66

    game_10_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_10.id).filter(
        Game_Team_Score.team_id == lSU.id
    ).one()
    game_10_win_score.score = 76
    game_10_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_10.id).filter(
        Game_Team_Score.team_id == st_Bonaventure.id
    ).one()
    game_10_lose_score.score = 61

    game_11_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_11.id).filter(
        Game_Team_Score.team_id == colorado.id
    ).one()
    game_11_win_score.score = 96
    game_11_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_11.id).filter(
        Game_Team_Score.team_id == georgetown.id
    ).one()
    game_11_lose_score.score = 73

    game_12_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_12.id).filter(
        Game_Team_Score.team_id == florida_State.id
    ).one()
    game_12_win_score.score = 64
    game_12_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_12.id).filter(
        Game_Team_Score.team_id == uNC_Greensboro.id
    ).one()
    game_12_lose_score.score = 54

    game_13_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_13.id).filter(
        Game_Team_Score.team_id == uCLA.id
    ).one()
    game_13_win_score.score = 73
    game_13_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_13.id).filter(
        Game_Team_Score.team_id == bYU.id
    ).one()
    game_13_lose_score.score = 62

    game_14_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_14.id).filter(
        Game_Team_Score.team_id == abilene_Christian.id
    ).one()
    game_14_win_score.score = 53
    game_14_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_14.id).filter(
        Game_Team_Score.team_id == texas.id
    ).one()
    game_14_lose_score.score = 52

    game_15_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_15.id).filter(
        Game_Team_Score.team_id == maryland.id
    ).one()
    game_15_win_score.score = 63
    game_15_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_15.id).filter(
        Game_Team_Score.team_id == uCONN.id
    ).one()
    game_15_lose_score.score = 54

    game_16_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_16.id).filter(
        Game_Team_Score.team_id == alabama.id
    ).one()
    game_16_win_score.score = 68
    game_16_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_16.id).filter(
        Game_Team_Score.team_id == iona.id
    ).one()
    game_16_lose_score.score = 55

    game_17_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_17.id).filter(
        Game_Team_Score.team_id == baylor.id
    ).one()
    game_17_win_score.score = 79
    game_17_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_17.id).filter(
        Game_Team_Score.team_id == hartford.id
    ).one()
    game_17_lose_score.score = 55

    game_18_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_18.id).filter(
        Game_Team_Score.team_id == wisconsin.id
    ).one()
    game_18_win_score.score = 85
    game_18_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_18.id).filter(
        Game_Team_Score.team_id == north_Carolina.id
    ).one()
    game_18_lose_score.score = 62

    game_19_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_19.id).filter(
        Game_Team_Score.team_id == villanova.id
    ).one()
    game_19_win_score.score = 73
    game_19_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_19.id).filter(
        Game_Team_Score.team_id == winthrop.id
    ).one()
    game_19_lose_score.score = 63

    game_20_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_20.id).filter(
        Game_Team_Score.team_id == north_Texas.id
    ).one()
    game_20_win_score.score = 78
    game_20_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_20.id).filter(
        Game_Team_Score.team_id == purdue.id
    ).one()
    game_20_lose_score.score = 69

    game_21_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_21.id).filter(
        Game_Team_Score.team_id == texas_Tech.id
    ).one()
    game_21_win_score.score = 65
    game_21_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_21.id).filter(
        Game_Team_Score.team_id == utah_State.id
    ).one()
    game_21_lose_score.score = 53

    game_22_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_22.id).filter(
        Game_Team_Score.team_id == arkansas.id
    ).one()
    game_22_win_score.score = 85
    game_22_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_22.id).filter(
        Game_Team_Score.team_id == colgate.id
    ).one()
    game_22_lose_score.score = 68

    game_23_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_23.id).filter(
        Game_Team_Score.team_id == florida.id
    ).one()
    game_23_win_score.score = 75
    game_23_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_23.id).filter(
        Game_Team_Score.team_id == virginia_Tech.id
    ).one()
    game_23_lose_score.score = 70

    game_24_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_24.id).filter(
        Game_Team_Score.team_id == oral_Roberts.id
    ).one()
    game_24_win_score.score = 75
    game_24_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_24.id).filter(
        Game_Team_Score.team_id == ohio_State.id
    ).one()
    game_24_lose_score.score = 72

    game_25_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_25.id).filter(
        Game_Team_Score.team_id == illinois.id
    ).one()
    game_25_win_score.score = 78
    game_25_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_25.id).filter(
        Game_Team_Score.team_id == drexel.id
    ).one()
    game_25_lose_score.score = 49

    game_26_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_26.id).filter(
        Game_Team_Score.team_id == loyola_Chicago.id
    ).one()
    game_26_win_score.score = 71
    game_26_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_26.id).filter(
        Game_Team_Score.team_id == georgia_Tech.id
    ).one()
    game_26_lose_score.score = 60

    game_27_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_27.id).filter(
        Game_Team_Score.team_id == oregon_State.id
    ).one()
    game_27_win_score.score = 70
    game_27_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_27.id).filter(
        Game_Team_Score.team_id == tennessee.id
    ).one()
    game_27_lose_score.score = 56

    game_28_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_28.id).filter(
        Game_Team_Score.team_id == oklahoma_State.id
    ).one()
    game_28_win_score.score = 69
    game_28_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_28.id).filter(
        Game_Team_Score.team_id == liberty.id
    ).one()
    game_28_lose_score.score = 60

    game_29_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_29.id).filter(
        Game_Team_Score.team_id == syracuse.id
    ).one()
    game_29_win_score.score = 78
    game_29_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_29.id).filter(
        Game_Team_Score.team_id == san_Diego_State.id
    ).one()
    game_29_lose_score.score = 62

    game_30_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_30.id).filter(
        Game_Team_Score.team_id == west_Virginia.id
    ).one()
    game_30_win_score.score = 84
    game_30_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_30.id).filter(
        Game_Team_Score.team_id == morehead_State.id
    ).one()
    game_30_lose_score.score = 67

    game_31_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_31.id).filter(
        Game_Team_Score.team_id == rutgers.id
    ).one()
    game_31_win_score.score = 60
    game_31_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_31.id).filter(
        Game_Team_Score.team_id == clemson.id
    ).one()
    game_31_lose_score.score = 56

    game_32_win_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_32.id).filter(
        Game_Team_Score.team_id == houston.id
    ).one()
    game_32_win_score.score = 87
    game_32_lose_score = Game_Team_Score.query.filter(
        Game_Team_Score.game_id == game_32.id).filter(
        Game_Team_Score.team_id == cleveland_State.id
    ).one()
    game_32_lose_score.score = 56

    db.session.commit()

    game_33 = Game(game_num=33, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_33)
    game_34 = Game(game_num=34, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_34)
    game_35 = Game(game_num=35, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_35)
    game_36 = Game(game_num=36, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_36)
    game_37 = Game(game_num=37, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_37)
    game_38 = Game(game_num=38, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_38)
    game_39 = Game(game_num=39, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_39)
    game_40 = Game(game_num=40, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_40)
    game_41 = Game(game_num=41, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_41)
    game_42 = Game(game_num=42, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_42)
    game_43 = Game(game_num=43, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_43)
    game_44 = Game(game_num=44, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_44)
    game_45 = Game(game_num=45, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_45)
    game_46 = Game(game_num=46, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_46)
    game_47 = Game(game_num=47, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_47)
    game_48 = Game(game_num=48, round_num=2,
                   winning_team_id=None, tournament_id=tournament.id)
    db.session.add(game_48)

    db.session.commit()

    game_1.child_game_id = game_33.id
    game_2.child_game_id = game_33.id

    game_3.child_game_id = game_34.id
    game_4.child_game_id = game_34.id

    game_5.child_game_id = game_35.id
    game_6.child_game_id = game_35.id

    game_7.child_game_id = game_36.id
    game_8.child_game_id = game_36.id

    game_9.child_game_id = game_37.id
    game_10.child_game_id = game_37.id

    game_11.child_game_id = game_38.id
    game_12.child_game_id = game_38.id

    game_13.child_game_id = game_39.id
    game_14.child_game_id = game_39.id

    game_15.child_game_id = game_40.id
    game_16.child_game_id = game_40.id

    game_17.child_game_id = game_41.id
    game_18.child_game_id = game_41.id

    game_19.child_game_id = game_42.id
    game_20.child_game_id = game_42.id

    game_21.child_game_id = game_43.id
    game_22.child_game_id = game_43.id

    game_23.child_game_id = game_44.id
    game_24.child_game_id = game_44.id

    game_25.child_game_id = game_45.id
    game_26.child_game_id = game_45.id

    game_27.child_game_id = game_46.id
    game_28.child_game_id = game_46.id

    game_29.child_game_id = game_47.id
    game_30.child_game_id = game_47.id

    game_31.child_game_id = game_48.id
    game_32.child_game_id = game_48.id

    db.session.commit()

    game_33_win_score = Game_Team_Score(
        game_id=game_33.id, team_id=gonzaga.id, score=None)
    game_33_lose_score = Game_Team_Score(
        game_id=game_33.id, team_id=oklahoma.id, score=None)
    game_33.game_team_scores = [game_33_win_score, game_33_lose_score]

    game_34_win_score = Game_Team_Score(
        game_id=game_34.id, team_id=creighton.id, score=None)
    game_34_lose_score = Game_Team_Score(
        game_id=game_34.id, team_id=ohio.id, score=None)
    game_34.game_team_scores = [game_34_win_score, game_34_lose_score]

    game_35_win_score = Game_Team_Score(
        game_id=game_35.id, team_id=uSC.id, score=None)
    game_35_lose_score = Game_Team_Score(
        game_id=game_35.id, team_id=kansas.id, score=None)
    game_35.game_team_scores = [game_35_win_score, game_35_lose_score]

    game_36_win_score = Game_Team_Score(
        game_id=game_36.id, team_id=oregon.id, score=None)
    game_36_lose_score = Game_Team_Score(
        game_id=game_36.id, team_id=iowa.id, score=None)
    game_36.game_team_scores = [game_36_win_score, game_36_lose_score]

    game_37_win_score = Game_Team_Score(
        game_id=game_37.id, team_id=michigan.id, score=None)
    game_37_lose_score = Game_Team_Score(
        game_id=game_37.id, team_id=lSU.id, score=None)
    game_37.game_team_scores = [game_37_win_score, game_37_lose_score]

    game_38_win_score = Game_Team_Score(
        game_id=game_38.id, team_id=colorado.id, score=None)
    game_38_lose_score = Game_Team_Score(
        game_id=game_38.id, team_id=florida_State.id, score=None)
    game_38.game_team_scores = [game_38_win_score, game_38_lose_score]

    game_39_win_score = Game_Team_Score(
        game_id=game_39.id, team_id=uCLA.id, score=None)
    game_39_lose_score = Game_Team_Score(
        game_id=game_39.id, team_id=abilene_Christian.id, score=None)
    game_39.game_team_scores = [game_39_win_score, game_39_lose_score]

    game_40_win_score = Game_Team_Score(
        game_id=game_40.id, team_id=maryland.id, score=None)
    game_40_lose_score = Game_Team_Score(
        game_id=game_40.id, team_id=alabama.id, score=None)
    game_40.game_team_scores = [game_40_win_score, game_40_lose_score]

    game_41_win_score = Game_Team_Score(
        game_id=game_41.id, team_id=baylor.id, score=None)
    game_41_lose_score = Game_Team_Score(
        game_id=game_41.id, team_id=wisconsin.id, score=None)
    game_41.game_team_scores = [game_41_win_score, game_41_lose_score]

    game_42_win_score = Game_Team_Score(
        game_id=game_42.id, team_id=villanova.id, score=None)
    game_42_lose_score = Game_Team_Score(
        game_id=game_42.id, team_id=north_Texas.id, score=None)
    game_42.game_team_scores = [game_42_win_score, game_42_lose_score]

    game_43_win_score = Game_Team_Score(
        game_id=game_43.id, team_id=texas_Tech.id, score=None)
    game_43_lose_score = Game_Team_Score(
        game_id=game_43.id, team_id=arkansas.id, score=None)
    game_43.game_team_scores = [game_43_win_score, game_43_lose_score]

    game_44_win_score = Game_Team_Score(
        game_id=game_44.id, team_id=florida.id, score=None)
    game_44_lose_score = Game_Team_Score(
        game_id=game_44.id, team_id=oral_Roberts.id, score=None)
    game_44.game_team_scores = [game_44_win_score, game_44_lose_score]

    game_45_win_score = Game_Team_Score(
        game_id=game_45.id, team_id=illinois.id, score=None)
    game_45_lose_score = Game_Team_Score(
        game_id=game_45.id, team_id=loyola_Chicago.id, score=None)
    game_45.game_team_scores = [game_45_win_score, game_45_lose_score]

    game_46_win_score = Game_Team_Score(
        game_id=game_46.id, team_id=oregon_State.id, score=None)
    game_46_lose_score = Game_Team_Score(
        game_id=game_46.id, team_id=oklahoma_State.id, score=None)
    game_46.game_team_scores = [game_46_win_score, game_46_lose_score]

    game_47_win_score = Game_Team_Score(
        game_id=game_47.id, team_id=syracuse.id, score=None)
    game_47_lose_score = Game_Team_Score(
        game_id=game_47.id, team_id=west_Virginia.id, score=None)
    game_47.game_team_scores = [game_47_win_score, game_47_lose_score]

    game_48_win_score = Game_Team_Score(
        game_id=game_48.id, team_id=rutgers.id, score=None)
    game_48_lose_score = Game_Team_Score(
        game_id=game_48.id, team_id=houston.id, score=None)
    game_48.game_team_scores = [game_48_win_score, game_48_lose_score]

    db.session.commit()

    print('done')


def undo_2021_tournament_round1():
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
