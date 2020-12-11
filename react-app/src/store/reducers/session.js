import { LOGIN } from '../actions/authenticate';

export default function reducer(state = {}, action) {
  switch (action.type) {
    case LOGIN:
      return action.data.session;
    default:
      return state;
  }
}
