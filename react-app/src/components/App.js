import React, { useEffect, useState } from "react";
import { useDispatch } from 'react-redux';
import { BrowserRouter, Route, Switch } from "react-router-dom";
// import MainPage from './MainPage';
import SplashPage from './SplashPage';
import PrivateRoute from "./auth/PrivateRoute";
import { CssBaseline } from '@material-ui/core';
import Theme from './Theme';
import { SnackbarProvider, useSnackbar } from 'notistack';
import { authenticateThunk } from "../store/actions/user";
import { Button } from '@material-ui/core';
import SimpleBackdrop from './SimpleBackdrop';


function App() {
  const [authenticated, setAuthenticated] = useState(false);
  const [loaded, setLoaded] = useState(false);
  const { enqueueSnackbar, closeSnackbar } = useSnackbar();
  const dispatch = useDispatch();

  useEffect(() => {
    (async() => {
      const auth = await dispatch(authenticateThunk());
      setAuthenticated(auth);
      setLoaded(true);
    })();
  }, [dispatch]);

  const handleClick = () => {
    enqueueSnackbar('I love hooks');
  };

  if (!loaded) {
    return <SimpleBackdrop/>;
  }

  return (
    <>
      <BrowserRouter>
        <Switch>
          <Route path='/splash' exact={true} >
            <SplashPage authenticated={authenticated} />
          </Route>
          {/* <ProtectedRoute path='/users/:id/leagues/:id/drafts/:id' authenticated={authenticated}> */}
          <PrivateRoute path='/' authenticated={authenticated}>
            {/* <MainPage /> */}
            <h1>MainPage</h1>
          </PrivateRoute>
        </Switch>
      </BrowserRouter>
      <Button onClick={handleClick}>Show snackbar</Button>
    </>
  );
}

export default function AppContainer() {
  return (
    <>
      <CssBaseline />
      <Theme>
        <SnackbarProvider maxSnack={3}>
          <App />
        </SnackbarProvider>
      </Theme>
    </>
  )
};
