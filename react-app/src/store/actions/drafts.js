import { setErrors } from "./errors";

export const DRAFT_CHANGE = 'drafts/DRAFT_CHANGE';
export const SET_DRAFT_DATA = 'drafts/SET_DRAFT_DATA';

export const draftChangeAction = (data) => ({ type: DRAFT_CHANGE, data });
export const setDraftDataAction = (data) => ({ type: SET_DRAFT_DATA, data });

export const draftChangeThunk = (draftId, leagueId) => async (dispatch) => {
  const response = await fetch(`/api/leagues/${leagueId}/drafts/${draftId}`);

  if (response.ok) {
    const data = await response.json();
    if (!data.errors) {
      dispatch(draftChangeAction(data));
    }
    else {
      dispatch(setErrors(data));
    }
  }
}