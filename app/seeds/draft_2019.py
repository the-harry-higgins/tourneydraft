from app.models import db, March_Madness_Team, League, League_User, Draft, Drafted_Team, User, Tournament
import json
from datetime import datetime
import random
from app.api.draft_routes import generate_draft_order


def seed_draft_2019():
    # This is for the Demo Draft functionality
    league = League.query.filter(
        League.name == 'The League of Extraordinary Gentlemen').one()

    tournament = Tournament.query.filter(Tournament.year=2019).one()

    draft_order = generate_draft_order(league.id)
    draft = Draft(league_id=league_id, tournament_id=tournament_id,
                  draft_order=json.dumps(draft_order), draft_index=0,
                  draft_time=datetime.now(),
                  drafting=True, current_drafter_id=draft_order[0])
    db.session.add(draft)
    db.session.commit()

    # This is for a second year of the Demo data
    league = League.query.filter(
        League.name == 'The Dumb Friends League').one()

    draft_order = generate_draft_order(league.id)
    draft = Draft(league_id=league_id, tournament_id=tournament_id,
                  draft_order=json.dumps(draft_order), draft_index=0,
                  draft_time=datetime.now(),
                  drafting=True, current_drafter_id=draft_order[0])
    db.session.add(draft)
    db.session.commit()

    march_madness_team_ids = {
        march_madness_team.id for march_madness_team in tournament.march_madness_teams
    }
    for i in range(0, 64):
        pick = random.choice(march_madness_team_ids)
        march_madness_team_ids.remove(pick)
        drafted_team = Drafted_Team(
            march_madness_team_id=pick,
            league_user_id=draft_order[i],
            draft_id=draft.id,
            selection_num=i+1)
        db.session.add(drafted_team)

    db.session.commit()


def undo_draft_2019():
    db.session.execute(
        'DELETE FROM drafts WHERE tournament.year = 2019 JOIN tournaments on (drafts.tournament_id = tournament.id);')
    db.session.commit()
