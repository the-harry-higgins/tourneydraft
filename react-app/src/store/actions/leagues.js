import { deleteLeague } from '../../services/leagues';
import { setErrors } from './errors';

export const DELETE_LEAGUE = 'leagues/DELETE_LEAGUE';
export const DELETE_CURRENT_LEAGUE = 'leagues/DELETE_CURRENT_LEAGUE';

export const deleteLeagueAction = data => ({ type: DELETE_LEAGUE, data });
export const deleteCurrentLeagueAction = data => ({
  type: DELETE_CURRENT_LEAGUE,
  data,
});

export const deleteLeagueThunk = (leagueId, currentLeagueId) => async dispatch => {
  const data = await deleteLeague(leagueId);

  if (!data.errors) {
    if (data.league.id === currentLeagueId) {
      dispatch(deleteCurrentLeagueAction(data));
    } else {
      dispatch(deleteLeagueAction(data));
    }
  } else {
    dispatch(setErrors(data));
  }
};
