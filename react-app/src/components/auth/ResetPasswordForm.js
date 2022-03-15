import React, { useState } from 'react';

import { Typography } from '@material-ui/core';
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import { useDispatch } from 'react-redux';
import { useParams, useHistory } from "react-router-dom";
import { resetPasswordThunk } from '../../store/actions/authenticate';

const ResetPasswordForm = props => {
  const [password, setPassword] = useState('');
  const [confirmPassword, setConfirmPassword] = useState('');
  const dispatch = useDispatch();
  const history = useHistory();
  const { token } = useParams();

  const handleSubmit = async e => {
    e.preventDefault();
    const success = await dispatch(resetPasswordThunk(password, token));
    if (success) {
      history.push('/');
    }
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
        inputProps={{
          autoCapitalize: 'none',
        }}
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
        inputProps={{
          autoCapitalize: 'none',
        }}
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
        Submit
      </Button>
    </form>
  );
};

export default ResetPasswordForm;
