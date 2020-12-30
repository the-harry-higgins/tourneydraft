import React, { useEffect, useState } from 'react';
import { makeStyles, withStyles } from '@material-ui/core/styles';
import {
  Table, TableBody, TableCell, TableContainer, TableHead,
  TableRow, Paper, Typography, Radio
} from '@material-ui/core';
import { DraftTeam } from './Team';


const useStyles = makeStyles({
  container: {
    maxHeight: 400,
  },
});

const getAvailableTeams = (marchMadnessTeams, draftedTeams) => {
  const teams = [];
  const ids = Object.values(draftedTeams).map(team => team.march_madness_team_id);
  Object.keys(marchMadnessTeams).forEach(id => {
    if (!ids.includes(Number(id))) {
      teams.push(marchMadnessTeams[id]);
    }
  });
  teams.sort((a, b) => a.seed_number - b.seed_number)
  return teams;
}

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


export default function AvailableTeamsTable(props) {
  const { draftedTeams, marchMadnessTeams, setSelection, selection } = props;
  const [rows, setRows] = useState([]);
  const classes = useStyles();


  useEffect(() => {
    setRows(getAvailableTeams(marchMadnessTeams, draftedTeams));
  }, [draftedTeams, marchMadnessTeams])

  const handleChange = (event) => {
    setSelection(event.target.value);
  };

  return (
    <>
      <Typography variant='h3'>
        Available Teams
      </Typography>
      <TableContainer className={classes.container} component={Paper}>
        <Table stickyHeader className={classes.table} aria-label="simple table">
          <TableHead>
            <StyledTableRow>
              <StyledTableCell align='center'>Select</StyledTableCell>
              <StyledTableCell align='center'>Seed</StyledTableCell>
              <StyledTableCell align='left'>Team</StyledTableCell>
              <StyledTableCell align='center'>Region</StyledTableCell>
            </StyledTableRow>
          </TableHead>
          <TableBody>
            {rows.map((row) => (
              <StyledTableRow hover key={row.id}>
                <StyledTableCell align='center'>
                  <Radio
                    checked={Number(selection) === row.id}
                    onChange={handleChange}
                    value={row.id}
                  />
                </StyledTableCell>
                <StyledTableCell align='center'>{row.seed_number}</StyledTableCell>
                <StyledTableCell align='center'>
                  <DraftTeam team={row} />
                </StyledTableCell>
                <StyledTableCell align='center'>{row.region}</StyledTableCell>
              </StyledTableRow>
            ))}
          </TableBody>
        </Table>
      </TableContainer>
    </>
  );
}