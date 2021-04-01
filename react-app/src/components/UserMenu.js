import React, { useState } from 'react';

import {
  Button,
  ClickAwayListener,
  Divider,
  Hidden,
  List,
  ListItem,
  ListItemText,
  Paper,
  Popper,
} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { ExpandLess, ExpandMore } from '@material-ui/icons';
import { useSelector, useDispatch } from 'react-redux';

import { ReactComponent as Logo } from '../images/basketball-game.svg';
import { logoutThunk } from '../store/actions/authenticate';
import { draftChangeThunk } from '../store/actions/drafts';
import { deleteLeagueThunk } from '../store/actions/leagues';
import { toggleDraftModal, toggleLeagueModal } from '../store/actions/ui';

const useStyles = makeStyles(theme => ({
  root: {
    position: 'fixed',
    top: 46.5,
    right: 0,
    height: 50,
    marginRight: theme.spacing(4),
    zIndex: 5,
    [theme.breakpoints.down('md')]: {
      top: 40.5,
      marginRight: theme.spacing(3),
    },
    [theme.breakpoints.down('sm')]: {
      top: 34.5,
      marginRight: theme.spacing(1),
    },
    [theme.breakpoints.down('xs')]: {
      top: 23.5,
      marginRight: theme.spacing(1),
    },
  },
  button: {
    padding: theme.spacing(1),
    color: '#FFF',
  },
  logo: {
    width: 26,
    fill: '#FFF',
    marginRight: theme.spacing(1),
  },
  indent: {
    paddingLeft: theme.spacing(4),
  },
  menu: {
    maxHeight: '60vh',
    overflow: 'auto',
  },
}));

export default function UserMenu() {
  const classes = useStyles();
  const [anchorEl, setAnchorEl] = useState(null);
  const user = useSelector(state => state.entities.user);
  const leagues = useSelector(state => state.entities.leagues);
  const drafts = useSelector(state => state.entities.drafts);
  const session = useSelector(state => state.session);
  const dispatch = useDispatch();
  const open = Boolean(anchorEl);
  const id = open ? 'simple-popper' : undefined;

  const handleClick = event => {
    setAnchorEl(anchorEl ? null : event.currentTarget);
  };

  const handleClickAway = () => {
    setAnchorEl(null);
  };

  const handleLogout = () => {
    dispatch(logoutThunk());
  };

  const handleDraftChange = (draftId, leagueId) => () => {
    dispatch(draftChangeThunk(draftId, leagueId));
  };

  const handleNewLeague = () => () => {
    dispatch(toggleLeagueModal());
    handleClickAway();
  };

  const handleNewDraft = leagueId => () => {
    dispatch(toggleDraftModal(leagueId));
    handleClickAway();
  };

  const handleDeleteLeague = leagueId => () => {
    dispatch(deleteLeagueThunk(leagueId, session.currentLeagueId));
    handleClickAway();
  };

  return (
    <ClickAwayListener onClickAway={handleClickAway}>
      <div className={classes.root}>
        <Button variant='contained' color='primary' onClick={handleClick} className={classes.button}>
          <Logo className={classes.logo} />
          <Hidden smDown>{user.name}</Hidden>
          {open ? <ExpandLess /> : <ExpandMore />}
        </Button>
        <Popper id={id} open={open} placement='top-end' anchorEl={anchorEl}>
          <Paper className={classes.menu}>
            <List>
              <ListItem disabled>
                <ListItemText primary={user.email} />
              </ListItem>
              <Divider />
              {Object.keys(leagues).map(leagueId => (
                <div key={`league-${leagueId}`}>
                  <ListItem disabled>
                    <ListItemText primary={leagues[leagueId].name} />
                  </ListItem>
                  {leagues[leagueId].draft_ids.map(id => (
                    <ListItem
                      key={`league-${leagueId}-draft-${id}`}
                      button
                      selected={session.currentDraftId === id}
                      disabled={session.currentDraftId === id}
                      onClick={handleDraftChange(id, leagueId)}
                      className={classes.indent}
                    >
                      <ListItemText primary={`${drafts[id].year}`} />
                    </ListItem>
                  ))}
                  {user.id === leagues[leagueId].admin_id ? (
                    <>
                      <ListItem
                        key={`createdraft-${leagueId}`}
                        button
                        onClick={handleNewDraft(leagueId)}
                        className={classes.indent}
                      >
                        <ListItemText primary='Create New Draft' />
                      </ListItem>
                      {/* { (user.name !== 'DemoDraft' && user.name !== 'Demo') ?
                        <ListItem
                          key={`deleteleague-${leagueId}`}
                          button
                          onClick={handleDeleteLeague(leagueId)}
                          className={classes.indent}
                        >
                          <ListItemText primary={'Delete League'} color='primary' />
                        </ListItem>
                        : null
                      } */}
                    </>
                  ) : null}
                  <Divider />
                </div>
              ))}
              <ListItem button onClick={handleNewLeague()}>
                <ListItemText primary='New League' />
              </ListItem>
              <Divider />
              <ListItem button onClick={handleLogout}>
                <ListItemText primary='Sign Out' />
              </ListItem>
            </List>
          </Paper>
        </Popper>
      </div>
    </ClickAwayListener>
  );
}
