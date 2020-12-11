import { LOGIN } from '../actions/authenticate';

export default function reducer(state = null, action) {
  switch (action.type) {
    case LOGIN:
      return action.data.drafts;
    default:
      return state;
  }
}
