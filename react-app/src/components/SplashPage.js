import React, { useState } from "react";
import { Box, Button, ButtonGroup, Container, Typography } from '@material-ui/core';
import { ReactComponent as Logo } from '../images/basketball-game.svg'
import { Redirect } from 'react-router-dom';
import TransitionModal from './TransitionModal';
import LoginForm from './auth/LoginForm';
import useSplashPageStyles from '../styles/SplashPageStyles';
import SignUpForm from './auth/SignUpForm';


const SplashPage = (props) => {
  const classes = useSplashPageStyles();
  const [redirect, setRedirect] = useState(false);

  if (redirect) {
    return <Redirect to="/" />;
  }

  return (
    <Box className={classes.root}>
      <Container className={classes.content}>
        <Typography variant='h1' display='block'>
          Tourney Draft
        </Typography>
        <Box className={classes.logo_container}>
          <Logo className={classes.logo}/>
        </Box>
        <Box className={classes.buttons}>
          { props.authenticated ?
            <Button variant='contained' color='secondary'>Home</Button> :
          <>
          <TransitionModal name='Login'>
            <LoginForm setRedirect={setRedirect}/>
          </TransitionModal>
          <TransitionModal name='Signup'>
            <SignUpForm setRedirect={setRedirect}/>
          </TransitionModal>
          </>
          }
        </Box>
        <ButtonGroup color="primary" variant='contained' aria-label="outlined primary button group">
          <Button>Demo Draft</Button>
          <Button>Demo Site</Button>
        </ButtonGroup>
      </Container>
    </Box>
  )
}

export default SplashPage;