import React, { useState } from "react";
import { useDispatch } from "react-redux";
import { signupThunk } from "../../store/actions/user";
import Button from '@material-ui/core/Button';
import TextField from '@material-ui/core/TextField';
// import AuthStyles from '../styles/AuthStyles';

const SignUpForm = (props) => {
  // const classes = AuthStyles();
  const [name, setName] = useState("");
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const dispatch = useDispatch();

  const handleSubmit = async (e) => {
    e.preventDefault();
    const success = await dispatch(signupThunk(name, email, password));
    if (success) {
      props.setRedirect(true);
    }
  };

  const updateName = (e) => {
    setName(e.target.value);
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
        autoComplete="fname"
        name="name"
        variant="outlined"
        required
        fullWidth
        id="name"
        label="Name"
        autoFocus
        margin="normal"
        value={name}
        onChange={updateName}
      />
      <TextField
        variant="outlined"
        margin="normal"
        required
        fullWidth
        id="email"
        label="Email"
        name="email"
        autoComplete="email"
        type="email"
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

export default SignUpForm;
