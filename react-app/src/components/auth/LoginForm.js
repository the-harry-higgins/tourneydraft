import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { loginThunk } from "../../store/actions/user";
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
// import AuthStyles from '../styles/AuthStyles';

const LoginForm = (props) => {
  // const classes = AuthStyles();
  const [email, setEmail] = useState("demo@aa.io");
  const [password, setPassword] = useState("password");
  const dispatch = useDispatch();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const success = await dispatch(loginThunk(email, password));
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
      // className={classes.form}
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
        // className={classes.submit}
      >
        Continue
      </Button>
    </form>
  );
};

export default LoginForm;
