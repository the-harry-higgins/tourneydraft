    { 
      entities: {
        'user': {
            id: 0,
            name: 'name',
            profile_image: 'url',
            league_user_ids: [0,1],
            league_ids: [1,2]
        },
        'leagues': {
            0: {
                id: 0,
                name: 'name',
                admin_id: 0,
                draft_ids: [0,1,2]
            }
        },
        'drafts': {
            0: {
                id: 0,
                league_id: 0,
                year: 2020,
                drafting: True
            }
        },
        'league-users': {
            12: {
                id: 12,
                name: name,
                drafted_team_ids: [1,2,3,4,5,6,7,8]
            },
            52: {
                id: 52,
                name: name,
                drafted_team_ids: [9,10,11,12,13,14,15,16]
            }
        },
        teams: {
            0: {
                id: 0,
                league_user_id: 0,
                draft_id: 0,
                selection_num: 64,
                year: 2020,
                seed_number: 8,
                region: 'West',
            }
        },
        games: {
          0: {
            game_num: 1-63,
            round_num: 1-6,
            winning_team_id,
          }
        }
      },
      session: {
        currentUserId: 1,
        currentLeagueId: 2
        currentLeagueUserId: 2,
        currentDraftId: 3,
      },
      ui: {
        roundNum:6
      }
      messages: {
        error: ['Login failed', ...],
        success: ['Login was successful',...]
      }
    }