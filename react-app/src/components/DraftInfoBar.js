import React from 'react';

import { Typography, Button } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { useDispatch } from 'react-redux';

import { toggleDraftModal } from '../store/actions/ui';
import { DraftTeam } from './Team';

const useStyles = makeStyles(theme => ({
  container: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
    padding: theme.spacing(2),
  },
  container2: {
    display: 'flex',
    flexDirection: 'column',
    alignItems: 'center',
    justifyContent: 'center',
    paddingTop: theme.spacing(2),
  },
  sentence: {
    paddingBottom: theme.spacing(2),
  },
  space: {
    paddingLeft: theme.spacing(2),
  },
}));

export default function DraftInfoBar(props) {
  const { user, marchMadnessTeams, draft, league, leagueUsers, selection, handleClick } = props;
  const classes = useStyles();
  const dispatch = useDispatch();

  const handleNewDraft = () => {
    dispatch(toggleDraftModal(league.id));
  };

  if (!draft) {
    return (
      <>
        <Typography variant='h3'>No Drafts</Typography>
        <div className={classes.container2}>
          <Typography variant='body1' className={classes.sentence}>
            {league.name} doesn't have any drafts yet.
          </Typography>
          {league.admin_id === user.id ? (
            <>
              <Typography variant='body1' className={classes.sentence}>
                You're the league admin. Set up a draft.
              </Typography>
              <Button variant='contained' color='secondary' onClick={handleNewDraft}>
                Create Draft
              </Button>
            </>
          ) : (
            <Typography variant='body1' className={classes.sentence}>
              Tell the league admin to set up a draft.
            </Typography>
          )}
        </div>
      </>
    );
  }
  if (draft.drafting) {
    return (
      <>
        <Typography variant='h3'>
          Drafting: {leagueUsers[draft.current_drafter_id].name} <br />
        </Typography>
        <div className={classes.container}>
          <Typography variant='body1'>Selected Team:</Typography>
          {selection ? (
            <div className={classes.space}>
              <DraftTeam team={marchMadnessTeams[selection]} />
            </div>
          ) : null}
        </div>
        <Button variant='contained' color='secondary' onClick={handleClick}>
          Draft Team
        </Button>
      </>
    );
  }
  return <Typography variant='h3'>History</Typography>;
}
