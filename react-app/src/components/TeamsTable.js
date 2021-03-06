import React from 'react';

import Paper from '@material-ui/core/Paper';
import { withStyles } from '@material-ui/core/styles';
import Table from '@material-ui/core/Table';
import TableBody from '@material-ui/core/TableBody';
import TableCell from '@material-ui/core/TableCell';
import TableContainer from '@material-ui/core/TableContainer';
import TableHead from '@material-ui/core/TableHead';
import TableRow from '@material-ui/core/TableRow';
import { useSelector, useDispatch } from 'react-redux';

import { setSort } from '../store/actions/ui';
import { LeaderboardTeam } from './Team';

function getTeams(player, draftedTeams, marchMadnessTeams, roundNum) {
  const teams = [];
  for (const drafted_team of Object.values(draftedTeams)) {
    if (drafted_team.league_user_id !== player.id) {
      continue;
    }

    const wins =
      roundNum - 1 < marchMadnessTeams[drafted_team.march_madness_team_id].won_game_ids.length
        ? roundNum - 1
        : marchMadnessTeams[drafted_team.march_madness_team_id].won_game_ids.length;
    teams.push({
      ...marchMadnessTeams[drafted_team.march_madness_team_id],
      selectionNum: drafted_team.selection_num,
      wins,
    });
  }
  return teams;
}

function sortBySelection(teams) {
  teams.sort((a, b) => a.selectionNum - b.selectionNum);
  return teams;
}

function sortByName(teams) {
  teams.sort((a, b) => (a.name <= b.name ? -1 : 1));
  return teams;
}

function sortByWins(teams) {
  teams.sort((a, b) => b.wins - a.wins);
  return teams;
}

function sortBySeed(teams) {
  teams.sort((a, b) => {
    return a.seed_number - b.seed_number;
  });
  return teams;
}

function sortByPoints(teams) {
  teams.sort((a, b) => b.points - a.points);
  return teams;
}

function sorted(teams, sortBy) {
  if (sortBy === 'wins') {
    return sortByWins(teams);
  }
  if (sortBy === 'selection') {
    return sortBySelection(teams);
  }
  if (sortBy === 'seed') {
    return sortBySeed(teams);
  }
  if (sortBy === 'points') {
    return sortByPoints(teams);
  }
  if (sortBy === 'name') {
    return sortByName(teams);
  }
}

const StyledTableCell = withStyles(theme => {
  return {
    root: {
      padding: 4,
    },
    head: {
      backgroundColor: theme.palette.background.default,
      color: theme.palette.common.white,
      cursor: 'pointer',
      '&:hover': {
        background: theme.palette.primary.main,
      },
    },
    body: {
      color: theme.palette.background.default,
      textTransform: 'capitalize',
    },
  };
})(TableCell);

const StyledTableRow = withStyles(theme => ({
  root: {
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.action.hover,
    },
  },
}))(TableRow);

export default function TeamsTable(props) {
  const draftedTeams = useSelector(state => state.entities.draftedTeams);
  const marchMadnessTeams = useSelector(state => state.entities.marchMadnessTeams);
  const roundNum = useSelector(state => state.ui.roundNum);
  const sort = useSelector(state => state.ui.sortBy);
  const dispatch = useDispatch();

  const teams = getTeams(props.player, draftedTeams, marchMadnessTeams, roundNum);

  const handleSort = sort => () => {
    dispatch(setSort(sort));
  };

  return (
    <TableContainer component={Paper}>
      <Table aria-label='customized table'>
        <TableHead>
          <TableRow>
            <StyledTableCell align='center' onClick={handleSort('selection')}>
              Selection
            </StyledTableCell>
            <StyledTableCell onClick={handleSort('name')}>Team</StyledTableCell>
            <StyledTableCell align='right' onClick={handleSort('seed')}>
              Seed
            </StyledTableCell>
            <StyledTableCell align='right' onClick={handleSort('wins')}>
              Wins
            </StyledTableCell>
            <StyledTableCell align='right' onClick={handleSort('points')}>
              Points
            </StyledTableCell>
          </TableRow>
        </TableHead>
        <TableBody>
          {sorted(teams, sort).map(team => {
            const color = roundNum - 1 === team.wins ? 'winner' : 'loser';
            return (
              <StyledTableRow key={team.name}>
                <StyledTableCell align='center'>{team.selectionNum}</StyledTableCell>
                <StyledTableCell className={`${color}`}>
                  <LeaderboardTeam team={team} />
                </StyledTableCell>
                <StyledTableCell align='right'>{team.seed_number}</StyledTableCell>
                <StyledTableCell align='right'>{team.wins}</StyledTableCell>
                <StyledTableCell align='right'>{team.points}</StyledTableCell>
              </StyledTableRow>
            );
          })}
        </TableBody>
      </Table>
    </TableContainer>
  );
}
