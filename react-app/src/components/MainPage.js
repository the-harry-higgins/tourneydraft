import React from 'react';
import { Redirect, Route, Switch } from "react-router-dom";
import UserMenu from './UserMenu';
import RoundsMenu from './RoundsMenu';
import BracketPage from './BracketPage';
import SimpleBottomNavigation from './SimpleBottomNavigation';


export default function MainPage(props) {

  return (
    <>
    <UserMenu />
    <Switch>
      <Route path='/draft' exact={true} >
        <h1>DraftPage</h1>
      </Route>
      <Route path='/'>
        <RoundsMenu />
        <Switch>
          <Route path='/leaderboard' exact={true} >
            <h1>LeaderboardPage</h1>
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