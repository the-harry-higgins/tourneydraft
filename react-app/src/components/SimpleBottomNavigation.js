import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import BottomNavigation from '@material-ui/core/BottomNavigation';
import BottomNavigationAction from '@material-ui/core/BottomNavigationAction';
import SportsBasketballIcon from '@material-ui/icons/SportsBasketball';
import EmojiEventsIcon from '@material-ui/icons/EmojiEvents';
import ViewListIcon from '@material-ui/icons/ViewList';
import { NavLink } from 'react-router-dom';

const useStyles = makeStyles(theme => ({
  stickToBottom: {
    width: '100%',
    position: 'fixed',
    bottom: 0,
  },
}));

export default function SimpleBottomNavigation() {
  const classes = useStyles();
  const [value, setValue] = React.useState(0);

  return (
    <BottomNavigation
      value={value}
      onChange={(event, newValue) => {
        setValue(newValue);
      }}
      showLabels
      className={classes.stickToBottom}
    >
      <BottomNavigationAction label="Bracket" icon={<SportsBasketballIcon />} component={NavLink} to='/bracket' />
      <BottomNavigationAction label="Leaderboard" icon={<EmojiEventsIcon />} component={NavLink} to='/leaderboard' />
      <BottomNavigationAction label="Draft" icon={<ViewListIcon />} component={NavLink} to='/draft' />
    </BottomNavigation>
  );
}