import React, { useState } from 'react';
import { useDispatch } from 'react-redux';
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

export default function UserMenu() {
  const classes = useStyles();
  const [anchorEl, setAnchorEl] = useState(null);
  const dispatch = useDispatch();
  const open = Boolean(anchorEl);
  const id = open ? 'simple-popper' : undefined;

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
              <ListItem button onClick={handleRoundChange(1)}>
                <ListItemText primary="Round 1" />
              </ListItem>
              <ListItem button onClick={handleRoundChange(2)}>
                <ListItemText primary="Round 2" />
              </ListItem>
              <ListItem button onClick={handleRoundChange(3)}>
                <ListItemText primary="Sweet Sixteen" />
              </ListItem>
              <ListItem button onClick={handleRoundChange(4)}>
                <ListItemText primary="Elite Eight" />
              </ListItem>
              <ListItem button onClick={handleRoundChange(5)}>
                <ListItemText primary="Final Four" />
              </ListItem>
              <ListItem button onClick={handleRoundChange(6)}>
                <ListItemText primary="Championship" />
              </ListItem>
              <ListItem button onClick={handleRoundChange(7)}>
                <ListItemText primary="Final" />
              </ListItem>
            </List>
          </Paper>
        </Popper>
      </div>
    </ClickAwayListener>
  );
}
