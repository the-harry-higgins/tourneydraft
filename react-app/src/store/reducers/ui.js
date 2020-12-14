import { SET_ROUND, SET_SORT } from '../actions/ui';
import { LOGIN, LOGOUT } from '../actions/authenticate';

export default function reducer(state = {}, action) {
  switch (action.type) {
    case LOGIN:
      return {...state, 'roundNum': 1, 'sortBy': 'wins'};
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
