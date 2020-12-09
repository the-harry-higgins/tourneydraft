import { makeStyles } from '@material-ui/core/styles'; 

const useSplashPageStyles = makeStyles((theme) => ({
  root: {
    backgroundImage: 'url("/images/background.jpg")',
    backgroundSize: 'auto 100%',
    backgroundRepeat: 'no-repeat',
    backgroundPosition: 'center',
    backgroundColor: theme.palette.background,
    // maxHeight: '100%',
    height: '100vh',
    // overflow: 'hidden',
    // width: '100%',
    display: 'flex'
  },
  content: {
    paddingTop: theme.spacing(4),
    display: 'flex',
    flexDirection: 'column',
    width: '100%',
    alignItems: 'center',
    // justifyContent: 'space-evenly'
  },
  logo_container: {
    paddingTop: theme.spacing(2),
    width: '10%',
  },
  logo: {
    fill: '#FFF'
  },
  buttons: {
    margin: theme.spacing(2),
    display: 'flex',
    flexDirection: 'column',
    width: '20%',
  },
}));

export default useSplashPageStyles;