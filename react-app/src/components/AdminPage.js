import React, { useEffect } from 'react';

import { useDispatch, useSelector } from 'react-redux';

import {
  Grid,
  Paper,
  Typography,
  InputLabel,
  MenuItem,
  FormControl,
  Select,
  Button,
} from '@material-ui/core';

import usePageStyles from './styles/PageStyles';
import { getTournamentsThunk, deleteTournamentThunk } from '../store/actions/admin';
import UpdateTournamentForm from './UpdateTournamentForm';
import CreateTournamentForm from './CreateTournamentForm';
import AdminGame from './AdminGame';

export default function AdminPage(props) {
  const classes = usePageStyles();
  const [tournament, setTournament] = React.useState('');
  const tournaments = useSelector(state => state.admin.tournaments);
  const dispatch = useDispatch();

  const handleTournamentChange = event => {
    setTournament(event.target.value);
  };

  const handleDeleteTournament = () => {
    dispatch(deleteTournamentThunk(tournament));
  };

  React.useEffect(() => {
    dispatch(getTournamentsThunk());
  }, []);

  return (
    <div className={classes.root}>
      <div className={classes.header}>
        <Typography variant='h1'>Admin</Typography>
      </div>
      <Grid className={classes.grid} container spacing={3}>
        <Grid item xs={12}>
          <Paper className={classes.paper}>
            <Typography variant='h2' color='primary'>
              Tournament
            </Typography>
            <Grid container spacing={2}>
              <Grid item xs={12} md={4}>
                <FormControl>
                  <InputLabel id='tournament-select-label'>Tournament</InputLabel>
                  <Select
                    labelId='tournament-select-label'
                    id='tournament-select'
                    value={tournament}
                    label='Tournament'
                    fullWidth
                    onChange={handleTournamentChange}
                  >
                    {Object.entries(tournaments).map(([id, tournament]) => (
                      <MenuItem key={id} value={id}>
                        {tournament.year}
                      </MenuItem>
                    ))}
                  </Select>
                </FormControl>
              </Grid>
              <Grid item xs={12} md={4}>
                <UpdateTournamentForm tournamentId={tournament} />
              </Grid>
              {/* <Grid item xs={3}>
                {tournament && (
                  <Button
                    type='submit'
                    variant='contained'
                    color='secondary'
                    onClick={handleDeleteTournament}
                  >
                    Delete
                  </Button>
                )}
              </Grid> */}
              <Grid item xs={12} md={4}>
                <CreateTournamentForm />
              </Grid>
            </Grid>
          </Paper>
        </Grid>
        <Grid item xs={12}>
          <Paper className={classes.paper}>
            <Typography variant='h2' color='primary'>
              Games
            </Typography>
            <Grid container spacing={2}>
              {tournaments[tournament] &&
                tournaments[tournament].games_ids.sort().map(gameId => <AdminGame gameId={gameId} />)}
            </Grid>
          </Paper>
        </Grid>
      </Grid>
    </div>
  );
}
