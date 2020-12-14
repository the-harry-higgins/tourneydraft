import React, { useEffect, useState } from "react";
import { useDispatch, useSelector } from 'react-redux';
import { BrowserRouter, Route, Switch } from "react-router-dom";
import MainPage from './MainPage';
import SplashPage from './SplashPage';
import PrivateRoute from "./auth/PrivateRoute";
import { CssBaseline, Button } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import Theme from './Theme';
import { SnackbarProvider, useSnackbar } from 'notistack';
import { authenticateThunk } from "../store/actions/authenticate";
import { authenticate } from '../services/auth';
import SimpleBackdrop from './SimpleBackdrop';

const useStyles = makeStyles((theme) => ({
  button: {
    color: '#FFF',
  },
}));

function App() {
  const classes = useStyles();
  const isNotLoggedIn = useSelector((state) => !state.session.currentUserId);
  const messages = useSelector((state) => state.messages);
  const [loaded, setLoaded] = useState(false);
  const { enqueueSnackbar, closeSnackbar } = useSnackbar();
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      await dispatch(authenticateThunk(authenticate));
      setLoaded(true);
    })();
  }, [dispatch]);

  useEffect(() => {
    if (messages) {
      Object.keys(messages).forEach(key => {
        messages[key].forEach(message => {
          enqueueSnackbar(message, {variant: key,
            action: (
              <Button className={classes.button} size="small" onClick={() => closeSnackbar()}>
                Close
              </Button>
            ),});
        });
      })
    }
  }, [messages, closeSnackbar, enqueueSnackbar, classes.button])

  if (!loaded) {
    return <SimpleBackdrop/>;
  }

  return (
    <>
      <BrowserRouter>
        <Switch>
          <Route path='/splash' exact={true} >
            <SplashPage authenticated={!isNotLoggedIn} />
          </Route>
          <PrivateRoute path='/' authenticated={!isNotLoggedIn}>
            <MainPage />
          </PrivateRoute>
        </Switch>
      </BrowserRouter>
    </>
  );
}

export default function AppContainer() {
  return (
    <>
      <CssBaseline />
      <Theme>
        <SnackbarProvider maxSnack={2}>
          <App />
        </SnackbarProvider>
      </Theme>
    </>
  )
};
