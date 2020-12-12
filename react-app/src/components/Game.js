import { makeStyles } from '@material-ui/core';
import React from 'react';

const useStyles = makeStyles(theme => ({
  root: {
    display: 'grid',
    gridTemplateAreas: `'top' 'bottom'`,
    justifyContent: 'stretch',
  },
  top: {
    gridArea: 'top',
    borderBottom: '2px solid black',
  },
  bottom: {
    gridArea: 'bottom',
    borderTop: '2px solid black',
  },
  winner: {
    color: theme.palette.success.main,
  },
  loser: {
    color: theme.palette.error.main,
  }
}));

const order = (thisRound, teams) => {
  if (thisRound === 1) {
    if (teams[0].seed_number > teams[1].seed_number) {
      teams.reverse();
    }
  } else {
    if (teams[0].games_by_round[thisRound - 1] > teams[1].games_by_round[thisRound - 1]) {
      teams.reverse();
    }
  }
  return teams;
}


export default function Game(props) {
  const classes = useStyles();

  if (!props.teams) {
    return (
      <div className={`${classes.root} game${props.bracketGameNum}`}>
        <div className={classes.top}>
        </div>
        <div className={classes.bottom}>
        </div>
      </div>
    )
  }

  const orderedTeams = order(props.thisRound, props.teams);

  if (!props.color) {
    return (
      <div className={`${classes.root} game${props.bracketGameNum}`}>
        <div className={classes.top}>
          {`#${orderedTeams[0].seed_number} ${orderedTeams[0].name}`}
        </div>
        <div className={classes.bottom}>
          {`#${orderedTeams[1].seed_number} ${orderedTeams[1].name}`}
        </div>
      </div>
    );
  }

  const colors = props.game.winning_team_id === orderedTeams[0].id ? 
    [classes.winner, classes.loser] : [classes.loser, classes.winner]

  return (
    <div className={`${classes.root} game${props.bracketGameNum}`}>
      <div className={`${classes.top} ${colors[0]}`}>
        {`#${orderedTeams[0].seed_number} ${orderedTeams[0].name}`}
      </div>
      <div className={`${classes.bottom} ${colors[1]}`}>
        {`#${orderedTeams[1].seed_number} ${orderedTeams[1].name}`}
      </div>
    </div>
  );
}