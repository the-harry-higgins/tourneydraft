import { createStore, applyMiddleware, combineReducers, compose } from 'redux';
import thunk from 'redux-thunk';

import draftedTeams from './reducers/draftedTeams';
import drafts from './reducers/drafts';
import games from './reducers/games';
import league_users from './reducers/league_users';
import leagues from './reducers/leagues';
import marchMadnessTeams from './reducers/marchMadnessTeams';
import messages from './reducers/messages';
import session from './reducers/session';
import tournament from './reducers/tournament';
import ui from './reducers/ui';
import user from './reducers/user';

const composeEnhancers = window.__REDUX_DEVTOOLS_EXTENSION_COMPOSE__ || compose;

const entities = combineReducers({
  user,
  leagues,
  league_users,
  drafts,
  draftedTeams,
  marchMadnessTeams,
  games,
  tournament,
});

const reducer = combineReducers({
  entities,
  session,
  messages,
  ui,
});

const configureStore = initialState => {
  return createStore(reducer, initialState, composeEnhancers(applyMiddleware(thunk)));
};

export default configureStore;
