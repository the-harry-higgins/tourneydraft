import { SET_ERRORS } from '../actions/errors';

export default function reducer(state = null, action) {
  switch (action.type) {
    case SET_ERRORS:
      return action.errors;
    default:
      return state;
  }
}
