import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Grid, Paper, Typography } from '@material-ui/core';
import { useSelector } from 'react-redux';
import PlayerCard from './PlayerCard';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    marginBottom: theme.spacing(10),
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
    backgroundColor: theme.palette.secondary.main,
  },
  header: {
    padding: theme.spacing(2),
    textAlign: 'center',
    backgroundColor: theme.palette.secondary.main,
  },
}));

function sort(players, draftedTeams, marchMadnessTeams) {
  const obj = {}
  Object.keys(players).forEach(id => {
    obj[id] = 0;
  });
  Object.keys(draftedTeams).forEach(team_id => {
    obj[draftedTeams[team_id].league_user_id] += marchMadnessTeams[draftedTeams[team_id].march_madness_team_id].points
  });
  const unsorted = []
  for (const [id, points] of Object.entries(obj)) {
    unsorted.push({id, points});
  }
  unsorted.sort((a, b) => b.points - a.points);
  return unsorted;
}

export default function LeaderboardPage() {
  const classes = useStyles();
  const players = useSelector(state => state.entities.league_users);
  const draftedTeams = useSelector(state => state.entities.draftedTeams);
  const marchMadnessTeams = useSelector(state => state.entities.marchMadnessTeams);

  const sorted = sort(players, draftedTeams, marchMadnessTeams)

  return (
    <div className={classes.root}>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Paper className={classes.header}>
            <Typography variant='h1'>
              LeaderBoard
            </Typography>
          </Paper>
        </Grid>
        {sorted.map((obj, index) => (
          <Grid key={`leader-${obj.id}`} item xs={12} md={6} lg={4}>
            <Paper className={classes.paper}>
              <PlayerCard rank={index + 1} points={obj.points} player={players[obj.id]}/>
            </Paper>
          </Grid>
        ))}
      </Grid>
    </div>
  );
}