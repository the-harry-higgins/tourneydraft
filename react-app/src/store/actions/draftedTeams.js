import { setDraftDataAction } from './drafts';
import { setErrors } from './errors';

export const draftedTeamsThunk = (draftId, leagueId) => async dispatch => {
  const response = await fetch(`/api/leagues/${leagueId}/drafts/${draftId}/drafted_teams`);

  if (response.ok) {
    const data = await response.json();
    if (!data.errors) {
      dispatch(setDraftDataAction(data));
    } else {
      dispatch(setErrors(data));
    }
  }
};
