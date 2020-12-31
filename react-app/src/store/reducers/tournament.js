import { LOGIN, LOGOUT } from '../actions/authenticate';
import { DRAFT_CHANGE, CREATE_DRAFT } from '../actions/drafts';
import { DELETE_CURRENT_LEAGUE } from '../actions/leagues';


export default function reducer(state = null, action) {
  switch (action.type) {
    case LOGIN:
    case CREATE_DRAFT:
    case DRAFT_CHANGE:
      return action.data.tournament;
    case DELETE_CURRENT_LEAGUE:
    case LOGOUT:
      return null;
    default:
      return state;
  }
}
