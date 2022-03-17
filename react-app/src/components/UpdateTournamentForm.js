import React, { useState } from 'react';

import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import { useDispatch } from 'react-redux';

import { updateTournamentThunk } from '../store/actions/admin';

const UpdateTournamentForm = ({ tournamentId }) => {
  const [lastRoundCompleted, setLastRoundCompleted] = useState('');
  const dispatch = useDispatch();

  const handleSubmit = e => {
    e.preventDefault();
    dispatch(updateTournamentThunk(tournamentId, lastRoundCompleted));
  };

  const updateLastRoundCompleted = e => {
    setLastRoundCompleted(e.target.value);
  };

  return (
    <form noValidate onSubmit={handleSubmit}>
      <TextField
        color='secondary'
        variant='outlined'
        margin='normal'
        required
        fullWidth
        id='lastRoundCompleted'
        label='Last Round Completed'
        name='lastRoundCompleted'
        type='text'
        value={lastRoundCompleted}
        onChange={updateLastRoundCompleted}
      />
      <Button type='submit' fullWidth variant='contained' color='secondary'>
        Update
      </Button>
    </form>
  );
};

export default UpdateTournamentForm;
