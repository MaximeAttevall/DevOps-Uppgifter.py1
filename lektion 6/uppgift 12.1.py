notes = {
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Kom ihåg": "Ta bilen till verkstad",
    "Inför tentamen": "Gör alla instuderingsuppgifter"

}

x = input("antecking >")
if x not in notes:
    print("detta finns ej med som alternativ")
else:
    print(notes[x])


