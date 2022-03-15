import React, { useState } from 'react';

import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import CircularProgress from '@material-ui/core/CircularProgress';
import { useDispatch } from 'react-redux';

import { forgotPasswordThunk } from '../../store/actions/authenticate';

const ForgotPasswordForm = props => {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');
  const [loading, setLoading] = useState(false);
  const [finished, setFinished] = useState(false);
  const [message, setMessage] = useState('');
  const dispatch = useDispatch();

  const handleSubmit = async e => {
    e.preventDefault();
    setLoading(true);
    setFinished(false);
    const success = await dispatch(forgotPasswordThunk(email, password));
    if (success) {
      setMessage('Password reset email sent');
    } else {
      setMessage('Password reset email failed');
    }
    setLoading(false);
    setFinished(true);
  };

  const updateEmail = e => {
    setEmail(e.target.value.toLowerCase());
  };

  const updatePassword = e => {
    setPassword(e.target.value);
  };

  if (loading) {
    return <CircularProgress />;
  }
  if (finished) {
    return <>{message}</>
  }
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
        inputProps={{
          autoCapitalize: 'none',
        }}
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
        Send
      </Button>
    </form>
  );
};

export default ForgotPasswordForm;
