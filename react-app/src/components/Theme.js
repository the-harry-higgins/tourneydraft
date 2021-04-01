import React from 'react';

import { unstable_createMuiStrictModeTheme as createMuiTheme } from '@material-ui/core';
import { responsiveFontSizes, ThemeProvider } from '@material-ui/core/styles';

let theme = createMuiTheme({
  fontFamily: ['Ubuntu', 'sans-serif'].join(','),
  overrides: {
    MuiListItem: {
      root: {
        paddingTop: 0,
        paddingBottom: 0,
      },
    },
    MuiBottomNavigation: {
      root: {
        backgroundColor: '#1976d2',
      },
    },
    MuiBottomNavigationAction: {
      root: {
        color: '#FFF',
      },
    },
    MuiButtonBase: {
      root: {
        '&$disabled': {
          opacity: 0.5,
        },
      },
      disabled: {},
    },
    PrivateSwitchBase: {
      root: {
        padding: 0,
      },
    },
  },
  typography: {
    fontFamily: ['Ubuntu', 'sans-serif'].join(','),
    color: '#546e7a',
    button: {
      fontWeight: 'bold',
    },
    h1: {
      color: '#FFF',
      fontFamily: ['Lobster', 'cursive'].join(','),
    },
    h2: {
      color: '#FFF',
      fontSize: '2rem',
      fontFamily: ['Lobster', 'cursive'].join(','),
    },
  },
  palette: {
    primary: {
      main: '#f57c00',
      contrastText: '#ffffff',
    },
    secondary: {
      main: '#1976d2',
    },
    background: {
      default: '#546e7a',
    },
  },
});

theme = responsiveFontSizes(theme);

const Theme = props => {
  return <ThemeProvider theme={theme}>{props.children}</ThemeProvider>;
};

export default Theme;
