import json
import os

def analyze_json_structure(filepath):
    """Analyze JSON file structure and return key findings."""
    with open(filepath, 'r') as f:
        data = json.load(f)

    findings = {
        'filename': os.path.basename(filepath),
        'top_level_keys': list(data.keys()) if isinstance(data, dict) else [],
        'has_members': 'members' in data if isinstance(data, dict) else False,
        'has_teams': 'teams' in data if isinstance(data, dict) else False,
        'has_schedule': 'schedule' in data if isinstance(data, dict) else False,
        'has_settings': 'settings' in data if isinstance(data, dict) else False,
        'has_standings': 'standings' in data if isinstance(data, dict) else False,
        'file_size_kb': round(os.path.getsize(filepath) / 1024, 2)
    }

    # Check team structure if teams exist
    if findings['has_teams'] and isinstance(data.get('teams'), list) and len(data['teams']) > 0:
        team = data['teams'][0]
        findings['team_keys'] = list(team.keys())
        findings['has_roster_in_team'] = 'roster' in team
        findings['has_record_in_team'] = 'record' in team
        findings['has_owners_in_team'] = 'owners' in team

    # Check members structure
    if findings['has_members'] and isinstance(data.get('members'), list) and len(data['members']) > 0:
        member = data['members'][0]
        findings['member_keys'] = list(member.keys())

    # Check schedule/matchup structure
    if findings['has_schedule'] and isinstance(data.get('schedule'), list) and len(data['schedule']) > 0:
        matchup = data['schedule'][0]
        findings['matchup_keys'] = list(matchup.keys())
        if 'away' in matchup:
            findings['matchup_away_keys'] = list(matchup['away'].keys())
        if 'home' in matchup:
            findings['has_rosterForMatchupPeriod'] = 'rosterForMatchupPeriod' in matchup.get('home', {})

    # Check standings
    if findings['has_standings'] and isinstance(data.get('standings'), dict):
        findings['standings_keys'] = list(data['standings'].keys())

    return findings

# Analyze all JSON files
json_files = [
    '../sample_data/base_no_views.json',
    '../sample_data/view_mMatchup.json',
    '../sample_data/view_mMatchupScore.json',
    '../sample_data/view_mTeam.json',
    '../sample_data/view_mSettings.json',
    '../sample_data/view_mStandings.json',
    '../sample_data/view_mRoster.json',
    '../sample_data/view_mStatus.json',
    '../sample_data/combined_team_roster.json',
    '../sample_data/combined_matchup_scores.json',
    '../sample_data/combined_team_standings.json',
    '../sample_data/combined_team_roster_standings.json',
    '../sample_data/full_combined.json'
]

print("=" * 80)
print("ESPN FANTASY API - ANALYZING ALL VIEWS")
print("=" * 80)

results = {}
for filename in json_files:
    if os.path.exists(filename):
        print(f"\nAnalyzing: {filename}")
        findings = analyze_json_structure(filename)
        results[filename] = findings

        # Print key findings
        print(f"  Size: {findings['file_size_kb']} KB")
        print(f"  Top-level keys: {', '.join(findings['top_level_keys'])}")

        if findings.get('team_keys'):
            print(f"  Team object keys: {', '.join(findings['team_keys'])}")
        if findings.get('member_keys'):
            print(f"  Member object keys: {', '.join(findings['member_keys'])}")

print("\n" + "=" * 80)
print("KEY FINDINGS SUMMARY")
print("=" * 80)

# Summary table
print("\n{:<40} {:>10} {:>10} {:>10} {:>10}".format(
    "File", "Members", "Teams", "Schedule", "Roster"
))
print("-" * 80)

for filename, findings in results.items():
    has_members = "YES" if findings.get('has_members') else "NO"
    has_teams = "YES" if findings.get('has_teams') else "NO"
    has_schedule = "YES" if findings.get('has_schedule') else "NO"
    has_roster = "YES" if findings.get('has_roster_in_team') else "NO"

    print("{:<40} {:>10} {:>10} {:>10} {:>10}".format(
        filename[:40], has_members, has_teams, has_schedule, has_roster
    ))

# Save detailed analysis
with open('analysis_results.json', 'w') as f:
    json.dump(results, indent=4, fp=f)

print("\n[SUCCESS] Detailed analysis saved to analysis_results.json")
