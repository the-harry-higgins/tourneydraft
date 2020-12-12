import { SET_ERRORS } from '../actions/errors';
import { LOGIN, LOGOUT } from '../actions/authenticate';

export default function reducer(state = null, action) {
  switch (action.type) {
    case SET_ERRORS:
      return {'error': action.errors};
    case LOGIN:
      return action.data.messages;
    default:
      return state;
  }
}
