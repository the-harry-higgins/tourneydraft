export const createDraft = async (tournament, leagueId, draftTime) => {
  const response = await fetch(`/api/leagues/${leagueId}/drafts/`, {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      'tournament_id': tournament.id,
    })
  });
  return await response.json();
}