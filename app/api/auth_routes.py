from flask import Blueprint, jsonify, session, request
from app.models import User, db, Drafted_Team, March_Madness_Team, Tournament
from app.forms import LoginForm
from app.forms import SignUpForm
from flask_login import current_user, login_user, logout_user, login_required
from .draft_routes import get_data_for_draft

auth_routes = Blueprint('auth', __name__)


def get_user_data(user):
    session_data = {'currentUserId': user.id}
    messages_data = {'success': ['Successfully logged in']}

    # Build the user menu data with all leagues and drafts
    leagues_data = {league.id: league.to_dict() for league in user.leagues}
    drafts_data = {draft.id: draft.to_dict()
                   for league in user.leagues for draft in league.drafts}

    # Specific to the league / draft
    league_users_data = None
    drafted_teams_data = None
    march_madness_teams_data = None
    games_data = None
    tournament_data = None

    # You are in at least one league
    if user.league_users:
        # There are drafts
        if drafts_data:
            # Check if any draft is currently drafting
            # Otherwise return most recent draft
            current_draft_id = None
            max_year = 0
            for draft_id in drafts_data:
                if drafts_data[draft_id]['drafting']:
                    current_draft_id = draft_id
                    messages_data['info'] = [
                        'Your league is currently drafting']
                    break
                if drafts_data[draft_id]['year'] > max_year:
                    max_year = drafts_data[draft_id]['year']
                    current_draft_id = draft_id

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
          pass
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


def validation_errors_to_error_messages(validation_errors):
    """
    Simple function that turns the WTForms validation errors into a simple list
    """
    errorMessages = []
    for field in validation_errors:
        for error in validation_errors[field]:
            errorMessages.append(f"{field} : {error}")
    return errorMessages


@auth_routes.route('/')
def authenticate():
    """
    Authenticates a user.
    """
    if current_user.is_authenticated:
        data = get_user_data(current_user)
        return data
    return {'errors': ['Unauthorized']}, 401


@auth_routes.route('/login', methods=['POST'])
def login():
    """
    Logs a user in
    """
    form = LoginForm()
    # Get the csrf_token from the request cookie and put it into the
    # form manually to validate_on_submit can be used
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        # Add the user to the session, we are logged in!
        user = User.query.filter(User.email == form.data['email']).first()
        login_user(user)
        data = get_user_data(user)
        return data
    return {'errors': validation_errors_to_error_messages(form.errors)}, 401


@auth_routes.route('/logout')
def logout():
    """
    Logs a user out
    """
    logout_user()
    return {'message': 'User logged out'}


@auth_routes.route('/signup', methods=['POST'])
def sign_up():
    """
    Creates a new user and logs them in
    """
    form = SignUpForm()
    form['csrf_token'].data = request.cookies['csrf_token']
    if form.validate_on_submit():
        user = User(
            name=form.data['name'],
            email=form.data['email'],
            password=form.data['password']
        )
        db.session.add(user)
        db.session.commit()
        login_user(user)
        data = get_user_data(user)
        return data
    return {'errors': validation_errors_to_error_messages(form.errors)}


@auth_routes.route('/unauthorized')
def unauthorized():
    """
    Returns unauthorized JSON when flask-login authentication fails
    """
    return {'errors': ['Unauthorized']}, 401
