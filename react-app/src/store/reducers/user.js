import { SET_USER, REMOVE_USER } from '../actions/user';
import { LOGIN } from '../actions/authenticate';

export default function reducer(state = null, action) {
  switch (action.type) {
    case LOGIN:
      return action.data.user;
    // case SET_USER:
    //   return action.user;
    // case REMOVE_USER:
    //   return null;
    default:
      return state;
  }
}
