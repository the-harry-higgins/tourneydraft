import { LOGIN, LOGOUT } from '../actions/authenticate';
import { DRAFT_CHANGE } from '../actions/drafts';

export default function reducer(state = null, action) {
  switch (action.type) {
    case LOGIN:
    case DRAFT_CHANGE:
      return action.data.tournament;
    case LOGOUT:
      return null;
    default:
      return state;
  }
}
