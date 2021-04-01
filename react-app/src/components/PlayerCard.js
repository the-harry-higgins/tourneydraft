import React from 'react';

import { makeStyles, Typography } from '@material-ui/core';

import TeamsTable from './TeamsTable';

const useStyles = makeStyles(theme => ({
  root: {
    display: 'flex',
    flexDirection: 'column',
  },
  topRow: {
    display: 'grid',
    gridTemplateColumns: '1fr 5fr 1fr',
  },
  middleRow: {
    color: theme.palette.background.default,
  },
}));

export default function PlayerCard(props) {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <div className={classes.topRow}>
        <div>
          <Typography variant='h2' color='secondary'>
            # {props.rank}
          </Typography>
        </div>
        <div>
          <Typography variant='h4' color='primary'>
            {props.player.name}
          </Typography>
        </div>
      </div>
      <div className={classes.middleRow}>
        <Typography variant='h4'>Total Points: {props.points}</Typography>
      </div>
      <TeamsTable player={props.player} />
    </div>
  );
}
