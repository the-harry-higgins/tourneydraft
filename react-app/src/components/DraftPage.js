import React, { useEffect, useRef, useState } from 'react';

import { Grid, Paper, Typography } from '@material-ui/core';
import { useDispatch, useSelector } from 'react-redux';

import { getDraftSocket } from '../services/socket';
import { draftedTeamsThunk } from '../store/actions/draftedTeams';
import { setDraftDataAction } from '../store/actions/drafts';
import { setErrors } from '../store/actions/errors';
import AvailableTeamsTable from './AvailableTeams';
import DraftInfoBar from './DraftInfoBar';
import SelectionsTable from './SelectionsTable';
import usePageStyles from './styles/PageStyles';

export default function DraftPage() {
  const classes = usePageStyles();
  const socket = useRef(null);
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
      dispatch(draftedTeamsThunk(draft.id, draft.league_id));
    }
  }, [dispatch]);

  useEffect(() => {
    if (draft && draft.drafting) {
      const ws = getDraftSocket(draft, user);

      socket.current = ws;

      socket.current.on('draft team', function (data) {
        dispatch(setDraftDataAction(data));
      });

      socket.current.on('error', error => {
        dispatch(setErrors(error));
      });

      return function cleanup() {
        if (socket.current !== null) {
          socket.current.disconnect();
        }
      };
    }
  }, [dispatch, user, currentDraftId]);

  const onClick = () => {
    if (socket.current !== null) {
      socket.current.emit('draft team', {
        username: user.name,
        room: draft.id,
        march_madness_team_id: selection,
        league_user_id: session.currentLeagueUserId,
        draft_id: draft.id,
        selection_num: draft.draft_index + 1,
      });
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
