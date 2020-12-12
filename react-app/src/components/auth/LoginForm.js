import React, { useState } from "react";
import { useDispatch } from "react-redux";
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
import { authenticateThunk } from "../../store/actions/authenticate";
import { login } from '../../services/auth';

const LoginForm = (props) => {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const dispatch = useDispatch();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const success = await dispatch(authenticateThunk(login, email, password));
    if (success) {
      props.setRedirect(true);
    }
  };

  const updateEmail = (e) => {
    setEmail(e.target.value);
  };

  const updatePassword = (e) => {
    setPassword(e.target.value);
  };

  return (
    <form 
      noValidate 
      onSubmit={handleSubmit}>
      <TextField
        variant="outlined"
        margin="normal"
        required
        fullWidth
        id="email"
        label="Email"
        name="email"
        autoComplete="email"
        autoFocus
        type="text"
        value={email}
        onChange={updateEmail}
      />
      <TextField
        variant="outlined"
        margin="normal"
        required
        fullWidth
        name="password"
        label="Password"
        type="password"
        id="password"
        autoComplete="current-password"
        value={password}
        onChange={updatePassword}
      />
      <Button
        type="submit"
        fullWidth
        variant="contained"
        color="primary"
      >
        Continue
      </Button>
    </form>
  );
};

export default LoginForm;
