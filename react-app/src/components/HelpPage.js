import React from 'react';

import { Grid, Paper, Typography } from '@material-ui/core';

import usePageStyles from './styles/PageStyles';
import TheRules from './TheRules';

export default function HelpPage(props) {
  const classes = usePageStyles();

  return (
    <div className={classes.root}>
      <div className={classes.header}>
        <Typography variant='h1'>TourneyDraft</Typography>
      </div>
      <Grid className={classes.grid} container spacing={3}>
        <Grid item xs={12}>
          <Paper className={classes.paper}>
            <Typography variant='h2' color='primary'>
              Join or Create a League
            </Typography>
          </Paper>
        </Grid>
        <Grid item xs={12}>
          <Paper className={classes.paper}>
            <TheRules />
          </Paper>
        </Grid>
      </Grid>
    </div>
  );
}
