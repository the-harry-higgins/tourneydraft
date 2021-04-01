import { LOGIN } from '../actions/authenticate';
import { DRAFT_CHANGE, SET_DRAFT_DATA, SET_DEMO_DRAFT_DATA, CREATE_DRAFT } from '../actions/drafts';
import { SET_ERRORS } from '../actions/errors';
import { DELETE_CURRENT_LEAGUE, DELETE_LEAGUE } from '../actions/leagues';
import { SET_ROUND, SET_SORT } from '../actions/ui';

const roundMessages = [
  '',
  'Round 1',
  'Round 2',
  'Sweet Sixteen',
  'Elite Eight',
  'Final Four',
  'Championship',
  'Final Results',
];

export default function reducer(state = null, action) {
  switch (action.type) {
    case SET_ERRORS:
      return { error: action.errors };
    case LOGIN:
    case DELETE_CURRENT_LEAGUE:
    case DELETE_LEAGUE:
    case CREATE_DRAFT:
    case DRAFT_CHANGE:
      return action.data.messages;
    case SET_DEMO_DRAFT_DATA:
    case SET_DRAFT_DATA:
      if (action.data.messages) {
        return { success: action.data.messages };
      }
      return null;
    case SET_ROUND:
      return { success: [`Viewing ${roundMessages[action.roundNum]}`] };
    case SET_SORT:
      return { info: [`Sorting by ${action.sort}`] };
    default:
      return null;
  }
}
