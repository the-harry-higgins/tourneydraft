import json

from datetime import datetime
from flask import Blueprint, request
from flask_login import login_required, current_user

from app.models import Draft, db
from app.api.utils import get_data_for_draft, generate_draft_order

draft_routes = Blueprint('drafts', __name__)

@draft_routes.route('/<int:draft_id>')
@login_required
def draft(league_id, draft_id):
    league_user_id = None
    for league_user in current_user.league_users:
        if league_user.league_id == league_id:
            league_user_id = league_user.id
            break
    if not league_user_id:
        return {'errors': ['Unauthorized']}, 401

    (tournament_data,
     league_users_data,
     drafted_teams_data,
     march_madness_teams_data,
     games_data) = get_data_for_draft(draft_id)

    session_data = {
        'currentUserId': current_user.id,
        'currentLeagueId': league_id,
        'currentLeagueUserId': league_user_id,
        'currentDraftId': draft_id
    }

    messages_data = {
        'info': ['Viewing new draft']
    }

    return {
        'tournament': tournament_data,
        'leagueUsers': league_users_data,
        'draftedTeams': drafted_teams_data,
        'marchMadnessTeams': march_madness_teams_data,
        'games': games_data,
        'session': session_data,
        'messages': messages_data,
    }


@draft_routes.route('/', methods=['POST'])
@login_required
def create_draft(league_id):
    req_data = json.loads(request.data)
    tournament_id = req_data['tournament_id']

    draft_order = generate_draft_order(league_id)

    draft = Draft(league_id=league_id, tournament_id=tournament_id,
                  draft_order=json.dumps(draft_order), draft_index=0, 
                  draft_time=datetime.now(),
                  drafting=True, current_drafter_id=draft_order[0])
    db.session.add(draft)
    db.session.commit()

    league_user_id = None
    for league_user in current_user.league_users:
        if league_user.league_id == league_id:
            league_user_id = league_user.id
            break
    if not league_user_id:
        return {'errors': ['Unauthorized']}, 401

    (tournament_data,
     league_users_data,
     drafted_teams_data,
     march_madness_teams_data,
     games_data) = get_data_for_draft(draft.id)

    session_data = {
        'currentUserId': current_user.id,
        'currentLeagueId': league_id,
        'currentLeagueUserId': league_user_id,
        'currentDraftId': draft.id
    }

    messages_data = {
        'success': ['Created a new draft']
    }

    return {
        'draft': draft.to_dict(),
        'tournament': tournament_data,
        'leagueUsers': league_users_data,
        'draftedTeams': drafted_teams_data,
        'marchMadnessTeams': march_madness_teams_data,
        'games': games_data,
        'session': session_data,
        'messages': messages_data,
    }



@draft_routes.route('/<int:draft_id>/drafted_teams')
@login_required
def draftedTeams(league_id, draft_id):
    draft = Draft.query.get(draft_id)
    drafted_teams_data = {
        drafted_team.id: drafted_team.to_dict()
        for drafted_team in draft.drafted_teams
    }
    return {
        'draft': draft.to_dict(),
        'draftedTeams': drafted_teams_data
    }
