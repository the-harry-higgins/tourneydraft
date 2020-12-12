import { SET_ROUND } from '../actions/ui';
import { LOGIN, LOGOUT } from '../actions/authenticate';

export default function reducer(state = {}, action) {
  switch (action.type) {
    case LOGIN:
      return {...state, 'roundNum': 1};
    case LOGOUT:
      return null;
    case SET_ROUND:
      return { ...state, 'roundNum': action.roundNum };
    default:
      return state;
  }
}
