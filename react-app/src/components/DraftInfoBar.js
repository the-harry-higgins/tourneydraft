import React from 'react';
import { Typography, Button } from '@material-ui/core';

export default function DraftInfoBar(props) {
  const { user, marchMadnessTeams, draft, league, leagueUsers, selection, handleClick } = props;

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
          Drafting: {leagueUsers[draft.current_drafter_id].name}
        </Typography>
        <Typography>Selected Team: {selection ? marchMadnessTeams[selection].name : null}</Typography>
        <Button onClick={handleClick}>Draft Team</Button>
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