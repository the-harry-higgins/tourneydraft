import { logout } from "../../services/auth";
import { setErrors } from "./errors";

export const LOGIN = 'authenticate/LOGIN';
export const LOGOUT = 'authenticate/LOGOUT';

export const loginAction = (data) => ({ type: LOGIN, data });
export const logoutAction = () => ({ type: LOGOUT });

export const authenticateThunk = (callback, ...params) => async (dispatch) => {
  function onSuccess(success) {
    dispatch(loginAction(success));
    let path = '/';
    if (success.messages.info) {
      if (success.messages.info[0] === 'Your league is currently drafting') {
        path = '/draft'
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
  else {
    return onError(data.errors);
  }
};

export const logoutThunk = () => async (dispatch) => {
  await logout();
  dispatch(logoutAction());
};