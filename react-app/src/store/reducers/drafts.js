import { LOGIN, LOGOUT } from '../actions/authenticate';

export default function reducer(state = null, action) {
  switch (action.type) {
    case LOGIN:
      return action.data.drafts;
    case LOGOUT:
      return null;
    default:
      return state;
  }
}
