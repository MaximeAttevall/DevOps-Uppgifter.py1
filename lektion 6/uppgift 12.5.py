notes = {
    "Meddelande från skolan": "Friluftsdag på tisdag",
    "Kom ihåg": "Ta bilen till verkstad",
    "Inför tentamen": "Gör alla instuderingsuppgifter"

}

x = input("Skriv rubrik på den artikel du vill ta bort: ")

del notes[x]


for key in notes:
    print("----")
    print("Titel: ", key )
    print("Text: ", notes[key])