import React, { useEffect, useRef } from 'react';
import { makeStyles } from '@material-ui/core/styles';
import { Grid, Paper, Typography } from '@material-ui/core';
// import { useSelector } from 'react-redux';
import { getDraftSocket } from '../services/socket';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    marginBottom: theme.spacing(8),
    backgroundColor: 'rgb(0,0,0,0.1)',
    minHeight: '100vh'
  },
  grid: {
    padding: theme.spacing(2),
    [theme.breakpoints.down('sm')]: {
      paddingLeft: 0,
      paddingRight: 0,
    },
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
  },
  header: {
    padding: theme.spacing(2),
    textAlign: 'center',
    backgroundColor: theme.palette.secondary.main,
  },
}));

export default function DraftPage(props) {
  const classes = useStyles();
  const socket = useRef(null);

  useEffect(() => {
    const ws = getDraftSocket();

    socket.current = ws;

    return function cleanup() {
      if (socket.current !== null) {
        socket.current.disconnect();
      }
    }
  }, []);

  const onClick = () => {
    if (socket.current !== null) {
      console.log('Attempting to join draft...');
      socket.current.emit('join', 'I am joing the draft');
    }
  }

  return (
    <div className={classes.root}>
      <div className={classes.header}>
        <Typography variant='h1'>
          Draft
        </Typography>
      </div>
      <Grid className={classes.grid} container spacing={3}>
        <Grid item xs={12}>
          <Paper className={classes.paper}>
            <h1>Drafting</h1>
            <button onClick={onClick}>Send Message</button>
          </Paper>
        </Grid>
        <Grid item xs={12} md={4}>
          <Paper className={classes.paper}>
            <Typography variant='h2'>
              Draft History
            </Typography>
          </Paper>
        </Grid>
        <Grid item xs={12} md={4}>
          <Paper className={classes.paper}>
            <Typography variant='h2'>
              Available Teams
            </Typography>
          </Paper>
        </Grid>
        <Grid item xs={12} md={4}>
          <Paper className={classes.paper}>
            <Typography variant='h2'>
              My Team
            </Typography>
          </Paper>
        </Grid>
      </Grid>
    </div>
  );
}