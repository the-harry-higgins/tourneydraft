import React from 'react';

import { Grid, Button, TextField } from '@material-ui/core';

import usePageStyles from './styles/PageStyles';
import { getGame, setGame as updateGame } from '../services/admin';

export default function AdminPage({ gameId }) {
  const classes = usePageStyles();
  const [game, setGame] = React.useState();
  const [gameTeamScore1, setGameTeamScore1] = React.useState();
  const [gameTeamScore2, setGameTeamScore2] = React.useState();
  const [score1, setScore1] = React.useState();
  const [score2, setScore2] = React.useState();

  const handleScore1Change = event => {
    setScore1(event.target.value);
  };

  const handleScore2Change = event => {
    setScore2(event.target.value);
  };

  const handleGetGame = async () => {
    const data = await getGame(gameId);
    console.log(data);
    if (data) {
      setGame(data.game);
      if (data.game.game_team_scores) {
        setGameTeamScore1(data.game.game_team_scores[0]);
        setGameTeamScore2(data.game.game_team_scores[1]);
      }
    }
  };

  const handleSubmitGame = async () => {
    const s1 = { id: gameTeamScore1.id, score: score1 };
    const s2 = { id: gameTeamScore2.id, score: score2 };
    const data = await updateGame(gameId, s1, s2);
    if (data) {
      setGame(data.game);
      if (data.game_team_scores) {
        setGameTeamScore1(data.game_team_scores[0]);
        setGameTeamScore2(data.game_team_scores[1]);
      }
    }
  };

  React.useEffect(() => {
    handleGetGame();
  }, [gameId]);

  if (!game) {
    return <div>loading...</div>;
  }

  return (
    <Grid item xs={12} md={4}>
      <Grid className={classes.grid} container spacing={1}>
        <Grid item xs={12}>
          {`Game Number: ${game.game_num}`}
        </Grid>
        <Grid item xs={12}>
          {`Round Number: ${game.round_num}`}
        </Grid>
        <Grid item xs={12}>
          {`Winning Team: ${game.winning_team ? game.winning_team.name : ''}`}
        </Grid>
        {gameTeamScore1 && (
          <Grid item xs={12}>
            {`Team: ${gameTeamScore1 ? gameTeamScore1.team.name : ''}`}
            <br />
            {`Score: ${gameTeamScore1.score}`}
            <br />
            <TextField
              color='secondary'
              variant='outlined'
              margin='normal'
              id='score1'
              label='Score'
              name='score1'
              type='number'
              value={score1}
              onChange={handleScore1Change}
            />
          </Grid>
        )}
        {gameTeamScore2 && (
          <Grid item xs={12}>
            {`Team: ${gameTeamScore2 ? gameTeamScore2.team.name : ''}`}
            <br />
            {`Score: ${gameTeamScore2.score}`}
            <br />
            <TextField
              color='secondary'
              variant='outlined'
              margin='normal'
              id='score2'
              label='Score'
              name='score2'
              type='number'
              value={score2}
              onChange={handleScore2Change}
            />
          </Grid>
        )}
        <Grid item xs={12}>
          <Button fullWidth variant='contained' color='secondary' onClick={handleSubmitGame}>
            Submit
          </Button>
        </Grid>
      </Grid>
    </Grid>
  );
}
