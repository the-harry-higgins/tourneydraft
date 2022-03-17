import random

from app.models import Draft, League


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages



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



def generate_draft_order(league_id):
    league = League.query.filter(League.id == league_id).one()
    league_user_ids = [league_user.id for league_user in league.league_users]

    loops = 64 / (len(league_user_ids) * 2)

    draft_order = []
    for loop in range(int(loops)):
        random.shuffle(league_user_ids)
        draft_order.extend(league_user_ids + list(reversed(league_user_ids)))
    return draft_order



def get_user_data(user, league=None, league_user_id=None):
    session_data = {'currentUserId': user.id}
    messages_data = {'success': ['Successfully logged in']}

    # Build the user menu data with all leagues and drafts
    leagues_data = {league.id: league.to_dict() for league in user.leagues}
    drafts_data = {draft.id: draft.to_dict()
                   for league in user.leagues for draft in league.drafts}

    # Specific to the league / draft
    league_users_data = {}
    drafted_teams_data = {}
    march_madness_teams_data = None
    games_data = None
    tournament_data = None

    # When you are joining or creating a new league
    if league and league_user_id:
        session_data['currentLeagueId'] = league.id
        session_data['currentLeagueUserId'] = league_user_id

        draft_ids = leagues_data[league.id]['draft_ids']
        # There are drafts
        if draft_ids:
            current_draft_id, drafting = determineDraftId(drafts_data, draft_ids)
            if drafting:
                messages_data['info'] = ['Your league is currently drafting']

            session_data['currentDraftId'] = current_draft_id

            (tournament_data,
             league_users_data,
             drafted_teams_data,
             march_madness_teams_data,
             games_data) = get_data_for_draft(current_draft_id)
        # No drafts
        else:
            messages_data['info'] = ['Your league does not have any drafts.']

            league_users_data = {
                lu.id: lu.to_dict()
                for lu in league.league_users
            }

    # You are in at least one league
    elif user.league_users:
        # There are drafts
        if drafts_data:
            current_draft_id, drafting = determineDraftId(drafts_data)
            if drafting:
                messages_data['info'] = [
                    'Your league is currently drafting']

            session_data['currentDraftId'] = current_draft_id

            league_id = drafts_data[current_draft_id]['league_id']
            session_data['currentLeagueId'] = league_id

            league_user_id = None
            for league_user in user.league_users:
                if league_user.league_id == league_id:
                    league_user_id = league_user.id
                    break
            session_data['currentLeagueUserId'] = league_user_id

            (tournament_data,
             league_users_data,
             drafted_teams_data,
             march_madness_teams_data,
             games_data) = get_data_for_draft(current_draft_id)
        # No drafts but you are in a league
        else:
            league_user = user.league_users[0]
            session_data['currentLeagueUserId'] = league_user.id
            session_data['currentLeagueId'] = league_user.league_id
            messages_data['info'] = ['Your league does not have any drafts.']

            league_users_data = {
                lu.id: lu.to_dict()
                for lu in league_user.league.league_users
            }
    # You are not in any leagues
    else:
        pass

    return {
        "user": user.to_dict(),
        "leagues": leagues_data,
        "drafts": drafts_data,
        'leagueUsers': league_users_data,
        'draftedTeams': drafted_teams_data,
        'marchMadnessTeams': march_madness_teams_data,
        'games': games_data,
        'tournament': tournament_data,
        "session": session_data,
        'messages': messages_data,
    }


def determineDraftId(drafts_data, draft_ids=None):
    """
    Check if any draft is currently drafting
    Otherwise return most recent draft
    """
    if not draft_ids:
        draft_ids = drafts_data.keys()

    current_draft_id = None
    max_year = 0
    drafting = False
    for draft_id in draft_ids:
        if drafts_data[draft_id]['drafting']:
            current_draft_id = draft_id
            drafting = True
            break
        if drafts_data[draft_id]['year'] > max_year:
            max_year = drafts_data[draft_id]['year']
            current_draft_id = draft_id

    return current_draft_id, drafting
