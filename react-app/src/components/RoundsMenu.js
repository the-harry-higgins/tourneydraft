import React, { useState } from 'react';

import {
  Button,
  ClickAwayListener,
  Hidden,
  List,
  ListItem,
  ListItemText,
  Paper,
  Popper,
} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { ExpandLess, ExpandMore } from '@material-ui/icons';
import { useDispatch, useSelector } from 'react-redux';

import { setRound } from '../store/actions/ui';

const useStyles = makeStyles(theme => ({
  root: {
    position: 'fixed',
    top: 46.5,
    left: 0,
    height: 50,
    marginLeft: theme.spacing(4),
    zIndex: 5,
    [theme.breakpoints.down('md')]: {
      top: 40.5,
      marginLeft: theme.spacing(3),
    },
    [theme.breakpoints.down('sm')]: {
      top: 34.5,
      marginLeft: theme.spacing(1),
    },
    [theme.breakpoints.down('xs')]: {
      top: 23.5,
      marginLeft: theme.spacing(1),
    },
  },
  button: {
    padding: theme.spacing(1),
    color: '#FFF',
  },
  logo: {
    width: 30,
    fill: '#FFF',
    marginRight: theme.spacing(2),
  },
  menu: {
    maxHeight: '60vh',
    overflow: 'auto',
  },
}));

const rounds = [
  { round: 1, name: 'Round 1' },
  { round: 2, name: 'Round 2' },
  { round: 3, name: 'Sweet Sixteen' },
  { round: 4, name: 'Elite Eight' },
  { round: 5, name: 'Final Four' },
  { round: 6, name: 'Championship' },
  { round: 7, name: 'Final' },
];

export default function RoundsMenu() {
  const classes = useStyles();
  const [anchorEl, setAnchorEl] = useState(null);
  const dispatch = useDispatch();
  const open = Boolean(anchorEl);
  const id = open ? 'simple-popper' : undefined;
  const tournament = useSelector(state => state.entities.tournament);
  const roundNum = useSelector(state => state.ui.roundNum);

  const handleClick = event => {
    setAnchorEl(anchorEl ? null : event.currentTarget);
  };

  const handleClickAway = () => {
    setAnchorEl(null);
  };

  const handleRoundChange = roundNum => () => {
    dispatch(setRound(roundNum));
  };

  if (!tournament) {
    return null;
  }

  return (
    <ClickAwayListener onClickAway={handleClickAway}>
      <div className={classes.root}>
        <Button
          variant='contained'
          color='primary'
          size='large'
          onClick={handleClick}
          className={classes.button}
        >
          <Hidden smDown>Rounds</Hidden>
          <Hidden mdUp>Rnd</Hidden>
          {open ? <ExpandLess /> : <ExpandMore />}
        </Button>
        <Popper id={id} open={open} placement='top-start' anchorEl={anchorEl}>
          <Paper className={classes.menu}>
            <List>
              {rounds.map(round => (
                <ListItem
                  key={`round-${round.round}`}
                  button
                  selected={round.round === roundNum}
                  disabled={tournament.last_round_completed < round.round - 1}
                  onClick={handleRoundChange(round.round)}
                >
                  <ListItemText primary={round.name} />
                </ListItem>
              ))}
            </List>
          </Paper>
        </Popper>
      </div>
    </ClickAwayListener>
  );
}
