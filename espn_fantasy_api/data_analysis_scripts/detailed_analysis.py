import json

def check_data_availability(filepath):
    """Check what specific data is available in a JSON file."""
    with open(filepath, 'r') as f:
        data = json.load(f)

    results = {
        'owner_names': False,
        'owner_first_last_names': False,
        'owner_profile_pics': False,
        'team_records': False,
        'win_rate': False,
        'streak': False,
        'rosters': False,
        'player_ids': False,
        'player_names': False,
        'team_logos': False,
        'team_names': False,
        'matchup_scores': False,
        'sample_data': {}
    }

    # Check for owner names
    if 'members' in data and len(data['members']) > 0:
        member = data['members'][0]
        results['owner_names'] = 'displayName' in member
        results['owner_first_last_names'] = 'firstName' in member and 'lastName' in member
        results['sample_data']['member_example'] = {
            'displayName': member.get('displayName'),
            'firstName': member.get('firstName'),
            'lastName': member.get('lastName')
        }

    # Check teams
    if 'teams' in data and len(data['teams']) > 0:
        team = data['teams'][0]

        # Check for team info
        results['team_logos'] = 'logo' in team
        results['team_names'] = 'name' in team

        # Check for record
        if 'record' in team and 'overall' in team['record']:
            record = team['record']['overall']
            results['team_records'] = True
            results['win_rate'] = 'percentage' in record or ('wins' in record and 'losses' in record)
            results['streak'] = 'streakType' in record or 'streakLength' in record

            results['sample_data']['record_example'] = {
                'wins': record.get('wins'),
                'losses': record.get('losses'),
                'ties': record.get('ties'),
                'percentage': record.get('percentage'),
                'streakType': record.get('streakType'),
                'streakLength': record.get('streakLength')
            }

        # Check for roster
        if 'roster' in team and 'entries' in team['roster'] and len(team['roster']['entries']) > 0:
            results['rosters'] = True
            entry = team['roster']['entries'][0]
            results['player_ids'] = 'playerId' in entry

            if 'playerPoolEntry' in entry and 'player' in entry['playerPoolEntry']:
                player = entry['playerPoolEntry']['player']
                results['player_names'] = 'fullName' in player

                results['sample_data']['player_example'] = {
                    'playerId': entry.get('playerId'),
                    'fullName': player.get('fullName'),
                    'firstName': player.get('firstName'),
                    'lastName': player.get('lastName')
                }

    # Check matchup scores
    if 'schedule' in data and len(data['schedule']) > 0:
        matchup = data['schedule'][0]
        if 'home' in matchup and 'totalPoints' in matchup['home']:
            results['matchup_scores'] = True
            results['sample_data']['matchup_example'] = {
                'home_teamId': matchup['home'].get('teamId'),
                'home_totalPoints': matchup['home'].get('totalPoints'),
                'away_teamId': matchup['away'].get('teamId'),
                'away_totalPoints': matchup['away'].get('totalPoints'),
                'winner': matchup.get('winner')
            }

    return results

# Files to analyze in detail
key_files = {
    '../sample_data/base_no_views.json': 'Base endpoint (no views)',
    '../sample_data/view_mTeam.json': 'mTeam view',
    '../sample_data/view_mRoster.json': 'mRoster view',
    '../sample_data/view_mMatchup.json': 'mMatchup view',
    '../sample_data/view_mMatchupScore.json': 'mMatchupScore view',
    '../sample_data/combined_team_roster.json': 'mTeam + mRoster',
    '../sample_data/combined_team_roster_standings.json': 'mTeam + mRoster + mStandings',
    '../sample_data/full_combined.json': 'Full combination'
}

print("=" * 100)
print("ESPN FANTASY API - DETAILED DATA AVAILABILITY")
print("=" * 100)

all_results = {}
for filename, description in key_files.items():
    print(f"\n{description} ({filename})")
    print("-" * 100)

    results = check_data_availability(filename)
    all_results[filename] = results

    # Print availability
    data_points = [
        ('Owner Display Names', results['owner_names']),
        ('Owner First/Last Names', results['owner_first_last_names']),
        ('Owner Profile Pictures', results['owner_profile_pics']),
        ('Team Logos', results['team_logos']),
        ('Team Names', results['team_names']),
        ('Team Records (W-L-T)', results['team_records']),
        ('Win Rate/Percentage', results['win_rate']),
        ('Win/Loss Streak', results['streak']),
        ('Rosters', results['rosters']),
        ('Player IDs', results['player_ids']),
        ('Player Names', results['player_names']),
        ('Matchup Scores', results['matchup_scores'])
    ]

    for label, available in data_points:
        status = "[YES]" if available else "[ NO]"
        print(f"  {status} {label}")

# Create summary matrix
print("\n\n" + "=" * 100)
print("SUMMARY MATRIX")
print("=" * 100)

headers = ['Data Point', 'Base', 'mTeam', 'mRoster', 'mMatchup', 'Team+Roster', 'Full']
files_for_matrix = [
    '../sample_data/base_no_views.json',
    '../sample_data/view_mTeam.json',
    '../sample_data/view_mRoster.json',
    '../sample_data/view_mMatchup.json',
    '../sample_data/combined_team_roster.json',
    '../sample_data/full_combined.json'
]

print(f"\n{headers[0]:<30} {headers[1]:^8} {headers[2]:^8} {headers[3]:^10} {headers[4]:^10} {headers[5]:^12} {headers[6]:^8}")
print("-" * 100)

data_points_to_check = [
    ('Owner Names', 'owner_names'),
    ('Owner First/Last', 'owner_first_last_names'),
    ('Team Names', 'team_names'),
    ('Team Logos', 'team_logos'),
    ('Team Records', 'team_records'),
    ('Win Rate', 'win_rate'),
    ('Streak', 'streak'),
    ('Rosters', 'rosters'),
    ('Player IDs', 'player_ids'),
    ('Player Names', 'player_names'),
    ('Matchup Scores', 'matchup_scores')
]

for label, key in data_points_to_check:
    row = [label]
    for filename in files_for_matrix:
        value = "YES" if all_results[filename][key] else "NO"
        row.append(value)

    print(f"{row[0]:<30} {row[1]:^8} {row[2]:^8} {row[3]:^10} {row[4]:^10} {row[5]:^12} {row[6]:^8}")

# Save detailed results
with open('detailed_analysis_results.json', 'w') as f:
    json.dump(all_results, indent=4, fp=f)

print("\n[SUCCESS] Detailed analysis saved to detailed_analysis_results.json")
