import { forgotPassword, logout, resetPassword } from '../../services/auth';
import { setErrors } from './errors';

export const LOGIN = 'authenticate/LOGIN';
export const LOGOUT = 'authenticate/LOGOUT';
export const FORGOT_PASSWORD = 'authenticate/FORGOT_PASSWORD';
export const RESET_PASSWORD = 'authenticate/RESET_PASSWORD';

export const loginAction = data => ({ type: LOGIN, data });
export const logoutAction = () => ({ type: LOGOUT });
export const forgotPasswordAction = data => ({ type: FORGOT_PASSWORD, data });
export const resetPasswordAction = data => ({ type: RESET_PASSWORD, data });

export const authenticateThunk = (callback, ...params) => async dispatch => {
  function onSuccess(success) {
    dispatch(loginAction(success));
    let path = '/';
    if (success.messages.info) {
      if (success.messages.info[0] === 'Your league is currently drafting') {
        path = '/draft';
      }
    }
    return path;
  }
  function onError(errors) {
    dispatch(setErrors(errors));
    return false;
  }
  const data = await callback(...params);
  if (!data.errors) {
    return onSuccess(data);
  }
  return onError(data.errors);
};

export const logoutThunk = () => async dispatch => {
  await logout();
  dispatch(logoutAction());
};

export const forgotPasswordThunk = (email) => async dispatch => {
  const data = await forgotPassword(email)

  if (!data.errors) {
    dispatch(forgotPasswordAction(data));
    return true;
  } else {
    dispatch(setErrors(data));
    return false;
  }
};


export const resetPasswordThunk = (password, token) => async dispatch => {
  const data = await resetPassword(password, token)

  if (!data.errors) {
    dispatch(resetPasswordAction(data));
    return true;
  } else {
    dispatch(setErrors(data));
    return false;
  }
};
