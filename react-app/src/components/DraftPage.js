import React, { useEffect, useRef, useState } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Grid, Paper, Typography, FormControl, FormControlLabel, Radio, RadioGroup } from '@material-ui/core';
import { getDraftSocket } from '../services/socket';
import { useDispatch, useSelector } from 'react-redux';
import { setDraftDataAction } from '../store/actions/drafts';
import { setErrors } from '../store/actions/errors';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    marginBottom: theme.spacing(8),
    backgroundColor: 'rgb(0,0,0,0.1)',
    minHeight: '100vh'
  },
  grid: {
    padding: theme.spacing(2),
    [theme.breakpoints.down('sm')]: {
      paddingLeft: 0,
      paddingRight: 0,
    },
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
  header: {
    padding: theme.spacing(2),
    textAlign: 'center',
    backgroundColor: theme.palette.secondary.main,
  },
}));

const getAvailableTeams = (marchMadnessTeams, draftedTeams) => {
  const teams = [];
  const ids = Object.values(draftedTeams).map(team => team.march_madness_team_id);
  Object.keys(marchMadnessTeams).forEach(id => {
    if (!ids.includes(Number(id))) {
      teams.push(marchMadnessTeams[id]);
    }
  });
  teams.sort((a, b) => a.seed_number - b.seed_number)
  return teams;
}

export default function DraftPage(props) {
  const classes = useStyles();
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
      const ws = getDraftSocket(draft, user);

      socket.current = ws;

      socket.current.on('draft team', function (data) {
        console.log(data);
        dispatch(setDraftDataAction(data))
      });

      socket.current.on('error', (error) => {
        console.error(error);
        dispatch(setErrors(error))
      });

      return function cleanup() {
        if (socket.current !== null) {
          socket.current.disconnect();
        }
      }
    }
  }, [draft]);

  const handleChange = (event) => {
    setSelection(event.target.value);
  };

  const onClick = () => {
    if (socket.current !== null) {
      console.log('Sending my draft pick...');
      socket.current.emit('draft team', {
        username: user.name,
        room: draft.id,
        march_madness_team_id: selection,
        league_user_id: session.currentLeagueUserId,
        draft_id: draft.id,
        selection_num: draft.draft_index + 1
      });
    }
  }

  const makeSelections = () => {
      const someJSX = draft['draft_order'].map((leagueUserId, i) => {
        let team = '';
        for (const key in draftedTeams) {
            if (draftedTeams[key].selection_num === i + 1) {
              team = marchMadnessTeams[draftedTeams[key].march_madness_team_id].name
            }
        }
        return <li>{`${leagueUsers[leagueUserId].name} ${team}`}</li>
      });
      return (
        <ol>
          {someJSX}
        </ol>
      );
  }

  if (!draft) {
    return (
      <div className={classes.root}>
        <div className={classes.header}>
          <Typography variant='h1'>
            Draft
        </Typography>
        </div>
        <Grid className={classes.grid} container spacing={3}>
          <Grid item xs={12}>
            <Paper className={classes.paper}>
              <Typography variant='h3'>
                {leagues[session.currentLeagueId].name} doesn't have any drafts yet.
              </Typography>
              <Typography variant='h3'>
                {leagues[session.currentLeagueId].admin_id === user.id ?
                `You're the league admin. Set up a draft.` :
                `Tell the league admin to set up a draft.`
                }
              </Typography>
            </Paper>
          </Grid>
        </Grid>
      </div>
    );
  }

  return (
    <div className={classes.root}>
      <div className={classes.header}>
        <Typography variant='h1'>
          Draft
        </Typography>
      </div>
      <Grid className={classes.grid} container spacing={3}>
        {draft && draft.drafting ?
          <Grid item xs={12}>
            <Paper className={classes.paper}>
              <Typography variant='h3'>
                Drafting: {leagueUsers[draft.current_drafter_id].name}
              </Typography>
              {selection ?
                <>
                  <Typography>Selected Team: {marchMadnessTeams[selection].name}</Typography>
                  <button onClick={onClick}>Draft Team</button>
                </> :
                null
              }
            </Paper>
          </Grid> :
          null
        }
        <Grid item xs={12} md={4}>
          <Paper className={classes.paper}>
            <Typography variant='h3'>
              Selections
            </Typography>
            {makeSelections()}
            <ol>
              {draft['draft_order'].map((leagueUserId, i) => (
                <li>{`${leagueUsers[leagueUserId].name}`}</li>
              ))}
            </ol>
          </Paper>
        </Grid>
        <Grid item xs={12} md={4}>
          <Paper className={classes.paper}>
            <Typography variant='h3'>
              Available Teams
            </Typography>
            <FormControl component="fieldset">
              <RadioGroup aria-label="teams" name="teams" value={Number(selection)} onChange={handleChange}>
                {getAvailableTeams(marchMadnessTeams, draftedTeams).map(
                  team => (
                    <FormControlLabel key={`available-team-${team.id}`} value={team.id} control={<Radio />} label={`${team.seed_number} ${team.name} ${team.region}`} />
                  ))
                }
              </RadioGroup>
            </FormControl>
          </Paper>
        </Grid>
        <Grid item xs={12} md={4}>
          <Paper className={classes.paper}>
            <Typography variant='h2'>
              My Team
            </Typography>
          </Paper>
        </Grid>
      </Grid>
    </div>
  );
}