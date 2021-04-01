import React, { useEffect, useState } from 'react';

import {
  Button,
  Grid,
  Paper,
  TextField,
  Typography,
  InputLabel,
  MenuItem,
  FormControl,
  Select,
} from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { useDispatch } from 'react-redux';

import { getJoinableLeagues, createLeague, joinLeague } from '../services/leagues';
import { loginAction } from '../store/actions/authenticate';
import { setErrors } from '../store/actions/errors';
import { toggleLeagueModal } from '../store/actions/ui';

const useStyles = makeStyles(theme => ({
  paper: {
    padding: theme.spacing(2),
  },
  formControl: {
    minWidth: 300,
  },
}));

const LeagueForm = () => {
  const classes = useStyles();
  const [newLeagueName, setNewLeagueName] = useState('');
  const [joinLeagueName, setJoinLeagueName] = useState('');
  const [joinableLeagues, setJoinableLeagues] = useState([]);
  const dispatch = useDispatch();

  useEffect(() => {
    const fetchData = async () => {
      const { leagues } = await getJoinableLeagues();
      if (leagues.length) {
        setJoinableLeagues(leagues);
      }
    };

    fetchData();
  }, []);

  const handleNewLeagueSubmit = async e => {
    e.preventDefault();
    const data = await createLeague(newLeagueName);
    if (data.errors) {
      dispatch(setErrors(data.errors));
    } else {
      dispatch(loginAction(data));
      dispatch(toggleLeagueModal());
    }
  };

  const handleJoinLeagueSubmit = async e => {
    e.preventDefault();
    const data = await joinLeague(joinLeagueName);
    if (data) {
      dispatch(loginAction(data));
      dispatch(toggleLeagueModal());
    }
  };

  const updateNewLeagueName = e => {
    setNewLeagueName(e.target.value);
  };

  const updateJoinLeagueName = e => {
    setJoinLeagueName(e.target.value);
  };

  return (
    <Grid className={classes.grid} container spacing={3}>
      <Grid item xs={12} md={6}>
        <Paper className={classes.paper}>
          <Typography variant='h2' color='primary'>
            Join a League
          </Typography>
          <form noValidate onSubmit={handleJoinLeagueSubmit}>
            <FormControl
              variant='outlined'
              margin='normal'
              color='primary'
              fullWidth
              required
              className={classes.formControl}
              disabled={!joinableLeagues.length}
            >
              <InputLabel>League Name</InputLabel>
              <Select value={joinLeagueName} onChange={updateJoinLeagueName} label='League Name'>
                {joinableLeagues.length ? (
                  joinableLeagues.map(league => (
                    <MenuItem key={`joinableLeague-${league.id}`} value={league.name}>
                      {league.name}
                    </MenuItem>
                  ))
                ) : (
                  <MenuItem value='' disabled>
                    No Available Leagues
                  </MenuItem>
                )}
              </Select>
            </FormControl>
            <Button type='submit' fullWidth variant='contained' color='primary' disabled={!joinLeagueName}>
              Join League
            </Button>
          </form>
        </Paper>
      </Grid>
      <Grid item xs={12} md={6}>
        <Paper className={classes.paper}>
          <Typography variant='h2' color='secondary'>
            Create a New League
          </Typography>
          <form noValidate onSubmit={handleNewLeagueSubmit}>
            <TextField
              color='secondary'
              variant='outlined'
              margin='normal'
              required
              fullWidth
              name='name'
              label='League Name'
              type='text'
              id='name'
              value={newLeagueName}
              onChange={updateNewLeagueName}
            />
            <Button type='submit' fullWidth variant='contained' color='secondary' disabled={!newLeagueName}>
              Create New League
            </Button>
          </form>
        </Paper>
      </Grid>
    </Grid>
  );
};

export default LeagueForm;
