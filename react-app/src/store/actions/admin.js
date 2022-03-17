import {
  getTournaments,
  getTournament,
  createTournament,
  updateTournament,
  deleteTournament,
} from '../../services/admin';
import { setErrors } from './errors';

export const GET_TOURNAMENTS = 'admin/GET_TOURNAMENTS';
export const GET_TOURNAMENT = 'admin/GET_TOURNAMENT';
export const CREATE_TOURNAMENT = 'admin/CREATE_TOURNAMENT';
export const UPDATE_TOURNAMENT = 'admin/UPDATE_TOURNAMENT';
export const DELETE_TOURNAMENT = 'admin/DELETE_TOURNAMENT';

export const getTournamentsAction = data => ({ type: GET_TOURNAMENTS, data });
export const getTournamentAction = data => ({ type: GET_TOURNAMENT, data });
export const createTournamentAction = data => ({ type: CREATE_TOURNAMENT, data });
export const updateTournamentAction = data => ({ type: UPDATE_TOURNAMENT, data });
export const deleteTournamentAction = data => ({ type: DELETE_TOURNAMENT, data });

export const getTournamentsThunk = () => async dispatch => {
  const data = await getTournaments();

  if (!data.errors) {
    dispatch(getTournamentsAction(data));
    return true;
  } else {
    dispatch(setErrors(data.errors));
    return false;
  }
};

export const getTournamentThunk = tournamentId => async dispatch => {
  const data = await getTournament(tournamentId);

  if (!data.errors) {
    dispatch(getTournamentAction(data));
    return true;
  } else {
    dispatch(setErrors(data.errors));
    return false;
  }
};

export const createTournamentThunk = (year, region1, region2, region3, region4) => async dispatch => {
  const data = await createTournament(year, region1, region2, region3, region4);

  if (!data.errors) {
    dispatch(createTournamentAction(data));
    return true;
  } else {
    dispatch(setErrors(data.errors));
    return false;
  }
};

export const updateTournamentThunk = (tournamentId, lastRoundCompleted) => async dispatch => {
  console.log(tournamentId, lastRoundCompleted);
  const data = await updateTournament(tournamentId, lastRoundCompleted);
  console.log(data);

  if (!data.errors) {
    dispatch(updateTournamentAction(data));
    return true;
  } else {
    dispatch(setErrors(data.errors));
    return false;
  }
};

export const deleteTournamentThunk = tournamentId => async dispatch => {
  const data = await deleteTournament(tournamentId);

  if (!data.errors) {
    dispatch(deleteTournamentAction({ tournamentId }));
    return true;
  } else {
    dispatch(setErrors(data));
    return false;
  }
};
