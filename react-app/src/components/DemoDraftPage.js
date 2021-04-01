import React, { useEffect, useState } from 'react';

import { Grid, Paper, Typography } from '@material-ui/core';
import { useDispatch, useSelector } from 'react-redux';

import { setDemoDraftDataAction } from '../store/actions/drafts';
import { setErrors } from '../store/actions/errors';
import AvailableTeamsTable, { getAvailableTeams } from './AvailableTeams';
import DraftInfoBar from './DraftInfoBar';
import SelectionsTable from './SelectionsTable';
import usePageStyles from './styles/PageStyles';

export default function DemoDraftPage() {
  const classes = usePageStyles();
  const currentDraftId = useSelector(state => state.session.currentDraftId);
  const draft = useSelector(state => state.entities.drafts[currentDraftId]);
  const leagueUsers = useSelector(state => state.entities.league_users);
  const draftedTeams = useSelector(state => state.entities.draftedTeams);
  const marchMadnessTeams = useSelector(state => state.entities.marchMadnessTeams);
  const leagues = useSelector(state => state.entities.leagues);
  const user = useSelector(state => state.entities.user);
  const session = useSelector(state => state.session);
  const [selection, setSelection] = useState(null);
  const dispatch = useDispatch();

  useEffect(() => {
    if (draft && draft.drafting) {
      setTimeout(draftTeam, 3000);
    }
  }, [draft]);

  const draftTeam = (leagueUserId = null, selection = null) => {
    if (!leagueUserId && session.currentLeagueUserId === draft.current_drafter_id) {
      return null;
    }
    if (!selection) {
      const availableTeams = getAvailableTeams(marchMadnessTeams, draftedTeams);
      selection = availableTeams[Math.floor(Math.random() * availableTeams.length)].id;
    }
    const draftedTeam = {
      id: draft.draft_index,
      march_madness_team_id: Number(selection),
      league_user_id: draft.current_drafter_id,
      draft_id: draft.id,
      selection_num: draft.draft_index + 1,
    };
    const newDraft = { ...draft };
    newDraft.draft_index += 1;
    newDraft.current_drafter_id = newDraft.draft_order[newDraft.draft_index];
    newDraft.drafted_team_ids.push(selection);
    const data = {
      draft: newDraft,
      draftedTeam,
      messages: [
        `${leagueUsers[draft.current_drafter_id].name} has drafted ${marchMadnessTeams[selection].name}`,
      ],
    };
    dispatch(setDemoDraftDataAction(data));
  };

  const onClick = () => {
    if (session.currentLeagueUserId === draft.current_drafter_id) {
      draftTeam(session.currentLeagueUserId, selection);
    } else {
      dispatch(setErrors(['You are not the current drafter']));
    }
  };

  return (
    <div className={classes.root}>
      <div className={classes.header}>
        <Typography variant='h1'>Draft</Typography>
      </div>
      <Grid className={classes.grid} container spacing={3}>
        <Grid item xs={12}>
          <Paper className={classes.paper}>
            <DraftInfoBar
              user={user}
              marchMadnessTeams={marchMadnessTeams}
              draft={draft}
              league={leagues[session.currentLeagueId]}
              leagueUsers={leagueUsers}
              selection={selection}
              handleClick={onClick}
            />
          </Paper>
        </Grid>
        {draft && draft.drafting ? (
          <>
            <Grid item xs={12} sm={6}>
              <Paper className={classes.paper}>
                <AvailableTeamsTable
                  draftedTeams={draftedTeams}
                  marchMadnessTeams={marchMadnessTeams}
                  setSelection={setSelection}
                  selection={selection}
                />
              </Paper>
            </Grid>
            <Grid item xs={12} sm={6}>
              <Paper className={classes.paper}>
                <SelectionsTable
                  draftedTeams={draftedTeams}
                  draft={draft}
                  leagueUsers={leagueUsers}
                  marchMadnessTeams={marchMadnessTeams}
                />
              </Paper>
            </Grid>
          </>
        ) : draft ? (
          <Grid item xs={12}>
            <Paper className={classes.paper}>
              <SelectionsTable
                draftedTeams={draftedTeams}
                draft={draft}
                leagueUsers={leagueUsers}
                marchMadnessTeams={marchMadnessTeams}
              />
            </Paper>
          </Grid>
        ) : null}
      </Grid>
    </div>
  );
}
