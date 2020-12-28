export const getJoinableLeagues = async () => {
  const response = await fetch('/api/leagues/', {
    headers: {
      'Content-Type': 'application/json'
    }
  });
  return await response.json();
}

export const createLeague = async (name) => {
  const response = await fetch('/api/leagues/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      name,
    })
  });
  return await response.json();
}

export const joinLeague = async (name) => {
  const response = await fetch('/api/leagues/join/', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json'
    },
    body: JSON.stringify({
      name,
    })
  });
  return await response.json();
}