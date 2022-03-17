import {
  GET_TOURNAMENTS,
  GET_TOURNAMENT,
  CREATE_TOURNAMENT,
  UPDATE_TOURNAMENT,
  DELETE_TOURNAMENT,
} from '../actions/admin';

const initialState = {
  tournaments: {},
};

export default function reducer(state = initialState, action) {
  switch (action.type) {
    case GET_TOURNAMENTS:
      return {
        ...state,
        tournaments: action.data.tournaments,
      };
    case GET_TOURNAMENT:
    case CREATE_TOURNAMENT:
    case UPDATE_TOURNAMENT:
      return {
        ...state,
        tournaments: {
          ...state.tournaments,
          [action.data.tournament.id]: action.data.tournament,
        },
      };
    case DELETE_TOURNAMENT:
      const newTournaments = { ...state.tournaments };
      delete newTournaments[action.data.tournamentId];
      return {
        ...state,
        tournaments: newTournaments,
      };
    default:
      return state;
  }
}
