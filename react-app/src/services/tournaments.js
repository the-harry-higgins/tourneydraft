export const getAvailableTournaments = async (leagueId) => {
  const response = await fetch(`/api/leagues/${leagueId}/tournaments/`, {
    headers: {
      'Content-Type': 'application/json'
    }
  });
  return await response.json();
}