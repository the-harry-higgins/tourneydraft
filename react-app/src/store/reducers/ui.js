import { SET_ROUND, SET_SORT, SHOW_CREATE_DRAFT, TOGGLE_LEAGUE_MODAL } from '../actions/ui';
import { LOGIN, LOGOUT } from '../actions/authenticate';
import { DRAFT_CHANGE } from '../actions/drafts';

export default function reducer(state = {showCreateDraft: false, showJoinLeague: false}, action) {
  switch (action.type) {
    case LOGIN:
    case DRAFT_CHANGE:
      const roundNum = action.data.tournament ?
        action.data.tournament.last_round_completed + 1 : null;
      return {
        ...state,
        'roundNum': roundNum,
        'sortBy': 'wins'
      };
    case LOGOUT:
      return null;
    case SET_ROUND:
      return { ...state, 'roundNum': action.roundNum };
    case SET_SORT:
      return { ...state, 'sortBy': action.sort };
    case SHOW_CREATE_DRAFT:
      return { ...state, 'showCreateDraft': !state['showCreateDraft'] };
    case TOGGLE_LEAGUE_MODAL:
      return { ...state, 'showJoinLeague': !state['showJoinLeague'] };
    default:
      return state;
  }
}
