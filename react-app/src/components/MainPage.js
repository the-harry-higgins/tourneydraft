import React from 'react';
import { Redirect, Route, Switch } from "react-router-dom";
import UserMenu from './UserMenu';
import RoundsMenu from './RoundsMenu';
import DraftPage from './DraftPage';
import BracketPage from './BracketPage';
import LeaderboardPage from './LeaderboardPage';
import SimpleBottomNavigation from './SimpleBottomNavigation';


export default function MainPage(props) {

  return (
    <>
    <UserMenu />
    <Switch>
      <Route path='/draft' exact={true} >
        <DraftPage />
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
    <SimpleBottomNavigation/>
    </>
  )
}