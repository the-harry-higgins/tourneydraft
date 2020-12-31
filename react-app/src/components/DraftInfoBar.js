import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Typography, Button } from '@material-ui/core';
import { DraftTeam } from './Team';

const useStyles = makeStyles((theme) => ({
  container: {
    display: 'flex',
    // flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    padding: theme.spacing(2),
  },
  space: {
    paddingLeft: theme.spacing(2),
  }
}));

export default function DraftInfoBar(props) {
  const { user, marchMadnessTeams, draft, league, leagueUsers, selection, handleClick } = props;
  const classes = useStyles();

  if (!draft) {
    return (
      <>
        <Typography variant='h3'>
          {league.name} doesn't have any drafts yet.
        </Typography>
        <Typography variant='h3'>
          {league.admin_id === user.id ?
            `You're the league admin. Set up a draft.` :
            `Tell the league admin to set up a draft.`
          }
        </Typography>
      </>
    );
  } else if (draft.drafting) {
    return (
      <>
        <Typography variant='h3'>
          Drafting: {leagueUsers[draft.current_drafter_id].name} <br />
        </Typography>
        <div className={classes.container}>
          <Typography variant='body1'>Selected Team:</Typography>
          {selection ?
          <div className={classes.space}>
            <DraftTeam  team={marchMadnessTeams[selection]} />
          </div>
            : null}
        </div>
        <Button variant='contained' color='secondary' onClick={handleClick}>Draft Team</Button>
      </>
    )
  } else {
    return (
      <Typography variant='h3'>
        History
      </Typography>
    );
  }
}