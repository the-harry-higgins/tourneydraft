from flask import Blueprint, jsonify
from flask_login import login_required, current_user
from app.models import User, League_User, League, Draft

draft_routes = Blueprint('drafts', __name__)


def get_data_for_draft(draft_id):
    draft = Draft.query.get(draft_id)
    tournament_data = draft.tournament.to_dict()

    league_users_data = {
        league_user.id: league_user.to_dict()
        for league_user in draft.league.league_users
    }

    drafted_teams_data = {
        drafted_team.id: drafted_team.to_dict()
        for drafted_team in draft.drafted_teams
    }

    march_madness_teams_data = {
        march_madness_team.id: march_madness_team.to_dict(
            draft.tournament.last_round_completed)
        for march_madness_team in draft.tournament.march_madness_teams
    }

    games_data = {
        game.id: game.to_dict()
        for game in draft.tournament.games
    }

    return (tournament_data,
            league_users_data,
            drafted_teams_data,
            march_madness_teams_data,
            games_data)


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
