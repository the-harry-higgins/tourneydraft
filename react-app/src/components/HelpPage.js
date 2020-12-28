import React, { useEffect, useRef } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Grid, Paper, Typography } from '@material-ui/core';
import TheRules from './TheRules';
// import { useSelector } from 'react-redux';


const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    paddingBottom: theme.spacing(8),
    backgroundColor: 'rgb(0,0,0,0.1)',
    minHeight: '90vh'
  },
  grid: {
    padding: theme.spacing(2),
    [theme.breakpoints.down('sm')]: {
      paddingLeft: 0,
      paddingRight: 0,
    },
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

export default function HelpPage(props) {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <div className={classes.header}>
        <Typography variant='h1'>
          TourneyDraft
        </Typography>
      </div>
      <Grid className={classes.grid} container spacing={3}>
        <Grid item xs={12}>
          <Paper className={classes.paper}>
            <Typography variant='h2' color='primary'>Join or Create a League</Typography>
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