import { makeStyles } from '@material-ui/core';
import React from 'react';
import { BracketTeam } from './Team';

const useStyles = makeStyles(theme => ({
  root: {
    display: 'grid',
    gridTemplateAreas: `'top' 'bottom'`,
    justifyContent: 'stretch',
    fontSize: '0.8rem'
  },
  top: {
    gridArea: 'top',
    borderBottom: '2px solid #546e7a',
    alignSelf: 'end',
    overflowX: 'hidden',
    whiteSpace: 'nowrap'
  },
  bottom: {
    gridArea: 'bottom',
    borderTop: '2px solid #546e7a',
    overflowX: 'hidden',
    whiteSpace: 'nowrap'
  },
  winner: {
    color: theme.palette.success.main,
  },
  loser: {
    color: theme.palette.error.main,
  },
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
          <BracketTeam team={orderedTeams[0]}/>
        </div>
        <div className={classes.bottom}>
          <BracketTeam team={orderedTeams[1]} />
        </div>
      </div>
    );
  }

  const colors = props.game.winning_team_id === orderedTeams[0].id ? 
    [classes.winner, classes.loser] : [classes.loser, classes.winner]

  return (
    <div className={`${classes.root} game${props.bracketGameNum}`}>
      <div className={`${classes.top} ${colors[0]}`}>
        <BracketTeam team={orderedTeams[0]} />
      </div>
      <div className={`${classes.bottom} ${colors[1]}`}>
        <BracketTeam team={orderedTeams[1]} />
      </div>
    </div>
  );
}