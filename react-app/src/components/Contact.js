import React from 'react';

import { Typography } from '@material-ui/core';
import { makeStyles } from '@material-ui/core/styles';
import Tooltip from '@material-ui/core/Tooltip';
import GitHubIcon from '@material-ui/icons/GitHub';
import LinkedInIcon from '@material-ui/icons/LinkedIn';
import PortraitIcon from '@material-ui/icons/Portrait';

const useStyles = makeStyles(theme => ({
  icons: {
    display: 'flex',
    paddingTop: theme.spacing(2),
    justifyContent: 'center',
  },
  icon: {
    margin: theme.spacing(1),
  },
}));

export default function Contact() {
  const classes = useStyles();

  return (
    <div className={classes.root}>
      <Typography variant='h2' color='primary'>
        Harrison Higgins
      </Typography>
      <div className={classes.icons}>
        <Tooltip title="Harrison's Portfolio" arrow>
          <PortraitIcon
            fontSize='large'
            className={classes.icon}
            onClick={() => window.open('https://the-harry-higgins.github.io/portfolio/')}
          />
        </Tooltip>
        <Tooltip title="Harrison's GitHub" arrow>
          <GitHubIcon
            fontSize='large'
            className={classes.icon}
            onClick={() => window.open('https://github.com/the-harry-higgins')}
          />
        </Tooltip>
        <Tooltip title="Harrison's LinkedIn" arrow>
          <LinkedInIcon
            fontSize='large'
            className={classes.icon}
            onClick={() => window.open('https://www.linkedin.com/in/harry-higgins-82a8661bb/')}
          />
        </Tooltip>
      </div>
    </div>
  );
}
