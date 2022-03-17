import React, { useEffect } from 'react';

import { useDispatch, useSelector } from 'react-redux';
import { Redirect, Route, Switch } from 'react-router-dom';

import { toggleLeagueModal } from '../store/actions/ui';
import AdminPage from './AdminPage';
import BracketPage from './BracketPage';
import DemoDraftPage from './DemoDraftPage';
import DraftModal from './DraftModal';
import DraftPage from './DraftPage';
import HelpPage from './HelpPage';
import LeaderboardPage from './LeaderboardPage';
import LeagueModal from './LeagueModal';
import RoundsMenu from './RoundsMenu';
import SimpleBottomNavigation from './SimpleBottomNavigation';
import UserMenu from './UserMenu';

export default function MainPage(props) {
  const currentLeagueUserId = useSelector(state => state.session.currentLeagueUserId);
  const isAdmin = useSelector(state => state.entities.user.is_admin);
  const dispatch = useDispatch();

  useEffect(() => {
    if (!currentLeagueUserId) {
      dispatch(toggleLeagueModal());
    }
  }, [currentLeagueUserId, dispatch]);

  return (
    <>
      <UserMenu />
      {!currentLeagueUserId ? (
        <HelpPage />
      ) : (
        <Switch>
          <Route path='/draft' exact>
            <DraftPage />
          </Route>
          <Route path='/demo-draft' exact>
            <DemoDraftPage />
          </Route>
          <Route path='/'>
            <RoundsMenu />
            <Switch>
              <Route path='/leaderboard' exact>
                <LeaderboardPage />
              </Route>
              <Route path='/bracket' exact>
                <BracketPage />
              </Route>
              {isAdmin && (
                <Route path='/admin' exact>
                  <AdminPage/>
                </Route>
              )}
              <Redirect from='/' to='/bracket' />
            </Switch>
          </Route>
        </Switch>
      )}
      <LeagueModal />
      <DraftModal />
      <SimpleBottomNavigation />
    </>
  );
}
