import React from 'react';
import { makeStyles, Typography } from '@material-ui/core';
import TeamsTable from './TeamsTable';

const useStyles = makeStyles(theme => ({
  root: {
    display: 'flex',
    flexDirection: 'column',
    backgroundColor: theme.palette.secondary.main,
  },
  topRow: {
    display: 'grid',
    gridTemplateColumns: '1fr 2fr 1fr',
  },
}))
export default function PlayerCard(props) {
  const classes = useStyles();
  return (
    <div className={classes.root}>
      <div className={classes.topRow}>
        <div>
          <Typography variant='h2'># {props.rank}</Typography>
        </div>
        <div>
          <Typography variant='h2' color='primary'>{props.player.name}</Typography>
        </div>
      </div>
      <div className={classes.middleRow}>
        <Typography variant='h2'>Total Points: {props.points}</Typography>
      </div>
      <TeamsTable player={props.player}/>
    </div>
  );
}