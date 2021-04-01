import { LOGIN, LOGOUT } from '../actions/authenticate';
import { DRAFT_CHANGE, CREATE_DRAFT } from '../actions/drafts';
import { SET_ROUND, SET_SORT, TOGGLE_DRAFT_MODAL, TOGGLE_LEAGUE_MODAL } from '../actions/ui';

export default function reducer(state = { showCreateDraft: false, showJoinLeague: false }, action) {
  switch (action.type) {
    case LOGIN:
    case CREATE_DRAFT:
    case DRAFT_CHANGE:
      const roundNum = action.data.tournament ? action.data.tournament.last_round_completed + 1 : null;
      return {
        ...state,
        roundNum,
        sortBy: 'wins',
      };
    case LOGOUT:
      return null;
    case SET_ROUND:
      return { ...state, roundNum: action.roundNum };
    case SET_SORT:
      return { ...state, sortBy: action.sort };
    case TOGGLE_DRAFT_MODAL:
      return { ...state, showCreateDraft: action.leagueId };
    case TOGGLE_LEAGUE_MODAL:
      return { ...state, showJoinLeague: !state.showJoinLeague };
    default:
      return state;
  }
}
