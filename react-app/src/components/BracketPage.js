import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Paper from '@material-ui/core/Paper';
import Grid from '@material-ui/core/Grid';
import BracketRegion from './BracketRegion';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
}));

export default function BracketPage() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Paper className={classes.paper}>Bracket Page</Paper>
        </Grid>
        <Grid item xs={12} md={6}>
          <Paper className={classes.paper}>
            <BracketRegion regionNum={1}/>
          </Paper>
        </Grid>
        <Grid item xs={12} md={6}>
          <Paper className={classes.paper}>
            <BracketRegion regionNum={3} />
          </Paper>
        </Grid>
        <Grid item xs={12} md={6}>
          <Paper className={classes.paper}>
            <BracketRegion regionNum={2} />
          </Paper>        </Grid>
        <Grid item xs={12} md={6}>
          <Paper className={classes.paper}>
            <BracketRegion regionNum={4} />
          </Paper>        </Grid>
        <Grid item sm={12}>
          <Paper className={classes.paper}>Final Four</Paper>
        </Grid>
      </Grid>
    </div>
  );
}