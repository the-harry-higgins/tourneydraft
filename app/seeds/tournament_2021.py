from app.models import db, March_Madness_Team, College, Game, Game_Team_Score, League, League_User, Draft, Drafted_Team, User, Tournament
import json
from datetime import datetime


def seed_2021_tournament():
    tournament = Tournament(year=2021, region1='West',
                            region2='East', region3='South', region4='Midwest', last_round_completed=0)
    db.session.add(tournament)
    db.session.commit()

    # West
    Gonzaga = College.query.filter(College.name == 'Gonzaga').one()
    gonzaga = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='West', college_id=Gonzaga.id)
    db.session.add(gonzaga)

    Norfolk_State = College.query.filter(College.name == 'Norfolk St.').one()
    norfolk_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='West', college_id=Norfolk_State.id)
    db.session.add(norfolk_State)

    Oklahoma = College.query.filter(College.name == 'Oklahoma').one()
    oklahoma = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='West', college_id=Oklahoma.id)
    db.session.add(oklahoma)

    Missouri = College.query.filter(College.name == 'Missouri').one()
    missouri = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='West', college_id=Missouri.id)
    db.session.add(missouri)

    Creighton = College.query.filter(College.name == 'Creighton').one()
    creighton = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='West', college_id=Creighton.id)
    db.session.add(creighton)

    UCSB = College.query.filter(College.name == 'UCSB').one()
    uCSB = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='West', college_id=UCSB.id)
    db.session.add(uCSB)

    Virginia = College.query.filter(College.name == 'Virginia').one()
    virginia = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='West', college_id=Virginia.id)
    db.session.add(virginia)

    Ohio = College.query.filter(College.name == 'Ohio').one()
    ohio = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='West', college_id=Ohio.id)
    db.session.add(ohio)

    USC = College.query.filter(College.name == 'USC').one()
    uSC = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='West', college_id=USC.id)
    db.session.add(uSC)

    Wichita_State = College.query.filter(College.name == 'Wichita State').one()
    wichita_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='West', college_id=Wichita_State.id)
    db.session.add(wichita_State)

    Kansas = College.query.filter(College.name == 'Kansas').one()
    kansas = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='West', college_id=Kansas.id)
    db.session.add(kansas)

    Eastern_Washington = College.query.filter(
        College.name == 'Eastern Washington').one()
    eastern_Washington = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='West', college_id=Eastern_Washington.id)
    db.session.add(eastern_Washington)

    Oregon = College.query.filter(College.name == 'Oregon').one()
    oregon = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='West', college_id=Oregon.id)
    db.session.add(oregon)

    VCU = College.query.filter(College.name == 'VCU').one()
    vCU = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='West', college_id=VCU.id)
    db.session.add(vCU)

    Iowa = College.query.filter(College.name == 'Iowa').one()
    iowa = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='West', college_id=Iowa.id)
    db.session.add(iowa)

    Grand_Canyon = College.query.filter(College.name == 'Grand Canyon').one()
    grand_Canyon = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='West', college_id=Grand_Canyon.id)
    db.session.add(grand_Canyon)

    # South
    Baylor = College.query.filter(College.name == 'Baylor').one()
    baylor = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='South', college_id=Baylor.id)
    db.session.add(baylor)

    Hartford = College.query.filter(College.name == 'Hartford').one()
    hartford = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='South', college_id=Hartford.id)
    db.session.add(hartford)

    North_Carolina = College.query.filter(
        College.name == 'North Carolina').one()
    north_Carolina = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='South', college_id=North_Carolina.id)
    db.session.add(north_Carolina)

    Wisconsin = College.query.filter(College.name == 'Wisconsin').one()
    wisconsin = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='South', college_id=Wisconsin.id)
    db.session.add(wisconsin)

    Villanova = College.query.filter(College.name == 'Villanova').one()
    villanova = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='South', college_id=Villanova.id)
    db.session.add(villanova)

    Winthrop = College.query.filter(College.name == 'Winthrop').one()
    winthrop = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='South', college_id=Winthrop.id)
    db.session.add(winthrop)

    Purdue = College.query.filter(College.name == 'Purdue').one()
    purdue = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='South', college_id=Purdue.id)
    db.session.add(purdue)

    North_Texas = College.query.filter(College.name == 'North Texas').one()
    north_Texas = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='South', college_id=North_Texas.id)
    db.session.add(north_Texas)

    Texas_Tech = College.query.filter(College.name == 'Texas Tech').one()
    texas_Tech = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='South', college_id=Texas_Tech.id)
    db.session.add(texas_Tech)

    Utah_State = College.query.filter(College.name == 'Utah State').one()
    Utah_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='South', college_id=Utah_State.id)
    db.session.add(Utah_State)

    Arkansas = College.query.filter(College.name == 'Arkansas').one()
    arkansas = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='South', college_id=Arkansas.id)
    db.session.add(arkansas)

    Colgate = College.query.filter(College.name == 'Colgate').one()
    colgate = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='South', college_id=Colgate.id)
    db.session.add(colgate)

    Florida = College.query.filter(College.name == 'Florida').one()
    florida = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='South', college_id=Florida.id)
    db.session.add(florida)

    Virginia_Tech = College.query.filter(College.name == 'Virginia Tech').one()
    virginia_Tech = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='South', college_id=Virginia_Tech.id)
    db.session.add(virginia_Tech)

    Ohio_State = College.query.filter(College.name == 'Ohio State').one()
    ohio_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='South', college_id=Ohio_State.id)
    db.session.add(ohio_State)

    Oral_Roberts = College.query.filter(College.name == 'Oral Roberts').one()
    Oral_Roberts = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='South', college_id=Oral_Roberts.id)
    db.session.add(Oral_Roberts)

    # Midwest
    Illinois = College.query.filter(College.name == 'Illinois').one()
    illinois = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='Midwest', college_id=Illinois.id)
    db.session.add(illinois)

    Drexel = College.query.filter(College.name == 'Drexel').one()
    drexel = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='Midwest', college_id=Drexel.id)
    db.session.add(drexel)

    Loyola_Chicago = College.query.filter(
        College.name == 'Loyola Chicago').one()
    loyola_Chicago = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='Midwest', college_id=Loyola_Chicago.id)
    db.session.add(loyola_Chicago)

    Georgia_Tech = College.query.filter(College.name == 'Georgia Tech').one()
    georgia_Tech = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='Midwest', college_id=Georgia_Tech.id)
    db.session.add(georgia_Tech)

    Tennessee = College.query.filter(College.name == 'Tennessee').one()
    tennessee = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='Midwest', college_id=Tennessee.id)
    db.session.add(tennessee)

    Oregon_State = College.query.filter(College.name == 'Oregon State').one()
    oregon_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='Midwest', college_id=Oregon_State.id)
    db.session.add(oregon_State)

    Oklahoma_State = College.query.filter(
        College.name == 'Oklahoma State').one()
    oklahoma_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='Midwest', college_id=Oklahoma_State.id)
    db.session.add(oklahoma_State)

    Liberty = College.query.filter(College.name == 'Liberty').one()
    liberty = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='Midwest', college_id=Liberty.id)
    db.session.add(liberty)

    San_Diego_State = College.query.filter(
        College.name == 'San Diego State').one()
    san_Diego_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='Midwest', college_id=San_Diego_State.id)
    db.session.add(san_Diego_State)

    Syracuse = College.query.filter(College.name == 'Syracuse').one()
    syracuse = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='Midwest', college_id=Syracuse.id)
    db.session.add(syracuse)

    West_Virginia = College.query.filter(College.name == 'West Virginia').one()
    west_Virginia = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='Midwest', college_id=West_Virginia.id)
    db.session.add(west_Virginia)

    Morehead_State = College.query.filter(
        College.name == 'Morehead State').one()
    morehead_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='Midwest', college_id=Morehead_State.id)
    db.session.add(morehead_State)

    Clemson = College.query.filter(College.name == 'Clemson').one()
    clemson = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='Midwest', college_id=Clemson.id)
    db.session.add(clemson)

    Rutgers = College.query.filter(College.name == 'Rutgers').one()
    rutgers = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='Midwest', college_id=Rutgers.id)
    db.session.add(rutgers)

    Houston = College.query.filter(College.name == 'Houston').one()
    houston = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='Midwest', college_id=Houston.id)
    db.session.add(houston)

    Cleveland_State = College.query.filter(
        College.name == 'Cleveland State').one()
    Cleveland_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='Midwest', college_id=Cleveland_State.id)
    db.session.add(Cleveland_State)

    # East
    Michigan = College.query.filter(College.name == 'Michigan').one()
    michigan = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='East', college_id=Michigan.id)
    db.session.add(michigan)

    Mount_St_Marys = College.query.filter(
        College.name == 'Mount St. Mary\'s').one()
    mount_St_Marys = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='East', college_id=Mount_St_Marys.id)
    db.session.add(mount_St_Marys)

    LSU = College.query.filter(College.name == 'LSU').one()
    lSU = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='East', college_id=LSU.id)
    db.session.add(lSU)

    St_Bonaventure = College.query.filter(
        College.name == 'St. Bonaventure').one()
    st_Bonaventure = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='East', college_id=St_Bonaventure.id)
    db.session.add(st_Bonaventure)

    Colorado = College.query.filter(College.name == 'Colorado').one()
    colorado = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='East', college_id=Colorado.id)
    db.session.add(colorado)

    Georgetown = College.query.filter(College.name == 'Georgetown').one()
    georgetown = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='East', college_id=Georgetown.id)
    db.session.add(georgetown)

    Florida_State = College.query.filter(College.name == 'Florida State').one()
    florida_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='East', college_id=Florida_State.id)
    db.session.add(florida_State)

    UNC_Greensboro = College.query.filter(
        College.name == 'UNC Greensboro').one()
    uNC_Greensboro = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='East', college_id=UNC_Greensboro.id)
    db.session.add(uNC_Greensboro)

    BYU = College.query.filter(College.name == 'BYU').one()
    bYU = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='East', college_id=BYU.id)
    db.session.add(bYU)

    Michigan_State = College.query.filter(
        College.name == 'Michigan State').one()
    michigan_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='East', college_id=Michigan_State.id)
    db.session.add(michigan_State)

    Texas = College.query.filter(College.name == 'Texas').one()
    texas = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='East', college_id=Texas.id)
    db.session.add(texas)

    Abilene_Christian = College.query.filter(
        College.name == 'Abilene Christian').one()
    abilene_Christian = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='East', college_id=Abilene_Christian.id)
    db.session.add(abilene_Christian)

    UCONN = College.query.filter(College.name == 'UCONN').one()
    uCONN = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='East', college_id=UCONN.id)
    db.session.add(uCONN)

    Maryland = College.query.filter(College.name == 'Maryland').one()
    maryland = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='East', college_id=Maryland.id)
    db.session.add(maryland)

    Alabama = College.query.filter(College.name == 'Alabama').one()
    alabama = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='East', college_id=Alabama.id)
    db.session.add(alabama)

    Iona = College.query.filter(College.name == 'Iona').one()
    iona = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='East', college_id=Iona.id)
    db.session.add(iona)

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
        game_id=game_1.id, team_id=norfolk_State.id, score=None)
    game_1.game_team_scores = [game_1_win_score, game_1_lose_score]

    game_2_win_score = Game_Team_Score(
        game_id=game_2.id, team_id=oklahoma.id, score=None)
    game_2_lose_score = Game_Team_Score(
        game_id=game_2.id, team_id=missouri.id, score=None)
    game_2.game_team_scores = [game_2_win_score, game_2_lose_score]

    game_3_win_score = Game_Team_Score(
        game_id=game_3.id, team_id=creighton.id, score=None)
    game_3_lose_score = Game_Team_Score(
        game_id=game_3.id, team_id=uCSB.id, score=None)
    game_3.game_team_scores = [game_3_win_score, game_3_lose_score]

    game_4_win_score = Game_Team_Score(
        game_id=game_4.id, team_id=virginia.id, score=None)
    game_4_lose_score = Game_Team_Score(
        game_id=game_4.id, team_id=ohio.id, score=None)
    game_4.game_team_scores = [game_4_win_score, game_4_lose_score]

    game_5_win_score = Game_Team_Score(
        game_id=game_5.id, team_id=uSC.id, score=None)
    game_5_lose_score = Game_Team_Score(
        game_id=game_5.id, team_id=wichita_State.id, score=None)
    game_5.game_team_scores = [game_5_win_score, game_5_lose_score]

    game_6_win_score = Game_Team_Score(
        game_id=game_6.id, team_id=kansas.id, score=None)
    game_6_lose_score = Game_Team_Score(
        game_id=game_6.id, team_id=eastern_Washington.id, score=None)
    game_6.game_team_scores = [game_6_win_score, game_6_lose_score]

    game_7_win_score = Game_Team_Score(
        game_id=game_7.id, team_id=oregon.id, score=None)
    game_7_lose_score = Game_Team_Score(
        game_id=game_7.id, team_id=vCU.id, score=None)
    game_7.game_team_scores = [game_7_win_score, game_7_lose_score]

    game_8_win_score = Game_Team_Score(
        game_id=game_8.id, team_id=iowa.id, score=None)
    game_8_lose_score = Game_Team_Score(
        game_id=game_8.id, team_id=grand_Canyon.id, score=None)
    game_8.game_team_scores = [game_8_win_score, game_8_lose_score]

    game_9_win_score = Game_Team_Score(
        game_id=game_9.id, team_id=michigan.id, score=None)
    game_9_lose_score = Game_Team_Score(
        game_id=game_9.id, team_id=mount_St_Marys.id, score=None)
    game_9.game_team_scores = [game_9_win_score, game_9_lose_score]

    game_10_win_score = Game_Team_Score(
        game_id=game_10.id, team_id=lSU.id, score=None)
    game_10_lose_score = Game_Team_Score(
        game_id=game_10.id, team_id=st_Bonaventure.id, score=None)
    game_10.game_team_scores = [game_10_win_score, game_10_lose_score]

    game_11_win_score = Game_Team_Score(
        game_id=game_11.id, team_id=colorado.id, score=None)
    game_11_lose_score = Game_Team_Score(
        game_id=game_11.id, team_id=georgetown.id, score=None)
    game_11.game_team_scores = [game_11_win_score, game_11_lose_score]

    game_12_win_score = Game_Team_Score(
        game_id=game_12.id, team_id=florida_State.id, score=None)
    game_12_lose_score = Game_Team_Score(
        game_id=game_12.id, team_id=uNC_Greensboro.id, score=None)
    game_12.game_team_scores = [game_12_win_score, game_12_lose_score]

    game_13_win_score = Game_Team_Score(
        game_id=game_13.id, team_id=bYU.id, score=None)
    game_13_lose_score = Game_Team_Score(
        game_id=game_13.id, team_id=michigan_State.id, score=None)
    game_13.game_team_scores = [game_13_win_score, game_13_lose_score]

    game_14_win_score = Game_Team_Score(
        game_id=game_14.id, team_id=texas.id, score=None)
    game_14_lose_score = Game_Team_Score(
        game_id=game_14.id, team_id=abilene_Christian.id, score=None)
    game_14.game_team_scores = [game_14_win_score, game_14_lose_score]

    game_15_win_score = Game_Team_Score(
        game_id=game_15.id, team_id=uCONN.id, score=None)
    game_15_lose_score = Game_Team_Score(
        game_id=game_15.id, team_id=maryland.id, score=None)
    game_15.game_team_scores = [game_15_win_score, game_15_lose_score]

    game_16_win_score = Game_Team_Score(
        game_id=game_16.id, team_id=alabama.id, score=None)
    game_16_lose_score = Game_Team_Score(
        game_id=game_16.id, team_id=iona.id, score=None)
    game_16.game_team_scores = [game_16_win_score, game_16_lose_score]

    game_17_win_score = Game_Team_Score(
        game_id=game_17.id, team_id=baylor.id, score=None)
    game_17_lose_score = Game_Team_Score(
        game_id=game_17.id, team_id=hartford.id, score=None)
    game_17.game_team_scores = [game_17_win_score, game_17_lose_score]

    game_18_win_score = Game_Team_Score(
        game_id=game_18.id, team_id=north_Carolina.id, score=None)
    game_18_lose_score = Game_Team_Score(
        game_id=game_18.id, team_id=wisconsin.id, score=None)
    game_18.game_team_scores = [game_18_win_score, game_18_lose_score]

    game_19_win_score = Game_Team_Score(
        game_id=game_19.id, team_id=villanova.id, score=None)
    game_19_lose_score = Game_Team_Score(
        game_id=game_19.id, team_id=winthrop.id, score=None)
    game_19.game_team_scores = [game_19_win_score, game_19_lose_score]

    game_20_win_score = Game_Team_Score(
        game_id=game_20.id, team_id=purdue.id, score=None)
    game_20_lose_score = Game_Team_Score(
        game_id=game_20.id, team_id=north_Texas.id, score=None)
    game_20.game_team_scores = [game_20_win_score, game_20_lose_score]

    game_21_win_score = Game_Team_Score(
        game_id=game_21.id, team_id=texas_Tech.id, score=None)
    game_21_lose_score = Game_Team_Score(
        game_id=game_21.id, team_id=Utah_State.id, score=None)
    game_21.game_team_scores = [game_21_win_score, game_21_lose_score]

    game_22_win_score = Game_Team_Score(
        game_id=game_22.id, team_id=arkansas.id, score=None)
    game_22_lose_score = Game_Team_Score(
        game_id=game_22.id, team_id=colgate.id, score=None)
    game_22.game_team_scores = [game_22_win_score, game_22_lose_score]

    game_23_win_score = Game_Team_Score(
        game_id=game_23.id, team_id=florida.id, score=None)
    game_23_lose_score = Game_Team_Score(
        game_id=game_23.id, team_id=virginia_Tech.id, score=None)
    game_23.game_team_scores = [game_23_win_score, game_23_lose_score]

    game_24_win_score = Game_Team_Score(
        game_id=game_24.id, team_id=ohio_State.id, score=None)
    game_24_lose_score = Game_Team_Score(
        game_id=game_24.id, team_id=Oral_Roberts.id, score=None)
    game_24.game_team_scores = [game_24_win_score, game_24_lose_score]

    game_25_win_score = Game_Team_Score(
        game_id=game_25.id, team_id=illinois.id, score=None)
    game_25_lose_score = Game_Team_Score(
        game_id=game_25.id, team_id=drexel.id, score=None)
    game_25.game_team_scores = [game_25_win_score, game_25_lose_score]

    game_26_win_score = Game_Team_Score(
        game_id=game_26.id, team_id=loyola_Chicago.id, score=None)
    game_26_lose_score = Game_Team_Score(
        game_id=game_26.id, team_id=georgia_Tech.id, score=None)
    game_26.game_team_scores = [game_26_win_score, game_26_lose_score]

    game_27_win_score = Game_Team_Score(
        game_id=game_27.id, team_id=tennessee.id, score=None)
    game_27_lose_score = Game_Team_Score(
        game_id=game_27.id, team_id=oregon_State.id, score=None)
    game_27.game_team_scores = [game_27_win_score, game_27_lose_score]

    game_28_win_score = Game_Team_Score(
        game_id=game_28.id, team_id=oklahoma_State.id, score=None)
    game_28_lose_score = Game_Team_Score(
        game_id=game_28.id, team_id=liberty.id, score=None)
    game_28.game_team_scores = [game_28_win_score, game_28_lose_score]

    game_29_win_score = Game_Team_Score(
        game_id=game_29.id, team_id=san_Diego_State.id, score=None)
    game_29_lose_score = Game_Team_Score(
        game_id=game_29.id, team_id=syracuse.id, score=None)
    game_29.game_team_scores = [game_29_win_score, game_29_lose_score]

    game_30_win_score = Game_Team_Score(
        game_id=game_30.id, team_id=west_Virginia.id, score=None)
    game_30_lose_score = Game_Team_Score(
        game_id=game_30.id, team_id=morehead_State.id, score=None)
    game_30.game_team_scores = [game_30_win_score, game_30_lose_score]

    game_31_win_score = Game_Team_Score(
        game_id=game_31.id, team_id=clemson.id, score=None)
    game_31_lose_score = Game_Team_Score(
        game_id=game_31.id, team_id=rutgers.id, score=None)
    game_31.game_team_scores = [game_31_win_score, game_31_lose_score]

    game_32_win_score = Game_Team_Score(
        game_id=game_32.id, team_id=houston.id, score=None)
    game_32_lose_score = Game_Team_Score(
        game_id=game_32.id, team_id=Cleveland_State.id, score=None)
    game_32.game_team_scores = [game_32_win_score, game_32_lose_score]

    db.session.commit()


def undo_2021_tournament():
    tournament = Tournament.query.filter(Tournament.year == 2021).one()

    db.session.execute(
        'DELETE from games WHERE tournament_id = :id', {'id': tournament.id})
    db.session.execute(
        'DELETE from march_madness_teams WHERE tournament_id = :id', {'id': tournament.id})
    db.session.execute(
        'DELETE from march_madness_teams WHERE tournament_id = :id', {'id': tournament.id})
    db.session.execute(
        'DELETE from tournaments WHERE id = :id', {'id': tournament.id})
    db.session.commit()
