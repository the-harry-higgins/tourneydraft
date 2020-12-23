import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Grid, Paper, Typography } from '@material-ui/core';
import BracketRegion from './BracketRegion';
import FinalFour from './FinalFour';
import { useSelector } from 'react-redux';
import { Redirect } from 'react-router-dom';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    marginBottom: theme.spacing(10),
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
  header: {
    padding: theme.spacing(2),
    textAlign: 'center',
    backgroundColor: theme.palette.secondary.main,
  },
}));

export default function BracketPage() {
  const classes = useStyles();
  const tournament = useSelector(state => state.entities.tournament)

  if (!tournament) {
    return <Redirect to="/draft" />;
  }

  return (
    <div className={classes.root}>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Paper className={classes.header}>
            <Typography variant='h1'>
              Bracket
            </Typography>
          </Paper>
        </Grid>
        <Grid item xs={12} md={6}>
          <Paper className={classes.paper}>
            <BracketRegion regionNum={1} region={tournament.region1}/>
          </Paper>
        </Grid>
        <Grid item xs={12} md={6}>
          <Paper className={classes.paper}>
            <BracketRegion regionNum={3} region={tournament.region3}/>
          </Paper>
        </Grid>
        <Grid item xs={12} md={6}>
          <Paper className={classes.paper}>
            <BracketRegion regionNum={2} region={tournament.region2}/>
          </Paper>        </Grid>
        <Grid item xs={12} md={6}>
          <Paper className={classes.paper}>
            <BracketRegion regionNum={4} region={tournament.region4}/>
          </Paper>       
        </Grid>
        <Grid item sm={12}>
          <Paper className={classes.paper}>
            <FinalFour/>
          </Paper>
        </Grid>
      </Grid>
    </div>
  );
}