import { authenticate, login, logout, signUp } from "../../services/auth";

export const SET_USER = 'authentication/SET_USER';
export const REMOVE_USER = 'authentication/REMOVE_USER';

export const removeUser = () => ({ type: REMOVE_USER });
export const setUser = (user) => ({ type: SET_USER, user });

export const authenticateThunk = () => async (dispatch) => {
  function onSuccess(success) {
    dispatch(setUser(success));
    return true;
  }
  function onError(error) {
    // dispatch(setUser(success));
    return false;
  }
  const data = await authenticate();
  if (!data.errors) {
    return onSuccess(data);
  }
  else {
    // dispatch(setErrors(data.errors))
    return onError(data);
  }
};

export const loginThunk = (email, password) => async (dispatch) => {
  function onSuccess(success) {
    dispatch(setUser(success));
    return true;
  }
  function onError(error) {
    // dispatch(setUser(success));
    return false;
  }
  const data = await login(email, password);
  if (!data.errors) {
    return onSuccess(data);
  }
  else {
    // dispatch(setErrors(data.errors))
    return onError(data);
  }
};

export const logoutThunk = () => async (dispatch) => {
  await logout();
  dispatch(removeUser());
};

export const signupThunk = (name, email, password) => async (dispatch) => {
  function onSuccess(success) {
    dispatch(setUser(success));
    return true;
  }
  function onError(error) {
    // dispatch(setUser(success));
    return false;
  }
  const data = await signUp(name, email, password);
  console.log(name, email, password);
  if (!data.errors) {
    return onSuccess(data);
  }
  else {
    // dispatch(setErrors(data.errors))
    return onError(data);
  }
}