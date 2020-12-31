import { LOGIN, LOGOUT } from '../actions/authenticate';
import { DRAFT_CHANGE, CREATE_DRAFT } from '../actions/drafts';
import { DELETE_CURRENT_LEAGUE } from '../actions/leagues';


export default function reducer(state = {}, action) {
  switch (action.type) {
    case LOGIN:
    case CREATE_DRAFT:
    case DRAFT_CHANGE:
      return action.data.session;
    case DELETE_CURRENT_LEAGUE:
      const newState = {currentUserId: state.currentUserId};
      return newState;
    case LOGOUT:
      return {};
    default:
      return state;
  }
}
