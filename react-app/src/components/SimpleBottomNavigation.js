import React from 'react';

import BottomNavigation from '@material-ui/core/BottomNavigation';
import BottomNavigationAction from '@material-ui/core/BottomNavigationAction';
import { makeStyles } from '@material-ui/core/styles';
import EmojiEventsIcon from '@material-ui/icons/EmojiEvents';
import SportsBasketballIcon from '@material-ui/icons/SportsBasketball';
import ViewListIcon from '@material-ui/icons/ViewList';
import { useSelector } from 'react-redux';
import { NavLink } from 'react-router-dom';

const useStyles = makeStyles(theme => ({
  stickToBottom: {
    width: '100%',
    position: 'fixed',
    bottom: 0,
  },
  active: {
    color: theme.palette.primary.main,
  },
}));

export default function SimpleBottomNavigation() {
  const classes = useStyles();
  const currentDraftId = useSelector(state => state.session.currentDraftId);
  const draftedTeams = useSelector(state => state.entities.draftedTeams);

  return (
    <BottomNavigation showLabels className={classes.stickToBottom}>
      <BottomNavigationAction
        label='Bracket'
        icon={<SportsBasketballIcon />}
        component={NavLink}
        to='/bracket'
        disabled={!currentDraftId}
        activeClassName={classes.active}
      />
      <BottomNavigationAction
        label='Leaderboard'
        icon={<EmojiEventsIcon />}
        component={NavLink}
        to='/leaderboard'
        disabled={!Object.keys(draftedTeams).length}
        activeClassName={classes.active}
      />
      <BottomNavigationAction
        label='Draft'
        icon={<ViewListIcon />}
        component={NavLink}
        to='/draft'
        disabled={!currentDraftId}
        activeClassName={classes.active}
      />
    </BottomNavigation>
  );
}
