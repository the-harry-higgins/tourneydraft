import { LOGIN, LOGOUT } from '../actions/authenticate';
import { SET_ROUND } from '../actions/ui';
import { DRAFT_CHANGE } from '../actions/drafts';

function calculatePoints(team, round) {
  let points = 0;
  for (let i = 1; i < round; i++) {
    if (!team.games_by_round[i] || team.won_game_ids === 0) {
      break;
    }
    if (team.won_game_ids.includes(team.games_by_round[i])) {
      points += team.seed_number + i;
    }
  }
  return points;
}

export default function reducer(state = null, action) {
  switch (action.type) {
    case LOGIN:
    case DRAFT_CHANGE:
      return action.data.marchMadnessTeams;
    case LOGOUT:
      return null;
    case SET_ROUND:
      const newState = {};
      Object.keys(state).forEach(id => {
        newState[id] = {
          ...state[id],
          points: calculatePoints(state[id], action.roundNum)
        }
      });
      return newState;
    default:
      return state;
  }
}
