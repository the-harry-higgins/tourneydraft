import { LOGIN, LOGOUT } from '../actions/authenticate';
import { DELETE_CURRENT_LEAGUE, DELETE_LEAGUE } from '../actions/leagues';

export default function reducer(state = null, action) {
  switch (action.type) {
    case LOGIN:
      return action.data.leagues;
    case DELETE_CURRENT_LEAGUE:
    case DELETE_LEAGUE:
      const newState = { ...state };
      delete newState[action.data.league.id];
      return newState;
    case LOGOUT:
      return null;
    default:
      return state;
  }
}
