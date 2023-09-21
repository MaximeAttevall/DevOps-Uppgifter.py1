teams = {
    "Brazil": {
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
    },
    "Serbia": {
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
    },
    "Switzerland": {
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
    },
    "Costa Rica": {
        "wins": 0,
        "draws": 0,
        "losses": 0,
        "goals_for": 0,
        "goals_against": 0,
    },
}


def add_game(home_team, home_score, away_team, away_score):
    teams[home_team]["wins"] += (home_score > away_score)
    teams[home_team]["draws"] += (home_score == away_score)
    teams[home_team]["losses"] += (home_score < away_score)
    teams[home_team]["goals_for"] += home_score
    teams[home_team]["goals_against"] += away_score

    teams[away_team]["wins"] += (away_score > home_score)
    teams[away_team]["draws"] += (away_score == home_score)
    teams[away_team]["losses"] += (away_score < home_score)
    teams[away_team]["goals_for"] += away_score
    teams[away_team]["goals_against"] += home_score



add_game("Costa Rica", 0, "Serbia", 1)
add_game("Brazil", 1, "Switzerland", 1)
add_game("Brazil", 2, "Costa Rica", 0)
add_game("Serbia", 1, "Switzerland", 2)
add_game("Serbia", 0, "Brazil", 2)
add_game("Switzerland", 2, "Costa Rica", 2)

for competitor in teams:
    wins = teams[competitor]["wins"]
    draws = teams[competitor]["draws"]
    losses = teams[competitor]["losses"]
    goals_for = teams[competitor]["goals_for"]
    goals_against = teams[competitor]["goals_against"]

    print(competitor)
    print("wins:", wins,"draws:", draws,"losses:", losses,"goals for:", goals_for,"goals against:", goals_against)

