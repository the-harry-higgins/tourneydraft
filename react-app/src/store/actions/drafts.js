import { createDraft } from '../../services/drafts';
import { setErrors } from './errors';

export const DRAFT_CHANGE = 'drafts/DRAFT_CHANGE';
export const SET_DRAFT_DATA = 'drafts/SET_DRAFT_DATA';
export const SET_DEMO_DRAFT_DATA = 'drafts/SET_DEMO_DRAFT_DATA';
export const CREATE_DRAFT = 'drafts/CREATE_DRAFT';

export const draftChangeAction = data => ({ type: DRAFT_CHANGE, data });
export const setDraftDataAction = data => ({ type: SET_DRAFT_DATA, data });
export const setDemoDraftDataAction = data => ({
  type: SET_DEMO_DRAFT_DATA,
  data,
});
export const createDraftAction = data => ({ type: CREATE_DRAFT, data });

export const draftChangeThunk = (draftId, leagueId) => async dispatch => {
  const response = await fetch(`/api/leagues/${leagueId}/drafts/${draftId}`);

  if (response.ok) {
    const data = await response.json();
    if (!data.errors) {
      dispatch(draftChangeAction(data));
    } else {
      dispatch(setErrors(data));
    }
  }
};

export const createDraftThunk = (tournament, leagueId) => async dispatch => {
  const data = await createDraft(tournament, leagueId);
  console.log(data);

  if (!data.errors) {
    dispatch(createDraftAction(data));
  } else {
    dispatch(setErrors(data));
  }
};
