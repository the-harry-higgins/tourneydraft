import React from "react";
import { responsiveFontSizes, ThemeProvider } from '@material-ui/core/styles';
import { unstable_createMuiStrictModeTheme as createMuiTheme } from '@material-ui/core';


let theme = createMuiTheme({
  fontFamily: [
      'Ubuntu',
      'sans-serif',
  ].join(','),
  overrides: {
    MuiButton: {
      root: {
        flexGrow: 1
      }
    },
    MuiListItem: {
      root: {
        paddingTop: 0,
        paddingBottom: 0,
      }
    },
    MuiBottomNavigation: {
      root: {
        color: '#FFF',
        backgroundColor: '#546e7a',
      }
    },
    MuiBottomNavigationAction: {
      root: {
        color: '#FFF',
      }
    },
  },
  // spacing: [0, 4, 8, 16, 32, 64],
  typography: {
    fontFamily: [
      'Ubuntu',
      'sans-serif',
    ].join(','),
    button: {
      fontWeight: 'bold',
    },
    h1: {
      color: '#FFF',
      fontFamily: [
        'Lobster',
        'cursive',
      ].join(','),
    },
  },
  palette: {
    primary: {
      main: '#f57c00',
    },
    secondary: {
      main: '#546e7a',
    },
  },
});

theme = responsiveFontSizes(theme)

const Theme = props => {
  return (
    <ThemeProvider theme={theme}>
      { props.children}
    </ThemeProvider>
  )
}

export default Theme;