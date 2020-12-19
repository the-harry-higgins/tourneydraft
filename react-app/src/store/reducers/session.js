import { LOGIN, LOGOUT } from '../actions/authenticate';
import { DRAFT_CHANGE } from '../actions/drafts';

export default function reducer(state = {}, action) {
  switch (action.type) {
    case LOGIN:
    case DRAFT_CHANGE:
      return action.data.session;
    case LOGOUT:
      return {};
    default:
      return state;
  }
}
