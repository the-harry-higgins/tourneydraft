import React from 'react';
import { useSelector } from 'react-redux';
import { BracketTeam } from './Team';
import {Typography} from '@material-ui/core';

function getGameByNum(games, num) {
  for (const game of Object.values(games)) {
    if (game.game_num === num) return game;
  }
}

export default function FinalFour(props) {
  const games = useSelector(state => state.entities.games);
  const roundNum = useSelector(state => state.ui.roundNum);
  const marchMadnessTeams = useSelector(state => state.entities.marchMadnessTeams);

  let region1winner = '';
  let region2winner = '';
  let region3winner = '';
  let region4winner = '';
  let semi1winner = '';
  let semi2winner = '';
  let championshipWinner = '';
  const colors = ['','','','','','','']

  if (roundNum >= 5) {
    region1winner = marchMadnessTeams[getGameByNum(games, 57).winning_team_id];
    region2winner = marchMadnessTeams[getGameByNum(games, 58).winning_team_id];
    region3winner = marchMadnessTeams[getGameByNum(games, 59).winning_team_id];
    region4winner = marchMadnessTeams[getGameByNum(games, 60).winning_team_id];
    if (roundNum >= 6) {
      semi1winner = marchMadnessTeams[getGameByNum(games, 61).winning_team_id];
      semi2winner = marchMadnessTeams[getGameByNum(games, 62).winning_team_id];
      if (semi1winner.id === region1winner.id) {
        colors[0] = 'winner';
        colors[1] = 'loser';
      } else {
        colors[1] = 'winner';
        colors[0] = 'loser';
      }
      if (semi2winner.id === region3winner.id) {
        colors[2] = 'winner';
        colors[3] = 'loser';
      } else {
        colors[3] = 'winner';
        colors[2] = 'loser';
      }
      if (roundNum === 7) {
        championshipWinner = marchMadnessTeams[getGameByNum(games, 62).winning_team_id];
        if (championshipWinner.id === semi1winner.id) {
          colors[4] = 'winner';
          colors[5] = 'loser';
        } else {
          colors[5] = 'winner';
          colors[4] = 'loser';
        }
        colors[6] = 'winner';
      }
    }
  }

  return (
    <div className='final-four'>
      <div className='region'>
        <Typography variant='h3'>Final Four</Typography>
      </div>
      <div className='round5'>
        <Typography variant='subtitle1'>Final Four</Typography>
      </div>
      <div className='round5-2'>
        <Typography variant='subtitle1'>Final Four</Typography>
      </div>
      <div className='championship'>
        <Typography variant='subtitle1'>National Championship</Typography>
      </div>
      <div className={`region1 ${colors[0]}`}>
        <BracketTeam team={region1winner} default=''/>
      </div>
      <div className={`region2 ${colors[1]}`}>
        <BracketTeam team={region2winner} default='' />
      </div>
      <div className={`region3 ${colors[2]}`}>
        <BracketTeam team={region3winner} default=''/>
      </div>
      <div className={`region4 ${colors[3]}`}>
        <BracketTeam team={region4winner} default=''/>
      </div>
      <div className={`semi1 ${colors[4]}`}>
        <BracketTeam team={semi1winner} default=''/>
      </div>
      <div className={`semi2 ${colors[5]}`}>
        <BracketTeam team={semi2winner} default=''/>
      </div>
      <div className={`champion ${colors[6]}`}>
        <BracketTeam team={championshipWinner} default='Champion'/>
      </div>
      <div className='link1' />
      <div className='link2' />
      <div className='link3' />
      <div className='link4' />
    </div>
  );
}