import { LOGIN, LOGOUT } from '../actions/authenticate';
import { DRAFT_CHANGE, SET_DRAFT_DATA } from '../actions/drafts';

export default function reducer(state = null, action) {
  switch (action.type) {
    case LOGIN:
    case SET_DRAFT_DATA:
    case DRAFT_CHANGE:
      return action.data.draftedTeams;
    case LOGOUT:
      return null;
    default:
      return state;
  }
}
