import React, { useEffect, useState } from 'react';
import { makeStyles, withStyles } from '@material-ui/core/styles';
import {
  Table, TableBody, TableCell, TableContainer, TableHead,
  TableRow, Paper, Typography,
} from '@material-ui/core';
import { DraftTeam } from './Team';


const useStyles = makeStyles({
  container: {
    maxHeight: 400,
  },
});

const StyledTableCell = withStyles((theme) => {
  return {
    root: {
      padding: theme.spacing(1),
    },
    head: {
      backgroundColor: theme.palette.background.default,
      color: theme.palette.common.white,
    },
    body: {
      color: theme.palette.background.default,
      textTransform: 'capitalize',
    },
  }
})(TableCell);

const StyledTableRow = withStyles((theme) => ({
  root: {
    '&:nth-of-type(odd)': {
      backgroundColor: theme.palette.action.hover,
    },
  },
}))(TableRow);

const makeSelectionsArray = (draftedTeams, draft, leagueUsers, marchMadnessTeams) => {
  const sorted = Object.values(draftedTeams).sort((a, b) => a.selection_num - b.selection_num);
  return draft['draft_order'].map((leagueUserId, i) => {
    let selection_num = i + 1;
    let drafter = leagueUsers[leagueUserId].name;
    let team = {};
    if (sorted[i]) {
      if (sorted[i].selection_num !== selection_num || sorted[i].league_user_id !== leagueUserId) {
        console.log('ERROR: you got some bugs.');
      }
      team = marchMadnessTeams[sorted[i].march_madness_team_id]
    }
    return {
      selection_num,
      drafter,
      team
    }
  });
}

export default function SelectionsTable(props) {
  const { draftedTeams, draft, leagueUsers, marchMadnessTeams } = props;
  const [rows, setRows] = useState([]);
  const classes = useStyles();


  useEffect(() => {
    setRows(makeSelectionsArray(draftedTeams, draft, leagueUsers, marchMadnessTeams));
  }, [draftedTeams, draft, leagueUsers, marchMadnessTeams])

  return (
    <>
      <Typography variant='h3'>
        Selections
      </Typography>
      <TableContainer className={classes.container} component={Paper}>
        <Table stickyHeader className={classes.table} aria-label="simple table">
          <TableHead>
            <StyledTableRow>
              <StyledTableCell align='center'>Pick</StyledTableCell>
              <StyledTableCell align='center'>Drafter</StyledTableCell>
              <StyledTableCell align='left'>Team</StyledTableCell>
              <StyledTableCell align='center'>Seed</StyledTableCell>
              <StyledTableCell align='center'>Region</StyledTableCell>
            </StyledTableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <StyledTableRow hover key={row.selection_num}>
                <StyledTableCell align='center' component="th" scope="row">
                  {row.selection_num}
                </StyledTableCell>
                <StyledTableCell align='center'>{row.drafter}</StyledTableCell>
                <StyledTableCell align='center'>
                  {row.team.id ?
                    <DraftTeam team={row.team} />
                    : null
                  }
                </StyledTableCell>
                <StyledTableCell align='center'>{row.team.seed_number}</StyledTableCell>
                <StyledTableCell align='center'>{row.team.region}</StyledTableCell>
              </StyledTableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </>
  );
}