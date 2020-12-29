import { LOGIN, LOGOUT } from '../actions/authenticate';
import { SET_DRAFT_DATA } from '../actions/drafts';

export default function reducer(state = null, action) {
  switch (action.type) {
    case LOGIN:
      return action.data.drafts;
    case SET_DRAFT_DATA:
      return {
        ...state,
        [action.data.draft.id]: action.data.draft
      };
    case LOGOUT:
      return null;
    default:
      return state;
  }
}
