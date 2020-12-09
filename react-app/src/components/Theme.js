import React from "react";
import { createMuiTheme, responsiveFontSizes, ThemeProvider } from '@material-ui/core/styles';

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
    }
  },
  spacing: [0, 4, 8, 16, 32, 64],
  typography: {
    button: {
      fontWeight: 'bold'
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
    // background: {
    //   default: '',
    // }
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