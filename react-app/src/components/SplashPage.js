import React, { useState } from "react";
import { useDispatch } from 'react-redux';
import { Box, Button, Typography } from '@material-ui/core';
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
    top: '50%',
    left: '50%',
    width: 300,
    height: 30,
    marginLeft: -150,
    marginTop: -18,
  },
  sentence: {
    // fontSize: '0.9rem',
    fontWeight: 'bold',
    paddingTop: theme.spacing(1),
    color: theme.palette.background.default,
  },
  logoContainer: {
    display: 'flex',
    height: '100%',
    [theme.breakpoints.down('sm')]: {
      flexDirection: 'row-reverse'
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
    fontFamily: theme.fontFamily
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
      <Box className={classes.leftPane}>
        <div className={classes.logoContainer}>
          <Logo className={classes.logoBig} />
        </div>
        <div className={classes.rulesButton}>
          <TransitionModal name='Learn how to Play' variant='outlined' color='primary' width={600}>
              <Typography variant='h3' color='primary'>The Rules:</Typography>
              <Typography className={classes.sentence} variant='body1'>Join or create a league of 8 players.</Typography>
              <Typography className={classes.sentence} variant='body1'>The league admin will set a draft time for an upcoming NCAA tournament.</Typography>
              <Typography className={classes.sentence} variant='body1'>Players then draft 8 teams each in snake fashion.</Typography>
              <Typography className={classes.sentence} variant='body1'>When the actual tournament starts, players are awarded points for their drafted teams winning games.</Typography>
              <Typography className={classes.sentence} variant='body1'>You receive points for the seed number as well as the round number.</Typography>
              <Typography className={classes.sentence} variant='body1'>If a 16 seed wins a first round game, the player that owns that team receives 16 + 1 = 17 points.</Typography>
              <Typography className={classes.sentence} variant='body1'>If a 2 seed wins the championship, the player that owns that team receives 2 + 6 = 8 points.</Typography>
          </TransitionModal>
        </div>
      </Box>
      <Box className={classes.rightPane}>
        <Box>
          <Logo className={classes.logoSmall} />
          <Typography variant='h1'>
            Tourney Draft
          </Typography>
        </Box>
        <Box className={classes.text}>
          <div>
            Join a league.
          </div>
          <div>
            Draft March Madness Teams.
          </div>
          <div>
            Compete against your friends.
          </div>
        </Box>
        {props.authenticated ?
          <Button className={classes.button} variant='contained' color='secondary'
            component={Link}
            to='/bracket'
          >
            Home
            </Button> :
          <>
            <TransitionModal name='Login' variant='contained' color='secondary' width={400}>
              <LoginForm setRedirect={setRedirect} />
            </TransitionModal>
            <TransitionModal name='Signup' variant='outlined' color='secondary' width={400}>
              <SignUpForm setRedirect={setRedirect} />
            </TransitionModal>
          </>
        }
        <Button className={classes.button} color="primary" variant='contained' onClick={demoLogin('demodraft@aa.io', 'password')}>Demo Draft</Button>
        <Button className={classes.buttonBottom} color="primary" variant='outlined' onClick={demoLogin('demo@aa.io', 'password')}>Demo Site</Button>
      </Box>
    </Box>
  )
}

export default SplashPage;