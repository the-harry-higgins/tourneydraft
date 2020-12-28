import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Modal from '@material-ui/core/Modal';
import Backdrop from '@material-ui/core/Backdrop';
import Fade from '@material-ui/core/Fade';
import { useDispatch, useSelector } from 'react-redux';
import { toggleLeagueModal } from '../store/actions/ui';
import LeagueForm from './LeagueForm';


const useStyles = makeStyles((theme) => ({
  modal: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
}));

export default function TransitionsModal(props) {
  const classes = useStyles();
  const showJoinLeague = useSelector(state => state.ui.showJoinLeague);
  const dispatch = useDispatch();

  const handleClose = () => {
    dispatch(toggleLeagueModal());
  };

  return (
    <Modal
      aria-labelledby="transition-modal-title"
      aria-describedby="transition-modal-description"
      className={classes.modal}
      open={showJoinLeague}
      onClose={handleClose}
      closeAfterTransition
      BackdropComponent={Backdrop}
      BackdropProps={{
        timeout: 500,
      }}
    >
      <Fade in={showJoinLeague}>
        <div>
          <LeagueForm />
        </div>
      </Fade>
    </Modal>
  );
}