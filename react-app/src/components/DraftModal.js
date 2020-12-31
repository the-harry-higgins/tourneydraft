import React from 'react';
import { makeStyles } from '@material-ui/core/styles';
import Modal from '@material-ui/core/Modal';
import Backdrop from '@material-ui/core/Backdrop';
import Fade from '@material-ui/core/Fade';
import { useDispatch, useSelector } from 'react-redux';
import { toggleDraftModal } from '../store/actions/ui';
import DraftForm from './DraftForm';


const useStyles = makeStyles((theme) => ({
  modal: {
    display: 'flex',
    alignItems: 'center',
    justifyContent: 'center',
  },
}));

export default function TransitionsModal(props) {
  const classes = useStyles();
  const showCreateDraft = useSelector(state => state.ui.showCreateDraft);
  const dispatch = useDispatch();

  const handleClose = () => {
    dispatch(toggleDraftModal(null));
  };

  return (
    <Modal
      aria-labelledby="transition-modal-title"
      aria-describedby="transition-modal-description"
      className={classes.modal}
      open={Boolean(showCreateDraft)}
      onClose={handleClose}
      closeAfterTransition
      BackdropComponent={Backdrop}
      BackdropProps={{
        timeout: 500,
      }}
    >
      <Fade in={Boolean(showCreateDraft)}>
        <div>
          <DraftForm leagueId={showCreateDraft} handleClose={handleClose}/>
        </div>
      </Fade>
    </Modal>
  );
}