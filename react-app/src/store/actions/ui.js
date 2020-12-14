export const SET_ROUND = 'ui/SET_ROUND';
export const SET_SORT = 'ui/SET_SORT';

export const setRound = (roundNum) => ({ type: SET_ROUND, roundNum });
export const setSort = (sort) => ({ type: SET_SORT, sort });