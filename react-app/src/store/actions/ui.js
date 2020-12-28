export const SET_ROUND = 'ui/SET_ROUND';
export const SET_SORT = 'ui/SET_SORT';
export const SHOW_CREATE_DRAFT = 'ui/SHOW_CREATE_DRAFT';
export const TOGGLE_LEAGUE_MODAL = 'ui/TOGGLE_LEAGUE_MODAL';

export const setRound = (roundNum) => ({ type: SET_ROUND, roundNum });
export const setSort = (sort) => ({ type: SET_SORT, sort });
export const showCreateDraft = () => ({ type: SHOW_CREATE_DRAFT });
export const toggleLeagueModal = () => ({ type: TOGGLE_LEAGUE_MODAL });