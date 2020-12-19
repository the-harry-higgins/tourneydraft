    { 
      entities: {
        'user': {
            id: 0,
            name: 'name',
            email: 'email'
            profile_image: 'url',
            league_user_ids: [0,1],
            league_ids: [1,2]
        },
        'leagues': {
            0: {
                id: 0,
                name: 'name',
                admin_id: 0,
                draft_ids: [0,1,2],
                league_user_ids: [1,2...]
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
        'leagueUsers': {
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
        draftedTeams: {
            0: {
                id: 0,
                league_user_id: 0,
                draft_id: 0,
                march_madness_team_id: 0,
                selection_num: 64,
            }
        },
        marchMadnessTeams: {
            0: {
                id: 0,
                logo: url,
                name: 'Alabama',
                seed_number: 8,
                region: 'West',
                points: 0,        <--Gets modified by round
                games_by_round: {
                  1: 81           <--Round num : Game id
                },
                won_game_ids: [1,33,...]
            }
        },
        games: {
          0: {
            id: 0,
            tournament_id: 1,
            game_num: 1,
            round_num: 1,
            team_ids: [1,64],
            winning_team_id: 1
          }
        }
        tournament: {
          0: {
            id: 1,
            march_madness_teams_ids: [1,...64],
            game_ids: [1,...63],
            last_round_completed: 1-6,
            region1: 'South',
            region2: 'West',
            region3: 'East',
            region4: 'Midwest',
            year: 2020
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
        roundNum:6,
        sortBy: 'wins',
      }
      messages: {
        error: ['Login failed', ...],
        success: ['Login was successful',...]
      }
    }