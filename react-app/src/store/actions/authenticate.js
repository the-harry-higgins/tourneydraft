import { logout } from "../../services/auth";
import { setErrors } from "./errors";

export const LOGIN = 'authenticate/LOGIN';
export const LOGOUT = 'authenticate/LOGOUT';

export const loginAction = (data) => ({ type: LOGIN, data });
export const logoutAction = () => ({ type: LOGOUT });

export const authenticateThunk = (callback, ...params) => async (dispatch) => {
  function onSuccess(success) {
    dispatch(loginAction(success));
    return true;
  }
  function onError(errors) {
    dispatch(setErrors(errors));
    return false;
  }
  const data = await callback(...params);
  console.log(data);
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