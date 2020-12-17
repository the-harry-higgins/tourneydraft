import { createStore, applyMiddleware, combineReducers, compose } from 'redux';
import thunk from "redux-thunk";
import user from './reducers/user';
import leagues from './reducers/leagues';
import league_users from './reducers/league_users';
import drafts from './reducers/drafts';
import draftedTeams from './reducers/draftedTeams';
import marchMadnessTeams from './reducers/marchMadnessTeams';
import games from './reducers/games';
import tournament from './reducers/tournament';
import session from './reducers/session';
import messages from './reducers/messages';
import ui from './reducers/ui';

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const entities = combineReducers({
  user,
  leagues,
  league_users,
  drafts,
  draftedTeams,
  marchMadnessTeams,
  games,
  tournament
});

const reducer = combineReducers({
  entities,
  session,
  messages,
  ui
});

const configureStore = (initialState) => {
  return createStore(reducer, initialState, composeEnhancers(applyMiddleware(thunk)));
};

export default configureStore;
