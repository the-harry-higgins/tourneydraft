import React, { useState } from 'react';

import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import { useDispatch } from 'react-redux';

import { login } from '../../services/auth';
import { authenticateThunk } from '../../store/actions/authenticate';

const LoginForm = props => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const dispatch = useDispatch();

  const handleSubmit = async e => {
    e.preventDefault();
    const success = await dispatch(authenticateThunk(login, email, password));
    if (success) {
      props.setRedirect(true);
    }
  };

  const updateEmail = e => {
    setEmail(e.target.value.toLowerCase());
  };

  const updatePassword = e => {
    setPassword(e.target.value);
  };

  return (
    <form noValidate onSubmit={handleSubmit}>
      <TextField
        color='secondary'
        variant='outlined'
        margin='normal'
        required
        fullWidth
        id='email'
        label='Email'
        name='email'
        autoComplete='email'
        autoFocus
        type='text'
        value={email}
        onChange={updateEmail}
      />
      <TextField
        color='secondary'
        variant='outlined'
        margin='normal'
        required
        fullWidth
        name='password'
        label='Password'
        type='password'
        id='password'
        autoComplete='current-password'
        value={password}
        onChange={updatePassword}
      />
      <Button type='submit' fullWidth variant='contained' color='secondary'>
        Continue
      </Button>
    </form>
  );
};

export default LoginForm;
