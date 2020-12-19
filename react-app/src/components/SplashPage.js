import React, { useState } from "react";
import { useDispatch } from 'react-redux';
import { Box, Button, ButtonGroup, Container, Typography } from '@material-ui/core';
import { ReactComponent as Logo } from '../images/basketball-game.svg';
import { Redirect, Link } from 'react-router-dom';
import TransitionModal from './TransitionModal';
import LoginForm from './auth/LoginForm';
import { makeStyles } from '@material-ui/core/styles'; 
import SignUpForm from './auth/SignUpForm';
import { authenticateThunk } from "../store/actions/authenticate";
import { login } from '../services/auth';

const useStyles = makeStyles((theme) => ({
  root: {
    backgroundImage: 'url("/images/background.jpg")',
    backgroundSize: 'auto 100%',
    backgroundRepeat: 'no-repeat',
    backgroundPosition: 'center',
    backgroundColor: theme.palette.background.default,
    minHeight: 400,
    height: '100vh',
    display: 'flex'
  },
  content: {
    paddingTop: theme.spacing(4),
    display: 'flex',
    flexDirection: 'column',
    width: '100%',
    alignItems: 'center',
  },
  logo_container: {
    paddingTop: theme.spacing(2),
    width: '10%',
    minWidth: 60,
    maxWidth: 100,
  },
  logo: {
    fill: '#FFF'
  },
  buttons: {
    margin: theme.spacing(2),
    display: 'flex',
    flexDirection: 'column',
    width: '20%',
    minWidth: 200,
  },
}));

const SplashPage = (props) => {
  const classes = useStyles();
  const [redirect, setRedirect] = useState(false);
  const dispatch = useDispatch();

  const demoLogin = (email, password) => async () => {
    const success = await dispatch(authenticateThunk(login, email, password));
    if (success) {
      setRedirect(true);
    }
  };

  if (redirect) {
    return <Redirect to="/" />;
  }

  return (
    <Box className={classes.root}>
      <Container className={classes.content}>
        <Typography variant='h1'>
          Tourney Draft
        </Typography>
        <Box className={classes.logo_container}>
          <Logo className={classes.logo}/>
        </Box>
        <Box className={classes.buttons}>
          { props.authenticated ?
            <Button variant='contained' color='secondary'
              component={Link}
              to='/bracket'
              >
              Home
            </Button> :
          <>
          <TransitionModal name='Login'>
            <LoginForm setRedirect={setRedirect}/>
          </TransitionModal>
          <TransitionModal name='Signup'>
            <SignUpForm setRedirect={setRedirect}/>
          </TransitionModal>
          </>
          }
          <ButtonGroup color="primary" variant='contained' orientation='vertical' aria-label="outlined primary button group">
            <Button onClick={demoLogin('demodraft@aa.io', 'password')}>Demo Draft</Button>
            <Button onClick={demoLogin('demo@aa.io', 'password')}>Demo Site</Button>
          </ButtonGroup>
        </Box>
      </Container>
    </Box>
  )
}

export default SplashPage;