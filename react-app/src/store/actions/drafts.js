export const DRAFT_CHANGE = 'drafts/DRAFT_CHANGE';

export const draftChangeAction = (data) => ({ type: DRAFT_CHANGE, data });

export const draftChangeThunk = (draftId) => async (dispatch) => {
  const response = await fetch(`/api/users/${userId}/notebooks/${notebookId}/notes/${noteId}/`);

  if (response.ok) {
    const note = await response.json();
    dispatch(updateNoteAction(note));
  }
}