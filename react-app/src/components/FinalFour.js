import React from 'react';
import { useSelector } from 'react-redux';


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
  let championshipWinner = 'Champion';
  const colors = ['','','','','','','']

  if (roundNum >= 5) {
    const winner1 = marchMadnessTeams[games[57].winning_team_id];
    const winner2 = marchMadnessTeams[games[58].winning_team_id];
    const winner3 = marchMadnessTeams[games[59].winning_team_id];
    const winner4 = marchMadnessTeams[games[60].winning_team_id];
    region1winner = winner1.name;
    region2winner = winner2.name;
    region3winner = winner3.name;
    region4winner =winner4.name;
    if (roundNum >= 6) {
      const semi1 = marchMadnessTeams[games[61].winning_team_id];
      const semi2 = marchMadnessTeams[games[62].winning_team_id];
      semi1winner = semi1.name;
      semi2winner = semi2.name;
      if (semi1.id === winner1.id) {
        colors[0] = 'winner';
        colors[1] = 'loser';
      } else {
        colors[1] = 'winner';
        colors[0] = 'loser';
      }
      if (semi2.id === winner3.id) {
        colors[2] = 'winner';
        colors[3] = 'loser';
      } else {
        colors[3] = 'winner';
        colors[2] = 'loser';
      }
      if (roundNum === 7) {
        const champion = marchMadnessTeams[games[62].winning_team_id];
        championshipWinner = champion.name;
        if (champion.id === semi1.id) {
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
      <div className='round5'>
        Final Four
      </div>
      <div className='round5-2'>
        Final Four
      </div>
      <div className='championship'>
        National Championship
      </div>
      <div className={`region1 ${colors[0]}`}>
        {region1winner}
      </div>
      <div className={`region2 ${colors[1]}`}>
        {region2winner}
      </div>
      <div className={`region3 ${colors[2]}`}>
        {region3winner}
      </div>
      <div className={`region4 ${colors[3]}`}>
        {region4winner}
      </div>
      <div className={`semi1 ${colors[4]}`}>
        {semi1winner}
      </div>
      <div className={`semi2 ${colors[5]}`}>
        {semi2winner}
      </div>
      <div className={`champion ${colors[6]}`}>
        {championshipWinner}
      </div>
      <div className='link1' />
      <div className='link2' />
      <div className='link3' />
      <div className='link4' />
    </div>
  );
}