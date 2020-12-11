import { createStore, applyMiddleware, combineReducers, compose } from 'redux';
import thunk from "redux-thunk";
import user from './reducers/user';
import leagues from './reducers/leagues';
import league_users from './reducers/league_users';
import drafts from './reducers/drafts';
import teams from './reducers/teams';
import games from './reducers/games';
import session from './reducers/session';
import errors from './reducers/errors';

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const entities = combineReducers({
  user,
  leagues,
  // league_users,
  // drafts,
  // teams,
  // games
});

const reducer = combineReducers({
  entities,
  session,
  errors
});

const configureStore = (initialState) => {
  return createStore(reducer, initialState, composeEnhancers(applyMiddleware(thunk)));
};

export default configureStore;
