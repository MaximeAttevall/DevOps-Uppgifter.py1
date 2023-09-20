teams = {
    "Brazil": {
        "wins": 2,
        "draws": 1,
        "losses": 0,
        "goals_for": 5,
        "goals_against": 1
    },
    "Serbia": {
        "wins": 1,
        "draws": 0,
        "losses": 2,
        "goals_for": 2,
        "goals_against": 4
    }
}


def make_list(dictionary):
    lista = []

    for countries in teams:
        countries_dict = {
            "country": countries,
            "wins": (teams[countries]["wins"]),
            "draws": (teams[countries]["draws"]),
            "losses": (teams[countries]["losses"]),
            "goals_for": (teams[countries]["goals_for"]),
            "goals_against": (teams[countries]["goals_against"])
        }

        lista.append(countries_dict)

    return lista


print(make_list(teams))
my_list = make_list(teams)

#Extra övning, summera alla wins ;)
summa = 0
for country in my_list:
    summa += country["wins"]

print("summa av alla wins är: ", summa)