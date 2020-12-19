import { SET_ROUND, SET_SORT } from '../actions/ui';
import { LOGIN, LOGOUT } from '../actions/authenticate';
import { DRAFT_CHANGE } from '../actions/drafts';

export default function reducer(state = {}, action) {
  switch (action.type) {
    case LOGIN:
    case DRAFT_CHANGE:
      return {...state, 'roundNum': action.data.tournament.last_round_completed + 1, 'sortBy': 'wins'};
    case LOGOUT:
      return null;
    case SET_ROUND:
      return { ...state, 'roundNum': action.roundNum };
    case SET_SORT:
      return { ...state, 'sortBy': action.sort };
    default:
      return state;
  }
}
