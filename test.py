import requests

def get_tba_api_key():
    return 'H50WEWo0KtTzyihWF71B78hFAV68oHSkIjJ5XHBdttUm6mE92wP0GCvSC98NuWuk'

def get_team_events(team_key, year):
    url = f'https://www.thebluealliance.com/api/v3/team/{team_key}/events/{year}/simple'
    response = requests.get(url, headers={'X-TBA-Auth-Key': get_tba_api_key()})
    return response.json()

def get_event_teams(event_key):
    url = f'https://www.thebluealliance.com/api/v3/event/{event_key}/teams/simple'
    response = requests.get(url, headers={'X-TBA-Auth-Key': get_tba_api_key()})
    return response.json()

def main():
    team_key = input("Enter your team number (e.g., frc254): ")
    year = input("Enter the year (e.g., 2023): ")


    events = get_team_events(team_key, year)

    unique_teams = set()
    unique_countries = set()
    unique_states = set()
    unique_cities = set()

    for event in events:
        event_key = event['key']
        event_teams = get_event_teams(event_key)

        for team in event_teams:
            team_number = team['team_number']
            team_country = team['country']
            team_state_prov = team['state_prov']
            team_city = team['city']

            unique_teams.add(team_number)
            unique_countries.add(team_country)
            unique_states.add(team_state_prov)
            unique_cities.add(team_city)

    print("\nInformation for Team", team_key, "in the", year, "season:")
    print("Unique Teams:", unique_teams)
    print("Unique Countries:", unique_countries)
    print("Unique States/Provinces:", unique_states)
    print("Unique Cities:", unique_cities)

if __name__ == "__main__":
    main()
