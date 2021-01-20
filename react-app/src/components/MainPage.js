import React, { useEffect } from 'react';
import { Redirect, Route, Switch } from "react-router-dom";
import HelpPage from './HelpPage';
import UserMenu from './UserMenu';
import RoundsMenu from './RoundsMenu';
import DraftPage from './DraftPage';
import DemoDraftPage from './DemoDraftPage';
import BracketPage from './BracketPage';
import LeaderboardPage from './LeaderboardPage';
import LeagueModal from './LeagueModal';
import DraftModal from './DraftModal';
import SimpleBottomNavigation from './SimpleBottomNavigation';
import { useDispatch, useSelector } from 'react-redux';
import { toggleLeagueModal } from '../store/actions/ui';


export default function MainPage(props) {
  const currentLeagueUserId = useSelector(state => state.session.currentLeagueUserId);
  const dispatch = useDispatch();

  useEffect(() => {
    if (!currentLeagueUserId) {
      dispatch(toggleLeagueModal())
    }

  }, [currentLeagueUserId, dispatch]);

  return (
    <>
      <UserMenu />
      {!currentLeagueUserId ?
        <HelpPage /> :

        <Switch>
          <Route path='/draft' exact={true} >
            <DraftPage />
          </Route>
          <Route path='/demo-draft' exact={true} >
            <DemoDraftPage />
          </Route>
          <Route path='/'>
            <RoundsMenu />
            <Switch>
              <Route path='/leaderboard' exact={true} >
                <LeaderboardPage />
              </Route>
              <Route path='/bracket' exact={true}>
                <BracketPage />
              </Route>
              <Redirect from='/' to='/bracket' />
            </Switch>
          </Route>
        </Switch>
      }
      <LeagueModal />
      <DraftModal />
      <SimpleBottomNavigation />
    </>
  )
}