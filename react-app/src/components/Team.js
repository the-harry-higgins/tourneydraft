import React from 'react';

import { makeStyles } from '@material-ui/core/styles';

const useStyles = makeStyles(theme => ({
  logo: {
    width: '20%',
    paddingRight: theme.spacing(2),
  },
  draftLogo: {
    height: 25,
    paddingRight: theme.spacing(2),
  },
  bracketLogo: {
    width: '25%',
  },
  teamCell: {
    display: 'flex',
    alignItems: 'center',
  },
  draftCell: {
    display: 'flex',
    alignItems: 'center',
  },
}));

export function LeaderboardTeam(props) {
  const classes = useStyles();
  return (
    <div className={classes.teamCell}>
      <img className={classes.logo} src={`/images/logos/${props.team.logo}`} alt='Logo' />
      <div>{props.team.name}</div>
    </div>
  );
}

export function BracketTeam(props) {
  const classes = useStyles();

  if (!props.team) return props.default;
  return (
    <div className={classes.teamCell}>
      <img className={classes.bracketLogo} src={`/images/logos/${props.team.logo}`} alt='Logo' />
      <div>{`${props.team.seed_number} ${props.team.name}`}</div>
    </div>
  );
}

export function DraftTeam(props) {
  const classes = useStyles();
  return (
    <div className={classes.draftCell}>
      <img className={classes.draftLogo} src={`/images/logos/${props.team.logo}`} alt='Logo' />
      <div>{props.team.name}</div>
    </div>
  );
}
