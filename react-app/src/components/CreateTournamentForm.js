import React, { useState } from 'react';

import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import { useDispatch } from 'react-redux';

import { createTournamentThunk } from '../store/actions/admin';

const CreateTournamentForm = () => {
  const [year, setYear] = useState('');
  const [region1, setRegion1] = useState('');
  const [region2, setRegion2] = useState('');
  const [region3, setRegion3] = useState('');
  const [region4, setRegion4] = useState('');
  const dispatch = useDispatch();

  const handleSubmit = e => {
    e.preventDefault();
    dispatch(createTournamentThunk(year, region1, region2, region3, region4));
  };

  const updateYear = e => {
    setYear(e.target.value);
  };

  const updateRegion1 = e => {
    setRegion1(e.target.value);
  };

  const updateRegion2 = e => {
    setRegion2(e.target.value);
  };

  const updateRegion3 = e => {
    setRegion3(e.target.value);
  };

  const updateRegion4 = e => {
    setRegion4(e.target.value);
  };

  return (
    <form noValidate onSubmit={handleSubmit}>
      <TextField
        color='secondary'
        variant='outlined'
        margin='normal'
        required
        fullWidth
        id='year'
        label='Year'
        name='year'
        type='number'
        value={year}
        onChange={updateYear}
      />
      <TextField
        color='secondary'
        variant='outlined'
        margin='normal'
        required
        fullWidth
        id='region1'
        label='Region 1'
        name='region1'
        type='text'
        value={region1}
        onChange={updateRegion1}
      />
      <TextField
        color='secondary'
        variant='outlined'
        margin='normal'
        required
        fullWidth
        id='region2'
        label='Region 2'
        name='region2'
        type='text'
        value={region2}
        onChange={updateRegion2}
      />
      <TextField
        color='secondary'
        variant='outlined'
        margin='normal'
        required
        fullWidth
        id='region3'
        label='Region 3'
        name='region3'
        type='text'
        value={region3}
        onChange={updateRegion3}
      />
      <TextField
        color='secondary'
        variant='outlined'
        margin='normal'
        required
        fullWidth
        id='region4'
        label='Region 4'
        name='region4'
        type='text'
        value={region4}
        onChange={updateRegion4}
      />
      <Button type='submit' fullWidth variant='contained' color='secondary'>
        Create
      </Button>
    </form>
  );
};

export default CreateTournamentForm;
