from app.models import db, March_Madness_Team, College, Game, Game_Team_Score, League, League_User, Draft, Drafted_Team, User, Tournament
import json
from datetime import datetime


def seed_2019_tournament():
    tournament = Tournament(year=2019, region1='East',
                            region2='West', region3='South', region4='Midwest', last_round_completed=6)
    db.session.add(tournament)
    db.session.commit()

    # East
    Duke = College.query.filter(College.name == 'Duke').one()
    duke = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='East', college_id=Duke.id)
    db.session.add(duke)

    Michigan_State = College.query.filter(
        College.name == 'Michigan State').one()
    michigan_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='East', college_id=Michigan_State.id)
    db.session.add(michigan_State)

    LSU = College.query.filter(College.name == 'LSU').one()
    lSU = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='East', college_id=LSU.id)
    db.session.add(lSU)

    Virginia_Tech = College.query.filter(College.name == 'Virginia Tech').one()
    virginia_Tech = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='East', college_id=Virginia_Tech.id)
    db.session.add(virginia_Tech)

    Mississippi_State = College.query.filter(
        College.name == 'Mississippi State').one()
    mississippi_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='East', college_id=Mississippi_State.id)
    db.session.add(mississippi_State)

    Maryland = College.query.filter(College.name == 'Maryland').one()
    maryland = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='East', college_id=Maryland.id)
    db.session.add(maryland)

    Louisville = College.query.filter(College.name == 'Louisville').one()
    louisville = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='East', college_id=Louisville.id)
    db.session.add(louisville)

    VCU = College.query.filter(College.name == 'VCU').one()
    vCU = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='East', college_id=VCU.id)
    db.session.add(vCU)

    UCF = College.query.filter(College.name == 'UCF').one()
    uCF = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='East', college_id=UCF.id)
    db.session.add(uCF)

    Minnesota = College.query.filter(College.name == 'Minnesota').one()
    minnesota = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='East', college_id=Minnesota.id)
    db.session.add(minnesota)

    Belmont = College.query.filter(College.name == 'Belmont').one()
    belmont = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='East', college_id=Belmont.id)
    db.session.add(belmont)

    Liberty = College.query.filter(College.name == 'Liberty').one()
    liberty = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='East', college_id=Liberty.id)
    db.session.add(liberty)

    Saint_Louis = College.query.filter(College.name == 'Saint Louis').one()
    saint_Louis = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='East', college_id=Saint_Louis.id)
    db.session.add(saint_Louis)

    Yale = College.query.filter(College.name == 'Yale').one()
    yale = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='East', college_id=Yale.id)
    db.session.add(yale)

    Bradley = College.query.filter(College.name == 'Bradley').one()
    bradley = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='East', college_id=Bradley.id)
    db.session.add(bradley)

    North_Dakota_State = College.query.filter(
        College.name == 'North Dakota State').one()
    north_Dakota_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='East', college_id=North_Dakota_State.id)
    db.session.add(north_Dakota_State)

    # South
    Virginia = College.query.filter(College.name == 'Virginia').one()
    virginia = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='South', college_id=Virginia.id)
    db.session.add(virginia)

    Tennessee = College.query.filter(
        College.name == 'Tennessee').one()
    tennessee = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='South', college_id=Tennessee.id)
    db.session.add(tennessee)

    Purdue = College.query.filter(College.name == 'Purdue').one()
    purdue = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='South', college_id=Purdue.id)
    db.session.add(purdue)

    Kansas_State = College.query.filter(College.name == 'Kansas State').one()
    kansas_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='South', college_id=Kansas_State.id)
    db.session.add(kansas_State)

    Wisconsin = College.query.filter(
        College.name == 'Wisconsin').one()
    wisconsin = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='South', college_id=Wisconsin.id)
    db.session.add(wisconsin)

    Villanova = College.query.filter(College.name == 'Villanova').one()
    villanova = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='South', college_id=Villanova.id)
    db.session.add(villanova)

    Cincinnati = College.query.filter(College.name == 'Cincinnati').one()
    cincinnati = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='South', college_id=Cincinnati.id)
    db.session.add(cincinnati)

    Ole_Miss = College.query.filter(College.name == 'Ole Miss').one()
    ole_Miss = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='South', college_id=Ole_Miss.id)
    db.session.add(ole_Miss)

    Oklahoma = College.query.filter(College.name == 'Oklahoma').one()
    oklahoma = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='South', college_id=Oklahoma.id)
    db.session.add(oklahoma)

    Iowa = College.query.filter(College.name == 'Iowa').one()
    iowa = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='South', college_id=Iowa.id)
    db.session.add(iowa)

    Saint_Marys = College.query.filter(College.name == 'Saint Mary\'s').one()
    saint_Marys = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='South', college_id=Saint_Marys.id)
    db.session.add(saint_Marys)

    Oregon = College.query.filter(College.name == 'Oregon').one()
    oregon = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='South', college_id=Oregon.id)
    db.session.add(oregon)

    UC_Irvine = College.query.filter(College.name == 'UC Irvine').one()
    uC_Irvine = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='South', college_id=UC_Irvine.id)
    db.session.add(uC_Irvine)

    Old_Dominion = College.query.filter(College.name == 'Old Dominion').one()
    old_Dominion = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='South', college_id=Old_Dominion.id)
    db.session.add(old_Dominion)

    Colgate = College.query.filter(College.name == 'Colgate').one()
    colgate = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='South', college_id=Colgate.id)
    db.session.add(colgate)

    Gardner_Webb = College.query.filter(College.name == 'Gardner-Webb').one()
    gardner_Webb = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='South', college_id=Gardner_Webb.id)
    db.session.add(gardner_Webb)

    # Midwest
    North_Carolina = College.query.filter(
        College.name == 'North Carolina').one()
    north_Carolina = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='Midwest', college_id=North_Carolina.id)
    db.session.add(north_Carolina)

    Kentucky = College.query.filter(
        College.name == 'Kentucky').one()
    kentucky = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='Midwest', college_id=Kentucky.id)
    db.session.add(kentucky)

    Houston = College.query.filter(College.name == 'Houston').one()
    houston = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='Midwest', college_id=Houston.id)
    db.session.add(houston)

    Kansas = College.query.filter(College.name == 'Kansas').one()
    kansas = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='Midwest', college_id=Kansas.id)
    db.session.add(kansas)

    Auburn = College.query.filter(
        College.name == 'Auburn').one()
    auburn = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='Midwest', college_id=Auburn.id)
    db.session.add(auburn)

    Iowa_State = College.query.filter(College.name == 'Iowa State').one()
    iowa_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='Midwest', college_id=Iowa_State.id)
    db.session.add(iowa_State)

    Wofford = College.query.filter(College.name == 'Wofford').one()
    wofford = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='Midwest', college_id=Wofford.id)
    db.session.add(wofford)

    Utah_State = College.query.filter(College.name == 'Utah State').one()
    utah_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='Midwest', college_id=Utah_State.id)
    db.session.add(utah_State)

    Washington = College.query.filter(College.name == 'Washington').one()
    washington = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='Midwest', college_id=Washington.id)
    db.session.add(washington)

    Seton_Hall = College.query.filter(College.name == 'Seton Hall').one()
    seton_Hall = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='Midwest', college_id=Seton_Hall.id)
    db.session.add(seton_Hall)

    Ohio_State = College.query.filter(College.name == 'Ohio State').one()
    ohio_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='Midwest', college_id=Ohio_State.id)
    db.session.add(ohio_State)

    New_Mexico_State = College.query.filter(
        College.name == 'New Mexico State').one()
    new_Mexico_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='Midwest', college_id=New_Mexico_State.id)
    db.session.add(new_Mexico_State)

    Northeastern = College.query.filter(College.name == 'Northeastern').one()
    northeastern = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='Midwest', college_id=Northeastern.id)
    db.session.add(northeastern)

    Georgia_State = College.query.filter(College.name == 'Georgia State').one()
    georgia_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='Midwest', college_id=Georgia_State.id)
    db.session.add(georgia_State)

    Abilene_Christian = College.query.filter(
        College.name == 'Abilene Christian').one()
    abilene_Christian = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='Midwest', college_id=Abilene_Christian.id)
    db.session.add(abilene_Christian)

    Iona = College.query.filter(College.name == 'Iona').one()
    iona = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='Midwest', college_id=Iona.id)
    db.session.add(iona)

    # West
    Gonzaga = College.query.filter(College.name == 'Gonzaga').one()
    gonzaga = March_Madness_Team(
        tournament_id=tournament.id, seed_number=1, region='West', college_id=Gonzaga.id)
    db.session.add(gonzaga)

    Michigan = College.query.filter(
        College.name == 'Michigan').one()
    michigan = March_Madness_Team(
        tournament_id=tournament.id, seed_number=2, region='West', college_id=Michigan.id)
    db.session.add(michigan)

    Texas_Tech = College.query.filter(College.name == 'Texas Tech').one()
    texas_Tech = March_Madness_Team(
        tournament_id=tournament.id, seed_number=3, region='West', college_id=Texas_Tech.id)
    db.session.add(texas_Tech)

    Florida_State = College.query.filter(College.name == 'Florida State').one()
    florida_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=4, region='West', college_id=Florida_State.id)
    db.session.add(florida_State)

    Marquette = College.query.filter(
        College.name == 'Marquette').one()
    marquette = March_Madness_Team(
        tournament_id=tournament.id, seed_number=5, region='West', college_id=Marquette.id)
    db.session.add(marquette)

    Buffalo = College.query.filter(College.name == 'Buffalo').one()
    buffalo = March_Madness_Team(
        tournament_id=tournament.id, seed_number=6, region='West', college_id=Buffalo.id)
    db.session.add(buffalo)

    Nevada = College.query.filter(College.name == 'Nevada').one()
    nevada = March_Madness_Team(
        tournament_id=tournament.id, seed_number=7, region='West', college_id=Nevada.id)
    db.session.add(nevada)

    Syracuse = College.query.filter(College.name == 'Syracuse').one()
    syracuse = March_Madness_Team(
        tournament_id=tournament.id, seed_number=8, region='West', college_id=Syracuse.id)
    db.session.add(syracuse)

    Baylor = College.query.filter(College.name == 'Baylor').one()
    baylor = March_Madness_Team(
        tournament_id=tournament.id, seed_number=9, region='West', college_id=Baylor.id)
    db.session.add(baylor)

    Florida = College.query.filter(College.name == 'Florida').one()
    florida = March_Madness_Team(
        tournament_id=tournament.id, seed_number=10, region='West', college_id=Florida.id)
    db.session.add(florida)

    Arizona_State = College.query.filter(College.name == 'Arizona State').one()
    arizona_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=11, region='West', college_id=Arizona_State.id)
    db.session.add(arizona_State)

    Murray_State = College.query.filter(College.name == 'Murray State').one()
    murray_State = March_Madness_Team(
        tournament_id=tournament.id, seed_number=12, region='West', college_id=Murray_State.id)
    db.session.add(murray_State)

    Vermont = College.query.filter(College.name == 'Vermont').one()
    vermont = March_Madness_Team(
        tournament_id=tournament.id, seed_number=13, region='West', college_id=Vermont.id)
    db.session.add(vermont)

    Northern_Kentucky = College.query.filter(
        College.name == 'Northern Kentucky').one()
    northern_Kentucky = March_Madness_Team(
        tournament_id=tournament.id, seed_number=14, region='West', college_id=Northern_Kentucky.id)
    db.session.add(northern_Kentucky)

    Montana = College.query.filter(College.name == 'Montana').one()
    montana = March_Madness_Team(
        tournament_id=tournament.id, seed_number=15, region='West', college_id=Montana.id)
    db.session.add(montana)

    Fairleigh_Dickinson = College.query.filter(
        College.name == 'Fairleigh Dickinson').one()
    fairleigh_Dickinson = March_Madness_Team(
        tournament_id=tournament.id, seed_number=16, region='West', college_id=Fairleigh_Dickinson.id)
    db.session.add(fairleigh_Dickinson)

    db.session.commit()

    game_1 = Game(game_num=1, round_num=1, winning_team_id=duke.id,
                  tournament_id=tournament.id)
    db.session.add(game_1)
    game_2 = Game(game_num=2, round_num=1, winning_team_id=uCF.id,
                  tournament_id=tournament.id)
    db.session.add(game_2)
    game_3 = Game(game_num=3, round_num=1, winning_team_id=liberty.id,
                  tournament_id=tournament.id)
    db.session.add(game_3)
    game_4 = Game(game_num=4, round_num=1, winning_team_id=virginia_Tech.id,
                  tournament_id=tournament.id)
    db.session.add(game_4)
    game_5 = Game(game_num=5, round_num=1, winning_team_id=maryland.id,
                  tournament_id=tournament.id)
    db.session.add(game_5)
    game_6 = Game(game_num=6, round_num=1, winning_team_id=lSU.id,
                  tournament_id=tournament.id)
    db.session.add(game_6)
    game_7 = Game(game_num=7, round_num=1, winning_team_id=minnesota.id,
                  tournament_id=tournament.id)
    db.session.add(game_7)
    game_8 = Game(game_num=8, round_num=1, winning_team_id=michigan_State.id,
                  tournament_id=tournament.id)
    db.session.add(game_8)
    game_9 = Game(game_num=9, round_num=1, winning_team_id=gonzaga.id,
                  tournament_id=tournament.id)
    db.session.add(game_9)
    game_10 = Game(game_num=10, round_num=1,
                   winning_team_id=baylor.id, tournament_id=tournament.id)
    db.session.add(game_10)
    game_11 = Game(game_num=11, round_num=1,
                   winning_team_id=murray_State.id, tournament_id=tournament.id)
    db.session.add(game_11)
    game_12 = Game(game_num=12, round_num=1,
                   winning_team_id=florida_State.id, tournament_id=tournament.id)
    db.session.add(game_12)
    game_13 = Game(game_num=13, round_num=1,
                   winning_team_id=buffalo.id, tournament_id=tournament.id)
    db.session.add(game_13)
    game_14 = Game(game_num=14, round_num=1,
                   winning_team_id=texas_Tech.id, tournament_id=tournament.id)
    db.session.add(game_14)
    game_15 = Game(game_num=15, round_num=1,
                   winning_team_id=florida.id, tournament_id=tournament.id)
    db.session.add(game_15)
    game_16 = Game(game_num=16, round_num=1,
                   winning_team_id=michigan.id, tournament_id=tournament.id)
    db.session.add(game_16)
    game_17 = Game(game_num=17, round_num=1,
                   winning_team_id=virginia.id, tournament_id=tournament.id)
    db.session.add(game_17)
    game_18 = Game(game_num=18, round_num=1,
                   winning_team_id=oklahoma.id, tournament_id=tournament.id)
    db.session.add(game_18)
    game_19 = Game(game_num=19, round_num=1,
                   winning_team_id=oregon.id, tournament_id=tournament.id)
    db.session.add(game_19)
    game_20 = Game(game_num=20, round_num=1,
                   winning_team_id=uC_Irvine.id, tournament_id=tournament.id)
    db.session.add(game_20)
    game_21 = Game(game_num=21, round_num=1,
                   winning_team_id=villanova.id, tournament_id=tournament.id)
    db.session.add(game_21)
    game_22 = Game(game_num=22, round_num=1,
                   winning_team_id=purdue.id, tournament_id=tournament.id)
    db.session.add(game_22)
    game_23 = Game(game_num=23, round_num=1,
                   winning_team_id=iowa.id, tournament_id=tournament.id)
    db.session.add(game_23)
    game_24 = Game(game_num=24, round_num=1,
                   winning_team_id=tennessee.id, tournament_id=tournament.id)
    db.session.add(game_24)
    game_25 = Game(game_num=25, round_num=1,
                   winning_team_id=north_Carolina.id, tournament_id=tournament.id)
    db.session.add(game_25)
    game_26 = Game(game_num=26, round_num=1,
                   winning_team_id=washington.id, tournament_id=tournament.id)
    db.session.add(game_26)
    game_27 = Game(game_num=27, round_num=1,
                   winning_team_id=auburn.id, tournament_id=tournament.id)
    db.session.add(game_27)
    game_28 = Game(game_num=28, round_num=1,
                   winning_team_id=kansas.id, tournament_id=tournament.id)
    db.session.add(game_28)
    game_29 = Game(game_num=29, round_num=1,
                   winning_team_id=ohio_State.id, tournament_id=tournament.id)
    db.session.add(game_29)
    game_30 = Game(game_num=30, round_num=1,
                   winning_team_id=houston.id, tournament_id=tournament.id)
    db.session.add(game_30)
    game_31 = Game(game_num=31, round_num=1,
                   winning_team_id=wofford.id, tournament_id=tournament.id)
    db.session.add(game_31)
    game_32 = Game(game_num=32, round_num=1,
                   winning_team_id=kentucky.id, tournament_id=tournament.id)
    db.session.add(game_32)
    game_33 = Game(game_num=33, round_num=2,
                   winning_team_id=duke.id, tournament_id=tournament.id)
    db.session.add(game_33)
    game_34 = Game(game_num=34, round_num=2,
                   winning_team_id=virginia_Tech.id, tournament_id=tournament.id)
    db.session.add(game_34)
    game_35 = Game(game_num=35, round_num=2,
                   winning_team_id=lSU.id, tournament_id=tournament.id)
    db.session.add(game_35)
    game_36 = Game(game_num=36, round_num=2,
                   winning_team_id=michigan_State.id, tournament_id=tournament.id)
    db.session.add(game_36)
    game_37 = Game(game_num=37, round_num=2,
                   winning_team_id=gonzaga.id, tournament_id=tournament.id)
    db.session.add(game_37)
    game_38 = Game(game_num=38, round_num=2,
                   winning_team_id=florida_State.id, tournament_id=tournament.id)
    db.session.add(game_38)
    game_39 = Game(game_num=39, round_num=2,
                   winning_team_id=texas_Tech.id, tournament_id=tournament.id)
    db.session.add(game_39)
    game_40 = Game(game_num=40, round_num=2,
                   winning_team_id=michigan.id, tournament_id=tournament.id)
    db.session.add(game_40)
    game_41 = Game(game_num=41, round_num=2,
                   winning_team_id=virginia.id, tournament_id=tournament.id)
    db.session.add(game_41)
    game_42 = Game(game_num=42, round_num=2,
                   winning_team_id=oregon.id, tournament_id=tournament.id)
    db.session.add(game_42)
    game_43 = Game(game_num=43, round_num=2,
                   winning_team_id=purdue.id, tournament_id=tournament.id)
    db.session.add(game_43)
    game_44 = Game(game_num=44, round_num=2,
                   winning_team_id=tennessee.id, tournament_id=tournament.id)
    db.session.add(game_44)
    game_45 = Game(game_num=45, round_num=2,
                   winning_team_id=north_Carolina.id, tournament_id=tournament.id)
    db.session.add(game_45)
    game_46 = Game(game_num=46, round_num=2,
                   winning_team_id=auburn.id, tournament_id=tournament.id)
    db.session.add(game_46)
    game_47 = Game(game_num=47, round_num=2,
                   winning_team_id=houston.id, tournament_id=tournament.id)
    db.session.add(game_47)
    game_48 = Game(game_num=48, round_num=2,
                   winning_team_id=kentucky.id, tournament_id=tournament.id)
    db.session.add(game_48)
    game_49 = Game(game_num=49, round_num=3,
                   winning_team_id=duke.id, tournament_id=tournament.id)
    db.session.add(game_49)
    game_50 = Game(game_num=50, round_num=3,
                   winning_team_id=michigan_State.id, tournament_id=tournament.id)
    db.session.add(game_50)
    game_51 = Game(game_num=51, round_num=3,
                   winning_team_id=gonzaga.id, tournament_id=tournament.id)
    db.session.add(game_51)
    game_52 = Game(game_num=52, round_num=3,
                   winning_team_id=texas_Tech.id, tournament_id=tournament.id)
    db.session.add(game_52)
    game_53 = Game(game_num=53, round_num=3,
                   winning_team_id=virginia.id, tournament_id=tournament.id)
    db.session.add(game_53)
    game_54 = Game(game_num=54, round_num=3,
                   winning_team_id=purdue.id, tournament_id=tournament.id)
    db.session.add(game_54)
    game_55 = Game(game_num=55, round_num=3,
                   winning_team_id=auburn.id, tournament_id=tournament.id)
    db.session.add(game_55)
    game_56 = Game(game_num=56, round_num=3,
                   winning_team_id=kentucky.id, tournament_id=tournament.id)
    db.session.add(game_56)
    game_57 = Game(game_num=57, round_num=4,
                   winning_team_id=michigan_State.id, tournament_id=tournament.id)
    db.session.add(game_57)
    game_58 = Game(game_num=58, round_num=4,
                   winning_team_id=texas_Tech.id, tournament_id=tournament.id)
    db.session.add(game_58)
    game_59 = Game(game_num=59, round_num=4,
                   winning_team_id=virginia.id, tournament_id=tournament.id)
    db.session.add(game_59)
    game_60 = Game(game_num=60, round_num=4,
                   winning_team_id=auburn.id, tournament_id=tournament.id)
    db.session.add(game_60)
    game_61 = Game(game_num=61, round_num=5,
                   winning_team_id=texas_Tech.id, tournament_id=tournament.id)
    db.session.add(game_61)
    game_62 = Game(game_num=62, round_num=5,
                   winning_team_id=virginia.id, tournament_id=tournament.id)
    db.session.add(game_62)
    game_63 = Game(game_num=63, round_num=6,
                   winning_team_id=virginia.id, tournament_id=tournament.id)
    db.session.add(game_63)
    db.session.commit()

    game_1_win_score = Game_Team_Score(
        game_id=game_1.id, team_id=duke.id, score=85)
    game_1_lose_score = Game_Team_Score(
        game_id=game_1.id, team_id=north_Dakota_State.id, score=62)
    game_1.game_team_scores = [game_1_win_score, game_1_lose_score]
    game_1.child_game_id = game_33.id

    game_2_win_score = Game_Team_Score(
        game_id=game_2.id, team_id=uCF.id, score=73)
    game_2_lose_score = Game_Team_Score(
        game_id=game_2.id, team_id=vCU.id, score=58)
    game_2.game_team_scores = [game_2_win_score, game_2_lose_score]
    game_2.child_game_id = game_33.id

    game_3_win_score = Game_Team_Score(
        game_id=game_3.id, team_id=liberty.id, score=80)
    game_3_lose_score = Game_Team_Score(
        game_id=game_3.id, team_id=mississippi_State.id, score=76)
    game_3.game_team_scores = [game_3_win_score, game_3_lose_score]
    game_3.child_game_id = game_34.id

    game_4_win_score = Game_Team_Score(
        game_id=game_4.id, team_id=virginia_Tech.id, score=66)
    game_4_lose_score = Game_Team_Score(
        game_id=game_4.id, team_id=saint_Louis.id, score=52)
    game_4.game_team_scores = [game_4_win_score, game_4_lose_score]
    game_4.child_game_id = game_34.id

    game_5_win_score = Game_Team_Score(
        game_id=game_5.id, team_id=maryland.id, score=79)
    game_5_lose_score = Game_Team_Score(
        game_id=game_5.id, team_id=belmont.id, score=77)
    game_5.game_team_scores = [game_5_win_score, game_5_lose_score]
    game_5.child_game_id = game_35.id

    game_6_win_score = Game_Team_Score(
        game_id=game_6.id, team_id=lSU.id, score=79)
    game_6_lose_score = Game_Team_Score(
        game_id=game_6.id, team_id=yale.id, score=74)
    game_6.game_team_scores = [game_6_win_score, game_6_lose_score]
    game_6.child_game_id = game_35.id

    game_7_win_score = Game_Team_Score(
        game_id=game_7.id, team_id=minnesota.id, score=86)
    game_7_lose_score = Game_Team_Score(
        game_id=game_7.id, team_id=louisville.id, score=76)
    game_7.game_team_scores = [game_7_win_score, game_7_lose_score]
    game_7.child_game_id = game_36.id

    game_8_win_score = Game_Team_Score(
        game_id=game_8.id, team_id=michigan_State.id, score=76)
    game_8_lose_score = Game_Team_Score(
        game_id=game_8.id, team_id=bradley.id, score=65)
    game_8.game_team_scores = [game_8_win_score, game_8_lose_score]
    game_8.child_game_id = game_36.id

    game_9_win_score = Game_Team_Score(
        game_id=game_9.id, team_id=gonzaga.id, score=87)
    game_9_lose_score = Game_Team_Score(
        game_id=game_9.id, team_id=fairleigh_Dickinson.id, score=49)
    game_9.game_team_scores = [game_9_win_score, game_9_lose_score]
    game_9.child_game_id = game_37.id

    game_10_win_score = Game_Team_Score(
        game_id=game_10.id, team_id=baylor.id, score=78)
    game_10_lose_score = Game_Team_Score(
        game_id=game_10.id, team_id=syracuse.id, score=69)
    game_10.game_team_scores = [game_10_win_score, game_10_lose_score]
    game_10.child_game_id = game_37.id

    game_11_win_score = Game_Team_Score(
        game_id=game_11.id, team_id=murray_State.id, score=83)
    game_11_lose_score = Game_Team_Score(
        game_id=game_11.id, team_id=marquette.id, score=64)
    game_11.game_team_scores = [game_11_win_score, game_11_lose_score]
    game_11.child_game_id = game_38.id

    game_12_win_score = Game_Team_Score(
        game_id=game_12.id, team_id=florida_State.id, score=76)
    game_12_lose_score = Game_Team_Score(
        game_id=game_12.id, team_id=vermont.id, score=69)
    game_12.game_team_scores = [game_12_win_score, game_12_lose_score]
    game_12.child_game_id = game_38.id

    game_13_win_score = Game_Team_Score(
        game_id=game_13.id, team_id=buffalo.id, score=91)
    game_13_lose_score = Game_Team_Score(
        game_id=game_13.id, team_id=arizona_State.id, score=74)
    game_13.game_team_scores = [game_13_win_score, game_13_lose_score]
    game_13.child_game_id = game_39.id

    game_14_win_score = Game_Team_Score(
        game_id=game_14.id, team_id=texas_Tech.id, score=72)
    game_14_lose_score = Game_Team_Score(
        game_id=game_14.id, team_id=northern_Kentucky.id, score=57)
    game_14.game_team_scores = [game_14_win_score, game_14_lose_score]
    game_14.child_game_id = game_39.id

    game_15_win_score = Game_Team_Score(
        game_id=game_15.id, team_id=florida.id, score=70)
    game_15_lose_score = Game_Team_Score(
        game_id=game_15.id, team_id=nevada.id, score=61)
    game_15.game_team_scores = [game_15_win_score, game_15_lose_score]
    game_15.child_game_id = game_40.id

    game_16_win_score = Game_Team_Score(
        game_id=game_16.id, team_id=michigan.id, score=74)
    game_16_lose_score = Game_Team_Score(
        game_id=game_16.id, team_id=montana.id, score=55)
    game_16.game_team_scores = [game_16_win_score, game_16_lose_score]
    game_16.child_game_id = game_40.id

    game_17_win_score = Game_Team_Score(
        game_id=game_17.id, team_id=virginia.id, score=71)
    game_17_lose_score = Game_Team_Score(
        game_id=game_17.id, team_id=gardner_Webb.id, score=56)
    game_17.game_team_scores = [game_17_win_score, game_17_lose_score]
    game_17.child_game_id = game_41.id

    game_18_win_score = Game_Team_Score(
        game_id=game_18.id, team_id=oklahoma.id, score=95)
    game_18_lose_score = Game_Team_Score(
        game_id=game_18.id, team_id=ole_Miss.id, score=72)
    game_18.game_team_scores = [game_18_win_score, game_18_lose_score]
    game_18.child_game_id = game_41.id

    game_19_win_score = Game_Team_Score(
        game_id=game_19.id, team_id=oregon.id, score=72)
    game_19_lose_score = Game_Team_Score(
        game_id=game_19.id, team_id=wisconsin.id, score=54)
    game_19.game_team_scores = [game_19_win_score, game_19_lose_score]
    game_19.child_game_id = game_42.id

    game_20_win_score = Game_Team_Score(
        game_id=game_20.id, team_id=uC_Irvine.id, score=70)
    game_20_lose_score = Game_Team_Score(
        game_id=game_20.id, team_id=kansas_State.id, score=64)
    game_20.game_team_scores = [game_20_win_score, game_20_lose_score]
    game_20.child_game_id = game_42.id

    game_21_win_score = Game_Team_Score(
        game_id=game_21.id, team_id=villanova.id, score=61)
    game_21_lose_score = Game_Team_Score(
        game_id=game_21.id, team_id=saint_Marys.id, score=57)
    game_21.game_team_scores = [game_21_win_score, game_21_lose_score]
    game_21.child_game_id = game_43.id

    game_22_win_score = Game_Team_Score(
        game_id=game_22.id, team_id=purdue.id, score=61)
    game_22_lose_score = Game_Team_Score(
        game_id=game_22.id, team_id=old_Dominion.id, score=48)
    game_22.game_team_scores = [game_22_win_score, game_22_lose_score]
    game_22.child_game_id = game_43.id

    game_23_win_score = Game_Team_Score(
        game_id=game_23.id, team_id=iowa.id, score=79)
    game_23_lose_score = Game_Team_Score(
        game_id=game_23.id, team_id=cincinnati.id, score=72)
    game_23.game_team_scores = [game_23_win_score, game_23_lose_score]
    game_23.child_game_id = game_44.id

    game_24_win_score = Game_Team_Score(
        game_id=game_24.id, team_id=tennessee.id, score=77)
    game_24_lose_score = Game_Team_Score(
        game_id=game_24.id, team_id=colgate.id, score=70)
    game_24.game_team_scores = [game_24_win_score, game_24_lose_score]
    game_24.child_game_id = game_44.id

    game_25_win_score = Game_Team_Score(
        game_id=game_25.id, team_id=north_Carolina.id, score=88)
    game_25_lose_score = Game_Team_Score(
        game_id=game_25.id, team_id=iona.id, score=73)
    game_25.game_team_scores = [game_25_win_score, game_25_lose_score]
    game_25.child_game_id = game_45.id

    game_26_win_score = Game_Team_Score(
        game_id=game_26.id, team_id=washington.id, score=78)
    game_26_lose_score = Game_Team_Score(
        game_id=game_26.id, team_id=utah_State.id, score=61)
    game_26.game_team_scores = [game_26_win_score, game_26_lose_score]
    game_26.child_game_id = game_45.id

    game_27_win_score = Game_Team_Score(
        game_id=game_27.id, team_id=auburn.id, score=78)
    game_27_lose_score = Game_Team_Score(
        game_id=game_27.id, team_id=new_Mexico_State.id, score=77)
    game_27.game_team_scores = [game_27_win_score, game_27_lose_score]
    game_27.child_game_id = game_46.id

    game_28_win_score = Game_Team_Score(
        game_id=game_28.id, team_id=kansas.id, score=87)
    game_28_lose_score = Game_Team_Score(
        game_id=game_28.id, team_id=northeastern.id, score=53)
    game_28.game_team_scores = [game_28_win_score, game_28_lose_score]
    game_28.child_game_id = game_46.id

    game_29_win_score = Game_Team_Score(
        game_id=game_29.id, team_id=ohio_State.id, score=62)
    game_29_lose_score = Game_Team_Score(
        game_id=game_29.id, team_id=iowa_State.id, score=59)
    game_29.game_team_scores = [game_29_win_score, game_29_lose_score]
    game_29.child_game_id = game_47.id

    game_30_win_score = Game_Team_Score(
        game_id=game_30.id, team_id=houston.id, score=84)
    game_30_lose_score = Game_Team_Score(
        game_id=game_30.id, team_id=georgia_State.id, score=55)
    game_30.game_team_scores = [game_30_win_score, game_30_lose_score]
    game_30.child_game_id = game_47.id

    game_31_win_score = Game_Team_Score(
        game_id=game_31.id, team_id=wofford.id, score=84)
    game_31_lose_score = Game_Team_Score(
        game_id=game_31.id, team_id=seton_Hall.id, score=68)
    game_31.game_team_scores = [game_31_win_score, game_31_lose_score]
    game_31.child_game_id = game_48.id

    game_32_win_score = Game_Team_Score(
        game_id=game_32.id, team_id=kentucky.id, score=79)
    game_32_lose_score = Game_Team_Score(
        game_id=game_32.id, team_id=abilene_Christian.id, score=44)
    game_32.game_team_scores = [game_32_win_score, game_32_lose_score]
    game_32.child_game_id = game_48.id

    game_33_win_score = Game_Team_Score(
        game_id=game_33.id, team_id=duke.id, score=77)
    game_33_lose_score = Game_Team_Score(
        game_id=game_33.id, team_id=uCF.id, score=76)
    game_33.game_team_scores = [game_33_win_score, game_33_lose_score]
    game_33.child_game_id = game_49.id

    game_34_win_score = Game_Team_Score(
        game_id=game_34.id, team_id=virginia_Tech.id, score=67)
    game_34_lose_score = Game_Team_Score(
        game_id=game_34.id, team_id=liberty.id, score=58)
    game_34.game_team_scores = [game_34_win_score, game_34_lose_score]
    game_34.child_game_id = game_49.id

    game_35_win_score = Game_Team_Score(
        game_id=game_35.id, team_id=lSU.id, score=69)
    game_35_lose_score = Game_Team_Score(
        game_id=game_35.id, team_id=maryland.id, score=67)
    game_35.game_team_scores = [game_35_win_score, game_35_lose_score]
    game_35.child_game_id = game_50.id

    game_36_win_score = Game_Team_Score(
        game_id=game_36.id, team_id=michigan_State.id, score=70)
    game_36_lose_score = Game_Team_Score(
        game_id=game_36.id, team_id=minnesota.id, score=50)
    game_36.game_team_scores = [game_36_win_score, game_36_lose_score]
    game_36.child_game_id = game_50.id

    game_37_win_score = Game_Team_Score(
        game_id=game_37.id, team_id=gonzaga.id, score=83)
    game_37_lose_score = Game_Team_Score(
        game_id=game_37.id, team_id=baylor.id, score=71)
    game_37.game_team_scores = [game_37_win_score, game_37_lose_score]
    game_37.child_game_id = game_51.id

    game_38_win_score = Game_Team_Score(
        game_id=game_38.id, team_id=florida_State.id, score=90)
    game_38_lose_score = Game_Team_Score(
        game_id=game_38.id, team_id=murray_State.id, score=62)
    game_38.game_team_scores = [game_38_win_score, game_38_lose_score]
    game_38.child_game_id = game_51.id

    game_39_win_score = Game_Team_Score(
        game_id=game_39.id, team_id=texas_Tech.id, score=78)
    game_39_lose_score = Game_Team_Score(
        game_id=game_39.id, team_id=buffalo.id, score=58)
    game_39.game_team_scores = [game_39_win_score, game_39_lose_score]
    game_39.child_game_id = game_52.id

    game_40_win_score = Game_Team_Score(
        game_id=game_40.id, team_id=michigan.id, score=64)
    game_40_lose_score = Game_Team_Score(
        game_id=game_40.id, team_id=florida.id, score=49)
    game_40.game_team_scores = [game_40_win_score, game_40_lose_score]
    game_40.child_game_id = game_52.id

    game_41_win_score = Game_Team_Score(
        game_id=game_41.id, team_id=virginia.id, score=63)
    game_41_lose_score = Game_Team_Score(
        game_id=game_41.id, team_id=oklahoma.id, score=51)
    game_41.game_team_scores = [game_41_win_score, game_41_lose_score]
    game_41.child_game_id = game_53.id

    game_42_win_score = Game_Team_Score(
        game_id=game_42.id, team_id=oregon.id, score=73)
    game_42_lose_score = Game_Team_Score(
        game_id=game_42.id, team_id=uC_Irvine.id, score=54)
    game_42.game_team_scores = [game_42_win_score, game_42_lose_score]
    game_42.child_game_id = game_53.id

    game_43_win_score = Game_Team_Score(
        game_id=game_43.id, team_id=purdue.id, score=87)
    game_43_lose_score = Game_Team_Score(
        game_id=game_43.id, team_id=villanova.id, score=61)
    game_43.game_team_scores = [game_43_win_score, game_43_lose_score]
    game_43.child_game_id = game_54.id

    game_44_win_score = Game_Team_Score(
        game_id=game_44.id, team_id=tennessee.id, score=83)
    game_44_lose_score = Game_Team_Score(
        game_id=game_44.id, team_id=iowa.id, score=77)
    game_44.game_team_scores = [game_44_win_score, game_44_lose_score]
    game_44.child_game_id = game_54.id

    game_45_win_score = Game_Team_Score(
        game_id=game_45.id, team_id=north_Carolina.id, score=81)
    game_45_lose_score = Game_Team_Score(
        game_id=game_45.id, team_id=washington.id, score=59)
    game_45.game_team_scores = [game_45_win_score, game_45_lose_score]
    game_45.child_game_id = game_55.id

    game_46_win_score = Game_Team_Score(
        game_id=game_46.id, team_id=auburn.id, score=89)
    game_46_lose_score = Game_Team_Score(
        game_id=game_46.id, team_id=kansas.id, score=75)
    game_46.game_team_scores = [game_46_win_score, game_46_lose_score]
    game_46.child_game_id = game_55.id

    game_47_win_score = Game_Team_Score(
        game_id=game_47.id, team_id=houston.id, score=74)
    game_47_lose_score = Game_Team_Score(
        game_id=game_47.id, team_id=ohio_State.id, score=59)
    game_47.game_team_scores = [game_47_win_score, game_47_lose_score]
    game_47.child_game_id = game_56.id

    game_48_win_score = Game_Team_Score(
        game_id=game_48.id, team_id=kentucky.id, score=62)
    game_48_lose_score = Game_Team_Score(
        game_id=game_48.id, team_id=wofford.id, score=56)
    game_48.game_team_scores = [game_48_win_score, game_48_lose_score]
    game_48.child_game_id = game_56.id

    game_49_win_score = Game_Team_Score(
        game_id=game_49.id, team_id=duke.id, score=75)
    game_49_lose_score = Game_Team_Score(
        game_id=game_49.id, team_id=virginia_Tech.id, score=73)
    game_49.game_team_scores = [game_49_win_score, game_49_lose_score]
    game_49.child_game_id = game_57.id

    game_50_win_score = Game_Team_Score(
        game_id=game_50.id, team_id=michigan_State.id, score=80)
    game_50_lose_score = Game_Team_Score(
        game_id=game_50.id, team_id=lSU.id, score=63)
    game_50.game_team_scores = [game_50_win_score, game_50_lose_score]
    game_50.child_game_id = game_57.id

    game_51_win_score = Game_Team_Score(
        game_id=game_51.id, team_id=gonzaga.id, score=72)
    game_51_lose_score = Game_Team_Score(
        game_id=game_51.id, team_id=florida_State.id, score=58)
    game_51.game_team_scores = [game_51_win_score, game_51_lose_score]
    game_51.child_game_id = game_58.id

    game_52_win_score = Game_Team_Score(
        game_id=game_52.id, team_id=texas_Tech.id, score=63)
    game_52_lose_score = Game_Team_Score(
        game_id=game_52.id, team_id=michigan.id, score=44)
    game_52.game_team_scores = [game_52_win_score, game_52_lose_score]
    game_52.child_game_id = game_58.id

    game_53_win_score = Game_Team_Score(
        game_id=game_53.id, team_id=virginia.id, score=53)
    game_53_lose_score = Game_Team_Score(
        game_id=game_53.id, team_id=oregon.id, score=49)
    game_53.game_team_scores = [game_53_win_score, game_53_lose_score]
    game_53.child_game_id = game_59.id

    game_54_win_score = Game_Team_Score(
        game_id=game_54.id, team_id=purdue.id, score=99)
    game_54_lose_score = Game_Team_Score(
        game_id=game_54.id, team_id=tennessee.id, score=94)
    game_54.game_team_scores = [game_54_win_score, game_54_lose_score]
    game_54.child_game_id = game_59.id

    game_55_win_score = Game_Team_Score(
        game_id=game_55.id, team_id=auburn.id, score=97)
    game_55_lose_score = Game_Team_Score(
        game_id=game_55.id, team_id=north_Carolina.id, score=80)
    game_55.game_team_scores = [game_55_win_score, game_55_lose_score]
    game_55.child_game_id = game_60.id

    game_56_win_score = Game_Team_Score(
        game_id=game_56.id, team_id=kentucky.id, score=62)
    game_56_lose_score = Game_Team_Score(
        game_id=game_56.id, team_id=houston.id, score=58)
    game_56.game_team_scores = [game_56_win_score, game_56_lose_score]
    game_56.child_game_id = game_60.id

    game_57_win_score = Game_Team_Score(
        game_id=game_57.id, team_id=michigan_State.id, score=68)
    game_57_lose_score = Game_Team_Score(
        game_id=game_57.id, team_id=duke.id, score=67)
    game_57.game_team_scores = [game_57_win_score, game_57_lose_score]
    game_57.child_game_id = game_61.id

    game_58_win_score = Game_Team_Score(
        game_id=game_58.id, team_id=texas_Tech.id, score=75)
    game_58_lose_score = Game_Team_Score(
        game_id=game_58.id, team_id=gonzaga.id, score=69)
    game_58.game_team_scores = [game_58_win_score, game_58_lose_score]
    game_58.child_game_id = game_61.id

    game_59_win_score = Game_Team_Score(
        game_id=game_59.id, team_id=virginia.id, score=80)
    game_59_lose_score = Game_Team_Score(
        game_id=game_59.id, team_id=purdue.id, score=75)
    game_59.game_team_scores = [game_59_win_score, game_59_lose_score]
    game_59.child_game_id = game_62.id

    game_60_win_score = Game_Team_Score(
        game_id=game_60.id, team_id=auburn.id, score=77)
    game_60_lose_score = Game_Team_Score(
        game_id=game_60.id, team_id=kentucky.id, score=71)
    game_60.game_team_scores = [game_60_win_score, game_60_lose_score]
    game_60.child_game_id = game_62.id

    game_61_win_score = Game_Team_Score(
        game_id=game_61.id, team_id=texas_Tech.id, score=61)
    game_61_lose_score = Game_Team_Score(
        game_id=game_61.id, team_id=michigan_State.id, score=51)
    game_61.game_team_scores = [game_61_win_score, game_61_lose_score]
    game_61.child_game_id = game_63.id

    game_62_win_score = Game_Team_Score(
        game_id=game_62.id, team_id=virginia.id, score=63)
    game_62_lose_score = Game_Team_Score(
        game_id=game_62.id, team_id=auburn.id, score=62)
    game_62.game_team_scores = [game_62_win_score, game_62_lose_score]
    game_62.child_game_id = game_63.id

    game_63_win_score = Game_Team_Score(
        game_id=game_63.id, team_id=virginia.id, score=85)
    game_63_lose_score = Game_Team_Score(
        game_id=game_63.id, team_id=texas_Tech.id, score=77)
    game_63.game_team_scores = [game_63_win_score, game_63_lose_score]
    db.session.commit()


def undo_2019_tournament():
    db.session.execute(
        'TRUNCATE march_madness_teams RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE games RESTART IDENTITY CASCADE;')
    db.session.execute('TRUNCATE drafts RESTART IDENTITY CASCADE;')
    db.session.commit()
