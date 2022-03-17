import React from 'react';

import { Typography } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(theme => ({
  sentence: {
    fontWeight: 'bold',
    paddingTop: theme.spacing(1),
    color: theme.palette.background.default,
  },
}));

export default function TheRules() {
  const classes = useStyles();

  return (
    <>
      <Typography variant='h2' color='primary'>
        The Rules:
      </Typography>
      <Typography className={classes.sentence} variant='body1'>
        Join or create a league of 8 players.
      </Typography>
      <Typography className={classes.sentence} variant='body1'>
        The league admin will set a draft time for an upcoming NCAA tournament.
      </Typography>
      <Typography className={classes.sentence} variant='body1'>
        Players then draft 8 teams each in snake fashion.
      </Typography>
      <Typography className={classes.sentence} variant='body1'>
        When the actual tournament starts, players are awarded points for their drafted teams winning games.
      </Typography>
      <Typography className={classes.sentence} variant='body1'>
        You receive points for the seed number as well as the round number.
      </Typography>
      <Typography className={classes.sentence} variant='body1'>
        If a 16 seed wins a first round game, the player that owns that team receives 16 + 0 = 16 points.
      </Typography>
      <Typography className={classes.sentence} variant='body1'>
        If a 2 seed wins the championship, the player that owns that team receives 2 + 5 = 7 points.
      </Typography>
      <Typography className={classes.sentence} variant='body1'>
        etc.
      </Typography>
      <Typography className={classes.sentence} variant='body1'>
        Most points is a partial winner.
      </Typography>
      <Typography className={classes.sentence} variant='body1'>
        Tournament champion is a partial winner.
      </Typography>
      <Typography className={classes.sentence} variant='body1'>
        Last drafted team that wins gets their buy in back.
      </Typography>
    </>
  );
}
