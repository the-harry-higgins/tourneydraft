import React, { useState } from 'react';

import { Box, Button, Typography } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import { useDispatch } from 'react-redux';
import { Redirect, Link } from 'react-router-dom';

import { ReactComponent as Logo } from '../images/basketball-game.svg';
import { login } from '../services/auth';
import { authenticateThunk } from '../store/actions/authenticate';
import LoginForm from './auth/LoginForm';
import SignUpForm from './auth/SignUpForm';
import Contact from './Contact';
import TheRules from './TheRules';
import TransitionModal from './TransitionModal';
import ForgotPasswordForm from './auth/ForgotPasswordForm';

const useStyles = makeStyles(theme => ({
  root: {
    display: 'flex',
    minHeight: '100vh',
    backgroundColor: theme.palette.secondary.dark,
    [theme.breakpoints.down('sm')]: {
      flexDirection: 'column',
    },
  },
  leftPane: {
    position: 'relative',
    width: '100%',
    backgroundColor: theme.palette.secondary.light,
    padding: theme.spacing(2),
    [theme.breakpoints.down('sm')]: {
      order: 2,
      // height: '100%',
    },
  },
  rightPane: {
    display: 'flex',
    flexDirection: 'column',
    width: '100%',
    paddingTop: theme.spacing(2),
    backgroundColor: theme.palette.secondary.dark,
    alignItems: 'center',
    [theme.breakpoints.down('sm')]: {
      order: 1,
    },
  },
  rulesButton: {
    position: 'absolute',
    top: '45%',
    left: '50%',
    width: 300,
    height: 30,
    marginLeft: -150,
    marginTop: -18,
    [theme.breakpoints.down('sm')]: {
      top: '35%',
    },
  },
  contactButton: {
    position: 'absolute',
    top: '55%',
    left: '50%',
    width: 300,
    height: 30,
    marginLeft: -150,
    marginTop: -18,
    [theme.breakpoints.down('sm')]: {
      top: '65%',
    },
  },
  logoContainer: {
    display: 'flex',
    height: '100%',
    [theme.breakpoints.down('sm')]: {
      flexDirection: 'row-reverse',
    },
  },
  logoBig: {
    width: '100%',
    fill: theme.palette.secondary.main,
    [theme.breakpoints.down('sm')]: {
      // height: '100%',
      width: 130,
    },
  },
  logoSmall: {
    fill: theme.palette.primary.main,
    width: '10%',
  },
  text: {
    marginTop: theme.spacing(4),
    marginBottom: theme.spacing(2),
    color: '#FFF',
    fontSize: '1.3rem',
    fontWeight: 'bold',
    fontFamily: theme.fontFamily,
  },
  button: {
    marginBottom: theme.spacing(2),
    width: 300,
  },
  buttonBottom: {
    marginBottom: theme.spacing(4),
    width: 300,
  },
}));

const SplashPage = props => {
  const classes = useStyles();
  const [redirect, setRedirect] = useState(false);
  const dispatch = useDispatch();

  const demoLogin = (email, password) => async () => {
    const success = await dispatch(authenticateThunk(login, email, password));
    if (success) {
      setRedirect(success);
    }
  };

  const demoDraftLogin = (email, password) => async () => {
    const success = await dispatch(authenticateThunk(login, email, password));
    if (success) {
      setRedirect('/demo-draft');
    }
  };

  if (redirect) {
    return <Redirect to={redirect} />;
  }

  return (
    <Box className={classes.root}>
      <Box className={classes.leftPane}>
        <div className={classes.logoContainer}>
          <Logo className={classes.logoBig} />
        </div>
        <div className={classes.rulesButton}>
          <TransitionModal name='Learn how to Play' variant='outlined' color='primary' width={600}>
            <TheRules />
          </TransitionModal>
        </div>
        <div className={classes.contactButton}>
          <TransitionModal name='Contact the Developer' variant='outlined' color='primary' width={600}>
            <Contact />
          </TransitionModal>
        </div>
      </Box>
      <Box className={classes.rightPane}>
        <Box>
          <Logo className={classes.logoSmall} />
          <Typography variant='h1'>Tourney Draft</Typography>
        </Box>
        <Box className={classes.text}>
          <div>Join a league.</div>
          <div>Draft March Madness Teams.</div>
          <div>Compete against your friends.</div>
        </Box>
        {props.authenticated ? (
          <Button
            className={classes.button}
            variant='contained'
            color='secondary'
            component={Link}
            to='/bracket'
          >
            Home
          </Button>
        ) : (
          <>
            <TransitionModal name='Login' variant='contained' color='secondary' width={400}>
              <LoginForm setRedirect={setRedirect} />
            </TransitionModal>
            <TransitionModal name='Signup' variant='outlined' color='secondary' width={400}>
              <SignUpForm setRedirect={setRedirect} />
            </TransitionModal>
            <TransitionModal name='Forgot Password' variant='outlined' color='secondary' width={400}>
              <ForgotPasswordForm setRedirect={setRedirect} />
            </TransitionModal>
          </>
        )}
        <Button
          className={classes.button}
          color='primary'
          variant='contained'
          onClick={demoLogin('demo@aa.io', 'password')}
        >
          Demo Site
        </Button>
        <Button
          className={classes.buttonBottom}
          color='primary'
          variant='outlined'
          onClick={demoDraftLogin('demodraft@aa.io', 'password')}
        >
          Demo Draft
        </Button>
      </Box>
    </Box>
  );
};

export default SplashPage;
