import { LOGIN } from '../actions/authenticate';

export default function reducer(state = null, action) {
  switch (action.type) {
    case LOGIN:
      return action.data.league_users;
    default:
      return state;
  }
}
