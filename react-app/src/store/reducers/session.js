import { LOGIN, LOGOUT } from '../actions/authenticate';

export default function reducer(state = {}, action) {
  switch (action.type) {
    case LOGIN:
      return action.data.session;
    case LOGOUT:
      return {};
    default:
      return state;
  }
}
