import { LOGIN, LOGOUT } from '../actions/authenticate';
import { DRAFT_CHANGE, SET_DRAFT_DATA, CREATE_DRAFT, SET_DEMO_DRAFT_DATA } from '../actions/drafts';
import { DELETE_CURRENT_LEAGUE } from '../actions/leagues';

export default function reducer(state = null, action) {
  switch (action.type) {
    case LOGIN:
    case SET_DRAFT_DATA:
    case CREATE_DRAFT:
    case DRAFT_CHANGE:
      return action.data.draftedTeams;
    case SET_DEMO_DRAFT_DATA:
      return {
        ...state,
        [action.data.draftedTeam.id]: action.data.draftedTeam
      }
    case DELETE_CURRENT_LEAGUE:
    case LOGOUT:
      return {};
    default:
      return state;
  }
}
