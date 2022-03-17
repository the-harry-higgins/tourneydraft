export const getTournaments = async () => {
  const response = await fetch('/api/admin/tournament', {
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return await response.json();
};

export const getTournament = async tournamentId => {
  const response = await fetch(`/api/admin/tournament/${tournamentId}`, {
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return await response.json();
};

export const createTournament = async (year, region1, region2, region3, region4) => {
  const response = await fetch('/api/admin/tournament', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      year,
      region1,
      region2,
      region3,
      region4,
    }),
  });
  return await response.json();
};

export const updateTournament = async (tournamentId, lastRoundCompleted) => {
  const response = await fetch(`/api/admin/tournament/${tournamentId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      last_round_completed: lastRoundCompleted,
    }),
  });
  return await response.json();
};

export const deleteTournament = async tournamentId => {
  const response = await fetch(`/api/admin/tournament/${tournamentId}`, {
    method: 'DELETE',
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return await response.json();
};

export const getGame = async gameId => {
  const response = await fetch(`/api/admin/game/${gameId}`, {
    headers: {
      'Content-Type': 'application/json',
    },
  });
  return await response.json();
};

export const setGame = async (gameId, gameTeamScore1, gameTeamScore2) => {
  const response = await fetch(`/api/admin/game/${gameId}`, {
    method: 'PUT',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      game_team_score1: {
        id: gameTeamScore1.id,
        score: gameTeamScore1.score,
      },
      game_team_score2: {
        id: gameTeamScore2.id,
        score: gameTeamScore2.score,
      },
    }),
  });
  return await response.json();
};
