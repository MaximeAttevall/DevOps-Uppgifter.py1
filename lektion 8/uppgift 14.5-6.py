# 14.5

#Följde mahmuds kod under lektionen och la till det sista ga, gd , p, d , l
teams = {
    "Brazil":
        {"wins": 2, "draws": 1, "losses": 0, "goals_for": 5, "goals_against": 1},
    "Serbia":
        {"wins": 1, "draws": 0, "losses": 2, "goals_for": 2, "goals_against": 4},
    "Switzerland":
        {"wins": 1, "draws": 2, "losses": 0, "goals_for": 5, "goals_against": 4},
    "Costa Rica":
        {"wins": 0, "draws": 1, "losses": 2, "goals_for": 2, "goals_against": 5}
}


def make_list(dictionary):
    new_lista = []

    for country in dictionary:
        country_dict = {
            "country": country,
            "wins": teams[country]["wins"],
            "draws": teams[country]["draws"],
            "losses": teams[country]["losses"],
            "goals_for": teams[country]["goals_for"],
            "goals_against": teams[country]["goals_against"]
        }

        new_lista.append(country_dict)

    return new_lista


my_list = make_list(teams)

summa = 0
for country in my_list:
    summa += country["wins"]

print("Summan av alla wins:", summa)


def print_table(lista):
    print("-" * 50)
    print("| # |", "Nation".ljust(11), "| W | D | L | GF | GA | GD | P |")
    print("-" * 50)
    num = 0
    for stats in lista:
        c = stats["country"].ljust(11)
        w = stats["wins"]
        d = stats["draws"]
        l = stats["losses"]
        gf = stats["goals_for"]
        ga = stats["goals_against"]
        gd = str(stats["goals_for"] - stats["goals_against"]).rjust(2)
        p = stats["wins"] * 3 + stats["draws"]
        num += 1
        print(f"| {num} | {c} | {w} | {d} | {l} | {gf} | {ga} | {gd} | {p} |")


print_table(my_list)
