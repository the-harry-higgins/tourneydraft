import { LOGIN, LOGOUT } from '../actions/authenticate';
import { SET_DRAFT_DATA, CREATE_DRAFT } from '../actions/drafts';
import { DELETE_CURRENT_LEAGUE, DELETE_LEAGUE } from '../actions/leagues';


export default function reducer(state = null, action) {
  switch (action.type) {
    case LOGIN:
      return action.data.drafts;
    case SET_DRAFT_DATA:
    case CREATE_DRAFT:
      return {
        ...state,
        [action.data.draft.id]: action.data.draft
      };
    case DELETE_CURRENT_LEAGUE:
    case DELETE_LEAGUE:
      const newState = {...state};
      for (let id in action.data.league.draft_ids) {
        delete newState[id];
      }
      return newState;
    case LOGOUT:
      return {};
    default:
      return state;
  }
}
