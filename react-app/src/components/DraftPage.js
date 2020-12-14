import React from 'react';
import io from "socket.io-client";
import { baseUrl } from "../config";
import { makeStyles } from '@material-ui/core/styles';
import { Grid, Paper, Typography } from '@material-ui/core';
import { useSelector } from 'react-redux';

const socket = io.connect(baseUrl);
socket.on('error', (error) => {
  console.log('Error');

  console.error(error);
});

socket.on('connect', function () {
  console.log('I connected');
  socket.emit('I\'m connected!');
});
socket.on('disconnect', function () {
  console.log('I disconnected');
});

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    marginBottom: theme.spacing(10),
  },
  paper: {
    padding: theme.spacing(2),
    textAlign: 'center',
    color: theme.palette.text.secondary,
    backgroundColor: theme.palette.secondary.main,
  },
  header: {
    padding: theme.spacing(2),
    textAlign: 'center',
    backgroundColor: theme.palette.secondary.main,
  },
}));

export default function DraftPage(props) {
  // socket.emit('connect', { data: 'I\'m connected!' });
  const classes = useStyles();

  const onClick = () => {
    socket.emit('message', 'Sending a message');
  }

  return (
    <div className={classes.root}>
      <Grid container spacing={3}>
        <Grid item xs={12}>
          <Paper className={classes.header}>
            <Typography variant='h1'>
              Draft
            </Typography>
          </Paper>
        </Grid>
        <Grid item xs={12}>
          <Paper className={classes.paper}>
            <h1>Drafting</h1>
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