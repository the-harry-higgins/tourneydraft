import React, { useState } from 'react';
import { useDispatch, useSelector } from 'react-redux';
import { ExpandLess, ExpandMore } from "@material-ui/icons";
import { makeStyles } from '@material-ui/core/styles';
import { Button, ClickAwayListener, List, ListItem, ListItemText, Paper, Popper } from '@material-ui/core';
import { setRound } from '../store/actions/ui';


const useStyles = makeStyles((theme) => ({
  root: {
    position: 'fixed',
    top: 0,
    left: 0,
    height: 50,
    marginTop: theme.spacing(1),
    marginLeft: theme.spacing(1),
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
}));

const rounds = [
  {round: 1, name: 'Round 1'},
  {round: 2, name: 'Round 2'},
  {round: 3, name: 'Sweet Sixteen'},
  {round: 4, name: 'Elite Eight'},
  {round: 5, name: 'Final Four'},
  {round: 6, name: 'Championship'},
  {round: 7, name: 'Final'},
]

export default function RoundsMenu() {
  const classes = useStyles();
  const [anchorEl, setAnchorEl] = useState(null);
  const dispatch = useDispatch();
  const open = Boolean(anchorEl);
  const id = open ? 'simple-popper' : undefined;
  const tournament = useSelector(state => state.entities.tournament);
  const roundNum = useSelector(state => state.ui.roundNum)

  const handleClick = (event) => {
    setAnchorEl(anchorEl ? null : event.currentTarget);
  };

  const handleClickAway = () => {
    setAnchorEl(null);
  };

  const handleRoundChange = (roundNum) => () => {
    dispatch(setRound(roundNum));
  };

  return (
    <ClickAwayListener onClickAway={handleClickAway}>
      <div className={classes.root}>
        <Button variant="contained" color="primary" size='large' onClick={handleClick} className={classes.button}>
          Rounds
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
                  onClick={handleRoundChange(round.round)}>
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
