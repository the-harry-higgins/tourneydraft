import React from 'react';

import { Typography } from '@material-ui/core';
import { useSelector } from 'react-redux';

import Game from './Game';

function getRoundGameNums(regionNum, roundNum) {
  const games = [0, 8, 4, 2, 1];
  const start = [0, 1, 33, 49, 57];
  return [...Array(games[roundNum]).keys()].map(num => {
    return num + start[roundNum] + (regionNum - 1) * games[roundNum];
  });
}

function getGameByNum(games, num) {
  for (const game of Object.values(games)) {
    if (game.game_num === num) return game;
  }
}

const links = [
  'link1to9',
  'link2to9',
  'link3to10',
  'link4to10',
  'link5to11',
  'link6to11',
  'link7to12',
  'link8to12',
  'link9to13',
  'link10to13',
  'link11to14',
  'link12to14',
  'link13to15',
  'link14to15',
];

export default function BracketRegion(props) {
  const games = useSelector(state => state.entities.games);
  const roundNum = useSelector(state => state.ui.roundNum);
  const marchMadnessTeams = useSelector(state => state.entities.marchMadnessTeams);

  const createGames = thisRound => {
    const roundGameNums = getRoundGameNums(props.regionNum, thisRound);
    const gameOffsets = [0, 1, 9, 13, 15];
    // Games without teams
    if (thisRound > roundNum) {
      return roundGameNums.map((num, index) => (
        <Game
          key={`game-${num}`}
          bracketGameNum={index + gameOffsets[thisRound]}
          thisRound={thisRound}
          roundNum={roundNum}
          teams={null}
          color={null}
        />
      ));
    }
    if (thisRound === roundNum) {
      return roundGameNums.map((num, index) => (
        <Game
          key={`game-${num}`}
          bracketGameNum={index + gameOffsets[thisRound]}
          thisRound={thisRound}
          roundNum={roundNum}
          teams={[
            marchMadnessTeams[getGameByNum(games, num).team_ids[0]],
            marchMadnessTeams[getGameByNum(games, num).team_ids[1]],
          ]}
          color={false}
        />
      ));
    }
    return roundGameNums.map((num, index) => (
      <Game
        key={`game-${num}`}
        bracketGameNum={index + gameOffsets[thisRound]}
        thisRound={thisRound}
        roundNum={roundNum}
        teams={[
          marchMadnessTeams[getGameByNum(games, num).team_ids[0]],
          marchMadnessTeams[getGameByNum(games, num).team_ids[1]],
        ]}
        game={getGameByNum(games, num)}
        color
      />
    ));
  };

  return (
    <div className={props.regionNum < 3 ? 'bracket-region__left' : 'bracket-region__right'}>
      <div className='region'>
        <Typography variant='h3'>{props.region}</Typography>
      </div>
      <div className='round1'>
        <Typography variant='subtitle1'>Round 1</Typography>
      </div>
      <div className='round2'>
        <Typography variant='subtitle1'>Round 2</Typography>
      </div>
      <div className='round3'>
        <Typography variant='subtitle1'>Sweet Sixteen</Typography>
      </div>
      <div className='round4'>
        <Typography variant='subtitle1'>Elite Eight</Typography>
      </div>
      {createGames(1)}
      {createGames(2)}
      {createGames(3)}
      {createGames(4)}
      {links.map(link => (
        <div key={link} className={link} />
      ))}
    </div>
  );
}
