export const SET_ROUND = 'ui/SET_ROUND';
export const SET_SORT = 'ui/SET_SORT';
export const TOGGLE_DRAFT_MODAL = 'ui/TOGGLE_DRAFT_MODAL';
export const TOGGLE_LEAGUE_MODAL = 'ui/TOGGLE_LEAGUE_MODAL';

export const setRound = (roundNum) => ({ type: SET_ROUND, roundNum });
export const setSort = (sort) => ({ type: SET_SORT, sort });
export const toggleDraftModal = (leagueId) => ({ type: TOGGLE_DRAFT_MODAL, leagueId });
export const toggleLeagueModal = () => ({ type: TOGGLE_LEAGUE_MODAL });