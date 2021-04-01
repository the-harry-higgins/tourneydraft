import React from 'react';

import { Grid, Paper, Typography } from '@material-ui/core';
import { useSelector } from 'react-redux';
import { Redirect } from 'react-router-dom';

import PlayerCard from './PlayerCard';
import usePageStyles from './styles/PageStyles';

function sort(players, draftedTeams, marchMadnessTeams) {
  const obj = {};
  Object.keys(players).forEach(id => {
    obj[id] = 0;
  });
  Object.keys(draftedTeams).forEach(team_id => {
    obj[draftedTeams[team_id].league_user_id] +=
      marchMadnessTeams[draftedTeams[team_id].march_madness_team_id].points;
  });
  const unsorted = [];
  for (const [id, points] of Object.entries(obj)) {
    unsorted.push({ id, points });
  }
  unsorted.sort((a, b) => b.points - a.points);
  return unsorted;
}

export default function LeaderboardPage() {
  const classes = usePageStyles();
  const players = useSelector(state => state.entities.league_users);
  const draftedTeams = useSelector(state => state.entities.draftedTeams);
  const marchMadnessTeams = useSelector(state => state.entities.marchMadnessTeams);

  if (Object.keys(draftedTeams).length === 0) {
    return <Redirect to='/draft' />;
  }

  const sorted = sort(players, draftedTeams, marchMadnessTeams);

  return (
    <div className={classes.root}>
      <div className={classes.header}>
        <Typography variant='h1'>LeaderBoard</Typography>
      </div>
      <Grid className={classes.grid} container spacing={3}>
        {sorted.map((obj, index) => (
          <Grid key={`leader-${obj.id}`} item xs={12} md={6} lg={4}>
            <Paper className={classes.paper}>
              <PlayerCard rank={index + 1} points={obj.points} player={players[obj.id]} />
            </Paper>
          </Grid>
        ))}
      </Grid>
    </div>
  );
}
