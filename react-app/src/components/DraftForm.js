import React, { useEffect, useState } from "react";
import { useDispatch } from "react-redux";
import { makeStyles } from '@material-ui/core/styles';
import { Button, Paper, Typography, InputLabel, MenuItem, FormControl, Select } from '@material-ui/core';
import { getAvailableTournaments } from "../services/tournaments";
import { createDraftThunk } from '../store/actions/drafts';


const useStyles = makeStyles((theme) => ({
  paper: {
    padding: theme.spacing(2),
  },
  formControl: {
    minWidth: 300,
  },
}));

const DraftForm = (props) => {
  const { leagueId, handleClose } = props;
  const classes = useStyles();
  const [tournament, setTournament] = useState("");
  // const [draftTime, setDraftTime] = useState("");
  const [availableTournaments, setAvailableTournaments] = useState([]);
  const dispatch = useDispatch();

  useEffect(() => {
    if (leagueId){
      const fetchData = async () => {
        const { tournaments } = await getAvailableTournaments(leagueId);
        if (tournaments.length) {
          setAvailableTournaments(tournaments);
        }
      }
  
      fetchData();
    }
  }, [leagueId]);

  const handleSubmit = async (e) => {
    e.preventDefault();
    dispatch(createDraftThunk(tournament, leagueId));
    handleClose();
  };

  const updateTournament = (e) => {
    setTournament(e.target.value);
  };

  // const updateDraftTime = (e) => {
  //   setDraftTime(e.target.value);
  // };

  return (
    <Paper className={classes.paper}>
      <Typography variant='h2' color='primary'>Create A Draft</Typography>
      <form
        noValidate
        onSubmit={handleSubmit}>
        <FormControl
          variant="outlined"
          margin="normal"
          color='primary'
          fullWidth
          required
          className={classes.formControl}
          disabled={!availableTournaments.length}>
          <InputLabel>Tournament Year</InputLabel>
          <Select
            value={tournament}
            onChange={updateTournament}
            label="Tournament Year"
          >
            {availableTournaments.length ?
              availableTournaments.map(tournament => (
                <MenuItem
                  key={`availableTournaments-${tournament.id}`}
                  value={tournament}>
                  {tournament.year}
                </MenuItem>
              )) :
              <MenuItem value="" disabled>
                No Available Tournaments
                    </MenuItem>
            }
          </Select>
        </FormControl>
        <Button
          type="submit"
          fullWidth
          variant="contained"
          color="primary"
          disabled={!tournament}
        >
          Create Draft
        </Button>
      </form>
    </Paper>
  );
};

export default DraftForm;
