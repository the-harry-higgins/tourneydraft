import React, { useState } from 'react';

import { Typography } from '@material-ui/core';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import { useDispatch } from 'react-redux';

import { signUp } from '../../services/auth';
import { authenticateThunk } from '../../store/actions/authenticate';

const SignUpForm = props => {
  const [name, setName] = useState('');
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const dispatch = useDispatch();

  const handleSubmit = async e => {
    e.preventDefault();
    const success = await dispatch(authenticateThunk(signUp, name, email, password));
    if (success) {
      props.setRedirect(true);
    }
  };

  const updateName = e => {
    setName(e.target.value);
  };

  const updateEmail = e => {
    setEmail(e.target.value.toLowerCase());
  };

  const updatePassword = e => {
    setPassword(e.target.value);
  };

  const updateConfirmPassword = e => {
    setConfirmPassword(e.target.value);
  };

  const matchPassword = () => {
    return password.length > 0 && password === confirmPassword;
  };

  return (
    <form noValidate onSubmit={handleSubmit}>
      <TextField
        autoComplete='fname'
        name='name'
        variant='outlined'
        required
        fullWidth
        id='name'
        label='Name'
        autoFocus
        margin='normal'
        value={name}
        onChange={updateName}
      />
      <TextField
        variant='outlined'
        margin='normal'
        required
        fullWidth
        id='email'
        label='Email'
        name='email'
        autoComplete='email'
        type='email'
        value={email}
        onChange={updateEmail}
      />
      <TextField
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
      {password !== confirmPassword ? (
        <div>
          <Typography>Passwords must match</Typography>
        </div>
      ) : null}
      <TextField
        variant='outlined'
        margin='normal'
        required
        fullWidth
        name='confirmpassword'
        label='Confirm Password'
        type='password'
        id='password'
        value={confirmPassword}
        onChange={updateConfirmPassword}
      />
      <Button type='submit' fullWidth variant='contained' color='primary' disabled={!matchPassword()}>
        Continue
      </Button>
    </form>
  );
};

export default SignUpForm;
